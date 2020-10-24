# BetterLogging


![BetterLogging](https://telegra.ph/file/ebd3b272eb1969dd55f58.png "BetterLogging")

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

#### In code

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

def div(x: int, y: int) -> float:
    return x / y

try:
    div(1, 0)
except:
    logger.exception("Some exception")
```

#### Config for `uvicorn`

```json
{
  "version": 1,
  "disable_existing_loggers": false,
  "formatters": {
    "default": {
      "()": "betterlogging.ColorizedFormatter"
    },
    "access": {
      "()": "betterlogging.ColorizedFormatter",
      "fmt": "%(c_fg_green)s%(asctime)s %(c_color)s%(levelname)-8s%(c_reset)s %(c_fg_cyan)s[%(name)s] %(c_reset)s%(message)s"
    }
  },
  "handlers": {
    "default": {
      "formatter": "default",
      "class": "logging.StreamHandler"
    },
    "access": {
      "formatter": "access",
      "class": "logging.StreamHandler",
      "stream": "ext://sys.stdout"
    }
  },
  "loggers": {
    "": {
      "handlers": [
        "default"
      ],
      "level": "DEBUG"
    },
    "uvicorn.error": {
      "level": "INFO"
    },
    "uvicorn.access": {
      "handlers": [
        "access"
      ],
      "level": "INFO",
      "propagate": false
    }
  }
}
```

```shell script
uvicorn application:app --debug --reload --log-config ./logging.json
```