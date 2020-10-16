# Copyright (C) 2020 by Vd.
# This file is part of BetterLogging, my logging improvement.
# BetterLogging is released under the MIT License (see LICENSE).


from typing import TYPE_CHECKING

import logging
from logging import *  # noqa: F401, F403
from logging import root
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
