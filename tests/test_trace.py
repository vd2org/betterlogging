# Copyright (C) 2020-2024 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


import betterlogging as logging


def test_trace():
    logger = logging.getLogger("test")

    logger.setLevel(logging.TRACE)
    logging.root.setLevel(logging.TRACE)

    logger.trace("some trace message")
    logging.trace("some trace message")
    logging.root.trace("some trace message")
