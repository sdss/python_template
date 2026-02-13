#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2025-12-29
# @Filename: tasks.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import datetime
import pathlib
import subprocess
import urllib.request

from typing import Any

import colorama
import yaml


colorama.init()


def get_binary_path(binary: str) -> pathlib.Path | None:
    """Returns the path to a binary if it exists in PATH."""

    result = subprocess.run(
        ["which", binary],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        return pathlib.Path(result.stdout.strip())

    return None


def delete_copier_files(keep_answers: bool = False) -> None:
    """Deletes the post_copy.py file."""

    file_path = pathlib.Path(__file__).resolve()
    if file_path.exists():
        file_path.unlink(missing_ok=True)
        print(colorama.Fore.WHITE + "  > Deleted post_copy.py file.")

    answers_path = pathlib.Path.cwd() / ".copier-answers.yml"
    if not keep_answers and answers_path.exists():
        answers_path.unlink(missing_ok=True)
        print(colorama.Fore.WHITE + "  > Deleted .copier-answers.yml file.")


def get_license_text(license_file: str) -> str:
    """Returns the text of a license file."""

    url = f"https://raw.githubusercontent.com/sdss/python_template/refs/heads/python-template-v3/licenses/{license_file}"

    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def update_license(license: str) -> bool:
    """Updates the LICENSE file with the selected license."""

    dst_file = pathlib.Path.cwd() / "LICENSE"
    license_text: str = ""

    if license == "BSD-3-Clause":
        # The template includes this license by default.
        pass
    else:
        license_text = get_license_text(license)
        with dst_file.open("w") as f:
            f.write(license_text)

    # Update the copyright year
    with dst_file.open("a+") as f:
        f.seek(0)
        text = f.read()
        text = text.replace(
            "{{ year }}",
            str(datetime.datetime.now().year),
        )
        f.seek(0)
        f.truncate(0)
        f.write(text)
        f.truncate()

    print(colorama.Fore.WHITE + f"  > Updated LICENSE file to {license}.")

    return True


def run_command(
    command: list[str] | str,
    cwd: pathlib.Path | None = None,
    success_message: str | None = None,
    error_message: str | None = None,
    shell: bool = False,
    exit_on_error: bool = False,
    keep_answers: bool = False,
) -> bool:
    """Runs a command in a subprocess."""

    if shell:
        command = " ".join(command) if isinstance(command, list) else command

    cwd = cwd or pathlib.Path.cwd()

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        cwd=cwd,
        shell=shell,
    )

    if result.returncode != 0:
        if error_message:
            print(colorama.Fore.RED + f"  ! {error_message}")
            print(colorama.Fore.RED + result.stderr)

        if exit_on_error:
            delete_copier_files(keep_answers=keep_answers)
            exit(1)

        return False
    else:
        if success_message:
            print(colorama.Fore.WHITE + f"  > {success_message}")
        return True


def post_copy():
    """Post copy tasks."""

    # Get the answers
    answer_file = pathlib.Path.cwd() / ".copier-answers.yml"
    answers: dict[str, Any] = {}
    if answer_file.exists():
        answers = yaml.safe_load(answer_file.read_text())
        print(colorama.Fore.WHITE + "  > Parsed Copier answers file.")
    else:
        print(colorama.Fore.YELLOW + "  ! No Copier answers file found.")
        delete_copier_files()
        return

    keep_answers = answers.get("keep_answers", False)
    project_name = answers.get("project_name", "").strip()

    if not project_name:
        print(colorama.Fore.RED + "  ! No project name found in answers.")
        delete_copier_files(keep_answers=keep_answers)
        return

    # Update the LICENSE file
    license = answers.get("license", "BSD-3-Clause").strip()
    update_license(license)

    # Sync the project with 'uv' if requested
    if answers.get("sync_project", True):
        uv_path = get_binary_path("uv")
        if not uv_path:
            print(
                colorama.Fore.YELLOW
                + "  ! 'uv' binary not found in PATH. Skipping project sync."
            )
        else:
            cwd = pathlib.Path.cwd().resolve()
            run_command(
                [
                    "UV_ACTIVE=0",
                    f"UV_PROJECT_ENVIRONMENT={cwd!s}/.venv",
                    f"VIRTUAL_ENV={cwd!s}/.venv",
                    "UV_PYTHON=''",
                    str(uv_path),
                    "sync",
                    "--all-groups",
                    "--all-extras",
                ],
                shell=True,
                success_message="Project synced with 'uv'.",
                error_message="Failed to sync project with 'uv'.",
            )

    # If git is available, initialize a repository.
    git_path = get_binary_path("git")
    if not git_path:
        print(colorama.Fore.YELLOW + "  ! 'git' binary not found in PATH.")
    else:
        result = run_command(
            [str(git_path), "init"],
            success_message="Initialized git repository.",
            error_message="Failed to initialize git repository.",
        )

        github_organization = answers.get("github_organization", "").strip()
        push_to_github = answers.get("push_to_github", False)
        private = answers.get("private_repository", False)

        # If we are pushing to GitHub, set the remote and push. We need to add and
        # commit all files first but skip the copier files.
        if result and push_to_github and github_organization:
            # Set the remote
            github_repo_url = f"git@github.com:{github_organization}/{project_name}.git"
            run_command(
                [str(git_path), "remote", "add", "origin", github_repo_url],
                success_message=f"Added GitHub remote '{github_repo_url}'.",
                error_message="Failed to add GitHub remote.",
                exit_on_error=True,
                keep_answers=keep_answers,
            )

            # Stage all files
            run_command(
                [str(git_path), "add", "."],
                success_message="Staged all files for initial commit.",
                error_message="Failed to stage files for initial commit.",
                exit_on_error=True,
                keep_answers=keep_answers,
            )

            # Remove copier files from staging
            files_to_unstage = ["post_copy.py"]
            if not keep_answers:
                files_to_unstage.append(".copier-answers.yml")

            run_command(
                [str(git_path), "reset", "--"] + files_to_unstage,
                success_message="Removed copier files from staging.",
                error_message="Failed to remove copier files from staging.",
                exit_on_error=True,
                keep_answers=keep_answers,
            )

            # Commit
            run_command(
                [str(git_path), "commit", "-m", "Initial commit"],
                success_message="Created initial commit.",
                error_message="Failed to create initial commit.",
                exit_on_error=True,
                keep_answers=keep_answers,
            )

            # Create the GitHub repository using 'gh' CLI, if available.
            gh_cli_path = get_binary_path("gh")
            if gh_cli_path:
                if run_command(
                    [
                        str(gh_cli_path),
                        "repo",
                        "create",
                        f"{github_organization}/{project_name}",
                        "--private" if private else "--public",
                    ],
                    success_message="Created GitHub repository.",
                    error_message="Failed to create GitHub repository.",
                ):
                    run_command(
                        [str(git_path), "push", "-u", "origin", "main"],
                        success_message="Pushed initial commit to GitHub.",
                        error_message="Failed to push initial commit to GitHub.",
                    )
            else:
                print(
                    colorama.Fore.YELLOW
                    + "  ! 'gh' binary not found. Not creating GitHub repository."
                )

    # Delete docker files if we are not building and image.
    if not answers.get("build_docker_image", True):
        cwd = pathlib.Path.cwd()
        (cwd / "Dockerfile").unlink(missing_ok=True)
        (cwd / ".github" / "workflows" / "docker.yml").unlink(missing_ok=True)
        print(colorama.Fore.WHITE + "  > Deleted Dockerfile and GitHub workflow.")

    delete_copier_files(keep_answers=keep_answers)


if __name__ == "__main__":
    post_copy()
