# Copyright (C) 2020 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


import betterlogging as logging


def test_colorized():
    logger = logging.getLogger("test")

    handler = logging.StreamHandler()
    handler.setFormatter(logging.ColorizedFormatter())

    logger.addHandler(handler)
    logger.setLevel(logging.TRACE)

    logger.trace("some trace message")
    logger.debug("some debug message")
    logger.info("some info message")
    logger.warning("some warning message")
    logger.error("some error message")
    logger.critical("some critical message")

    try:
        raise TypeError
    except TypeError:
        logger.exception("some exception")
