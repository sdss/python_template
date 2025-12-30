#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2025-12-29
# @Filename: tasks.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import pathlib
import subprocess

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

        if result and push_to_github and github_organization:
            github_repo_url = f"git@github.com:{github_organization}/{project_name}.git"
            run_command(
                [str(git_path), "remote", "add", "origin", github_repo_url],
                success_message=f"Added GitHub remote '{github_repo_url}'.",
                error_message="Failed to add GitHub remote.",
                exit_on_error=True,
                keep_answers=keep_answers,
            )

            run_command(
                [str(git_path), "add", "."],
                success_message="Staged all files for initial commit.",
                error_message="Failed to stage files for initial commit.",
                exit_on_error=True,
                keep_answers=keep_answers,
            )

            run_command(
                [str(git_path), "commit", "-m", "Initial commit"],
                success_message="Created initial commit.",
                error_message="Failed to create initial commit.",
                exit_on_error=True,
                keep_answers=keep_answers,
            )

            gh_path = get_binary_path("gh")
            if gh_path:
                if run_command(
                    [
                        str(gh_path),
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

    delete_copier_files(keep_answers=keep_answers)


if __name__ == "__main__":
    post_copy()
