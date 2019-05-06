# encoding: utf-8
#
# @Author: José Sánchez-Gallego
# @Date: Oct 11, 2017
# @Filename: logger.py
# @License: BSD 3-Clause
# @Copyright: José Sánchez-Gallego

# Adapted from astropy's logging system.

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import os
import re
import shutil
import sys
import traceback
import warnings
from logging.handlers import TimedRotatingFileHandler

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import get_lexer_by_name

from .color_print import color_text


__all__ = ['get_logger']


# Adds custom log level for print and twisted messages
PRINT = 15
logging.addLevelName(PRINT, 'PRINT')


def print_log_level(self, message, *args, **kws):
    self._log(PRINT, message, args, **kws)


logging.Logger._print = print_log_level


def print_exception_formatted(type, value, tb):
    """A custom hook for printing tracebacks with colours."""

    tbtext = ''.join(traceback.format_exception(type, value, tb))
    lexer = get_lexer_by_name('pytb', stripall=True)
    formatter = TerminalFormatter()
    sys.stderr.write(highlight(tbtext, lexer, formatter))


def colored_formatter(record):
    """Prints log messages with colours."""

    colours = {'info': ('blue', 'normal'),
               'debug': ('magenta', 'normal'),
               'warning': ('yellow', 'normal'),
               'print': ('green', 'normal'),
               'critical': ('red', 'bold'),
               'error': ('red', 'bold')}

    levelname = record.levelname.lower()

    if levelname.lower() in colours:
        levelname_color = colours[levelname][0]
        header = color_text('[{}]: '.format(levelname.upper()),
                            levelname_color)

    message = record.getMessage()

    if levelname == 'warning':
        warning_category_groups = re.match(r'^\w*?(.+?Warning) (.*)', message)
        if warning_category_groups is not None:
            warning_category, warning_text = warning_category_groups.groups()

            warning_category_colour = color_text('({})'.format(warning_category), 'cyan')
            message = '{} {}'.format(color_text(warning_text, ''), warning_category_colour)

    sys.__stdout__.write('{}{}\n'.format(header, message))
    sys.__stdout__.flush()

    return


class MyFormatter(logging.Formatter):

    base_fmt = '%(asctime)s - %(levelname)s - %(message)s'
    # base_fmt = '%(asctime)s - %(levelname)s - %(message)s [%(funcName)s @ %(filename)s]'

    ansi_escape = re.compile(r'\x1b[^m]*m')

    def __init__(self, fmt=base_fmt):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._fmt = MyFormatter.base_fmt

        elif record.levelno == logging.getLevelName('PRINT'):
            self._fmt = MyFormatter.base_fmt

        elif record.levelno == logging.INFO:
            self._fmt = MyFormatter.base_fmt

        elif record.levelno == logging.ERROR:
            self._fmt = MyFormatter.base_fmt

        elif record.levelno == logging.CRITICAL:
            self._fmt = MyFormatter.base_fmt

        elif record.levelno == logging.WARNING:
            self._fmt = MyFormatter.base_fmt

        record.msg = self.ansi_escape.sub('', record.msg)

        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._fmt = format_orig

        return result


Logger = logging.getLoggerClass()


class LoggerStdout(object):
    """A pipe for stdout to a logger."""

    def __init__(self, level):
        self.level = level

    def write(self, message):

        if message != '\n':
            self.level(message)

    def flush(self):
        pass


class MyLogger(Logger):
    """This class is used to set up the logging system.

    The main functionality added by this class over the built-in
    logging.Logger class is the ability to keep track of the origin of the
    messages, the ability to enable logging of warnings.warn calls and
    exceptions, and the addition of colorized output and context managers to
    easily capture messages to a file or list.

    It is adapted from the astropy logging system.

    """

    def save_log(self, path):
        shutil.copyfile(self.log_filename, os.path.expanduser(path))

    def _catch_exceptions(self, exctype, value, tb):
        """Catches all exceptions and logs them."""

        # Now we log it.
        self.error('Uncaught exception', exc_info=(exctype, value, tb))

        # First, we print to stdout with some colouring.
        print_exception_formatted(exctype, value, tb)

    def warning(self, msg, category=None, **kwargs):
        """Redirects logging to `warnings.warn`."""

        if category is None:
            category = UserWarning

        full_message = '{0} {1}'.format(category.__name__, msg)

        return Logger.warning(self, full_message, **kwargs)

    def set_defaults(self, log_level=logging.INFO, redirect_stdout=False):
        """Reset logger to its initial state."""

        # Disable astropy logging if present because it uses the same override
        # of showwarning than us and messes up things
        try:
            from astropy import log
            log.disable_warnings_logging()
            log.disable_exception_logging()
        except Exception:
            pass

        # Remove all previous handlers
        for handler in self.handlers[:]:
            self.removeHandler(handler)

        # Set levels
        self.setLevel(logging.DEBUG)

        # Set up the stdout handler
        self.fh = None
        self.sh = logging.StreamHandler()
        self.sh.emit = colored_formatter
        self.addHandler(self.sh)

        self.sh.setLevel(log_level)

        # Redirects all stdout to the logger
        if redirect_stdout:
            sys.stdout = LoggerStdout(self._print)

        # Catches exceptions
        sys.excepthook = self._catch_exceptions

        warnings.showwarning = self._showwarning

    def _showwarning(self, *args, **kwargs):

        message = args[0]
        category = args[1]
        mod_path = args[2]

        mod_name = None
        mod_path, ext = os.path.splitext(mod_path)

        for name, mod in list(sys.modules.items()):
            try:
                path = os.path.splitext(getattr(mod, '__file__', ''))[0]
            except Exception:
                continue
            if path == mod_path:
                mod_name = mod.__name__
                break

        if mod_name is not None:
            self.warning(message, category, extra={'origin': mod_name})
        else:
            self.warning(message, category)

    def start_file_logger(self, path, log_file_level=logging.DEBUG):
        """Start file logging."""

        log_file_path = os.path.expanduser(path)
        log_dir = os.path.dirname(log_file_path)

        try:

            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            self.fh = TimedRotatingFileHandler(str(log_file_path), when='midnight', utc=True)
            self.fh.suffix = '%Y-%m-%d_%H:%M:%S'

        except (IOError, OSError) as ee:

            self.warning('log file {0!r} could not be '
                         'opened for writing: {1}'.format(log_file_path, ee),
                         RuntimeWarning)

        else:

            self.fh.setFormatter(MyFormatter())
            self.addHandler(self.fh)
            self.fh.setLevel(log_file_level)

            self.log_filename = log_file_path

        self.debug('starting file logger at ' + log_file_path)

    def set_level(self, level):
        """Sets levels for both sh and (if initialised) fh."""

        self.sh.setLevel(level)

        if self.fh:
            self.fh.setLevel(level)


def get_logger(name):
    """Gets a new logger."""

    orig_logger = logging.getLoggerClass()

    logging.setLoggerClass(MyLogger)

    log = logging.getLogger(name)
    log.set_defaults()

    logging.setLoggerClass(orig_logger)

    return log
