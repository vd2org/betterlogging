# BetterLogging

Improved version of the standard logger.

* Added `TRACE` level.
* Added `ColorizedFormatter`.
* Added better traceback formatting.

This package patching the standard `logging` library.

Thus, after import, all improvements will be available inside the `logging` module.

But for better typing, I prefer to use `betterlogging` everywhere.

### Requirements

Python 3.6 and above. No any additional dependencies.

### Installation

`pip install betterlogging`

### Usage

```python
import betterlogging as logging

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
    a = 1/0
except:
    logger.exception("Some exception")
```
