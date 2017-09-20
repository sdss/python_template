#!/usr/bin/env python
# encoding: utf-8

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import sys
import traceback
import warnings
import yaml

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

from .misc.color_print import color_text


NAME = 'python_template'

# Loads config
config = yaml.load(open(os.path.dirname(__file__) + '/../../etc/{0}.cfg'.format(NAME)))


# Monkeypatches formatwarning and error handling
def warning_on_one_line(message, category, filename, lineno, file=None, line=None):

    basename = os.path.basename(filename)
    category_colour = color_text('[{}]'.format(category.__name__), 'yellow')

    return '{}: {} ({}:{})\n'.format(category_colour, message, basename, lineno)


warnings.formatwarning = warning_on_one_line

warnings.filterwarnings(
    'ignore', 'Matplotlib is building the font cache using fc-list. This may take a moment.')


def custom_except_hook(type, value, tb):
    """A custom hook for printing tracebacks with colours."""

    tbtext = ''.join(traceback.format_exception(type, value, tb))
    lexer = get_lexer_by_name('pytb', stripall=True)
    formatter = TerminalFormatter()
    sys.stderr.write(highlight(tbtext, lexer, formatter))


__version__ = '0.2.0dev'
