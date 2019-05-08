# encoding: utf-8
#
# @Author: José Sánchez-Gallego
# @Date: Oct 11, 2017
# @Filename: logger.py
# @License: BSD 3-Clause
# @Copyright: José Sánchez-Gallego

import datetime
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


def get_exception_formatted(tp, value, tb):
    """Adds colours to tracebacks."""

    tbtext = ''.join(traceback.format_exception(tp, value, tb))
    lexer = get_lexer_by_name('pytb', stripall=True)
    formatter = TerminalFormatter()
    return highlight(tbtext, lexer, formatter)


def colored_formatter(record):
    """Prints log messages with colours."""

    colours = {'info': 'blue',
               'debug': 'magenta',
               'warning': 'yellow',
               'critical': 'red',
               'error': 'red'}

    levelname = record.levelname.lower()

    if levelname.lower() in colours:
        levelname_color = colours[levelname]
        header = color_text('[{}]: '.format(levelname.upper()),
                            levelname_color)

    message = record.getMessage()

    if levelname == 'warning':
        warning_category_groups = re.match(r'^.*?\s*?(\w*?Warning): (.*)', message)
        if warning_category_groups is not None:
            warning_category, warning_text = warning_category_groups.groups()

            warning_category_colour = color_text('({})'.format(warning_category), 'cyan')
            message = '{} {}'.format(color_text(warning_text, ''), warning_category_colour)

    sys.__stdout__.write('{}{}\n'.format(header, message))
    sys.__stdout__.flush()

    return


class SDSSFormatter(logging.Formatter):
    """Custom `Formatter <logging.Formatter>`."""

    base_fmt = '%(asctime)s - %(levelname)s - %(message)s'
    ansi_escape = re.compile(r'\x1b[^m]*m')

    def __init__(self, fmt=base_fmt):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):

        record.msg = self.ansi_escape.sub('', record.msg)

        # The format of a warnings redirected with warnings.captureWarnings
        # has the format <path>: <category>: message\n  <some-other-stuff>.
        # We reorganise that into a cleaner message. For some reason in this
        # case the message is in record.args instead of in record.msg.
        if record.levelno == logging.WARNING and len(record.args) > 0:
            match = re.match(r'^(.*?):\s*?(\w*?Warning): (.*)', record.args[0])
            if match:
                message = '{1} - {2} [{0}]'.format(*match.groups())
                record.args = tuple([message] + list(record.args[1:]))

        return logging.Formatter.format(self, record)


class SDSSLogger(logging.Logger):
    """Custom logging system.

    Parameters
    ----------
    name : str
        The name of the logger.
    log_level : int
        The initial logging level for the console handler.
    capture_warnings : bool
        Whether to capture warnings and redirect them to the log.

    """

    def __init__(self, name, log_level=logging.INFO, capture_warnings=True):

        super(SDSSLogger, self).__init__(name)

        if name == 'py.warnings':
            return

        # Set levels
        self.setLevel(logging.DEBUG)

        # Sets the console handler
        self.sh = logging.StreamHandler()
        self.sh.emit = colored_formatter
        self.addHandler(self.sh)
        self.sh.setLevel(log_level)

        # Placeholders for the file handler.
        self.fh = None
        self.log_filename = None

        # Catches exceptions
        sys.excepthook = self._catch_exceptions

        self.warnings_logger = None
        self.capture_warnings(capture_warnings)

    def _catch_exceptions(self, exctype, value, tb):
        """Catches all exceptions and logs them."""

        self.error(get_exception_formatted(exctype, value, tb))

    def capture_warnings(self, action):
        """Capture warnings.

        If ``action`` is `True`, redirects all the warnings to a logger called
        ``py.warnings``. Handlers are added to that logger. If ``action=False``
        disable the warning capture.

        """

        if action is False:
            logging.captureWarnings(action)
            self.warnings_logger = None
            return

        assert self.sh is not None, 'shell handler must'

        logging.captureWarnings(action)

        self.warnings_logger = logging.getLogger('py.warnings')
        self.warnings_logger.addHandler(self.sh)

    def save_log(self, path):
        shutil.copyfile(self.log_filename, os.path.expanduser(path))

    def start_file_logger(self, path, log_level=logging.DEBUG):
        """Start file logging."""

        log_file_path = os.path.expanduser(path)
        logdir = os.path.dirname(log_file_path)

        try:

            if not os.path.exists(logdir):
                os.makedirs(logdir)

            if os.path.exists(log_file_path):
                strtime = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')
                shutil.move(log_file_path, log_file_path + '.' + strtime)

            self.fh = TimedRotatingFileHandler(
                str(log_file_path), when='midnight', utc=True)

            self.fh.suffix = '%Y-%m-%d_%H:%M:%S'

        except (IOError, OSError) as ee:

            warnings.warn('log file {0!r} could not be opened for '
                          'writing: {1}'.format(log_file_path, ee),
                          RuntimeWarning)

        else:

            self.fh.setFormatter(SDSSFormatter())
            self.addHandler(self.fh)
            self.fh.setLevel(log_level)

            if self.warnings_logger:
                self.warnings_logger.addHandler(self.fh)

            self.log_filename = log_file_path

    def set_level(self, level):
        """Sets levels for both sh and (if initialised) fh."""

        self.sh.setLevel(level)

        if self.fh:
            self.fh.setLevel(level)


def get_logger(name):
    """Gets a new logger."""

    orig_logger = logging.getLoggerClass()

    logging.setLoggerClass(SDSSLogger)

    log = logging.getLogger(name)

    logging.setLoggerClass(orig_logger)

    return log
