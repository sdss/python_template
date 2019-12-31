# encoding: utf-8

from .utils import get_config, get_logger


NAME = '{{cookiecutter.package_name}}'


# Loads config
config = get_config(NAME)


# Inits the logging system. Only shell logging, and exception and warning catching.
# File logging can be started by calling log.start_file_logger(path).
log = get_logger(NAME)


__version__ = '{{cookiecutter.version}}'
