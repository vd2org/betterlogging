# Copyright (C) 2020-2022 by Vd.
# This file is part of BetterLogging, my logging improvement.
# BetterLogging is released under the MIT License (see LICENSE).


import logging
from logging import Formatter
from logging import LogRecord

from .colors import colors
from .outer.better_exceptions import ExceptionFormatter
from .trace import TRACE

DEFAULT_FORMAT = '%(c_fg_green)s%(asctime)s %(c_color)s%(levelname)-8s%(c_reset)s %(c_fg_cyan)s[%(name)s] ' \
                 '%(c_reset)s(%(filename)s:%(c_underscore)s%(funcName)s%(c_reset)s:%(lineno)d) ' \
                 '%(c_color)s%(message)s%(c_reset)s'

DEFAULT_LEVEL_COLORS = {
    TRACE: colors['c_fg_cyan'] + colors['c_bright'],
    logging.DEBUG: colors['c_fg_blue'] + colors['c_bright'],
    logging.INFO: colors['c_fg_white'] + colors['c_bright'],
    logging.WARN: colors['c_fg_yellow'] + colors['c_bright'],
    logging.ERROR: colors['c_fg_red'] + colors['c_bright'],
    logging.CRITICAL: colors['c_bg_red'] + colors['c_fg_white'] + colors['c_bright'],
    None: colors['c_reset']
}


class ColorizedFormatter(Formatter):
    def __init__(self, fmt=None, level_colors=None, hide_lib_diagnose=True, *args, **kwargs):
        self.level_colors = level_colors or DEFAULT_LEVEL_COLORS
        fmt = fmt or DEFAULT_FORMAT
        self._formatter = ExceptionFormatter(colorize=True, backtrace=False, diagnose=True,
                                             hide_lib_diagnose=hide_lib_diagnose)

        super().__init__(fmt=fmt, *args, **kwargs)

    def format(self, record: LogRecord) -> str:
        color = self.level_colors.get(record.levelno, self.level_colors.get(None, ""))
        orig = record.__dict__
        record.__dict__ = {**colors, "c_color": color, **record.__dict__}
        out = super().format(record)
        record.__dict__ = orig
        return out

    def formatException(self, ei) -> str:
        ex = self._formatter.format_exception(*ei)
        return "".join(ex)
