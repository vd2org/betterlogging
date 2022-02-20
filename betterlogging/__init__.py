# Copyright (C) 2020-2022 by Vd.
# This file is part of BetterLogging, my logging improvement.
# BetterLogging is released under the MIT License (see LICENSE).


import logging
from logging import *  # noqa: F401, F403
from logging import root
from typing import TYPE_CHECKING, Optional

from .colorized import ColorizedFormatter  # noqa: F401
from .trace import TRACE, TRACE_NAME


class BetterLogger(logging.Logger):
    def trace(self, msg, *args, **kwargs):
        if self.isEnabledFor(TRACE):
            self._log(TRACE, msg, args, **kwargs)


def trace(msg, *args, **kwargs):
    if len(logging.root.handlers) == 0:
        logging.basicConfig()
    logging.root.trace(msg, *args, **kwargs)  # noqa


logging.addLevelName(TRACE_NAME, TRACE)

logging.Logger.trace = BetterLogger.trace
logging.trace = trace
logging.TRACE = TRACE

if TYPE_CHECKING:
    Logger = BetterLogger
    root: Logger = root  # noqa


    def getLogger(name=None) -> 'Logger':  # noqa: E303
        return logging.getLogger(name)


def basic_colorized_config(**kwargs):
    """
    Same as logging.basicConfig, but sets ColorizedFormatter as default for any SeamHandler in root logger
    :return:
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(ColorizedFormatter())
    kwargs.update({'handlers': [stream_handler]})
    return logging.basicConfig(**kwargs)


def get_colorized_logger(name: Optional[str] = None) -> 'Logger':
    """
    Use this function to get an instance of logger with ColorizedFormatter.
    Warning! If you will set basic_colorized_config(), logs produced with this logger would duplicated.
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = ColorizedFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
