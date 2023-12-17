import logging
import sys
from os.path import abspath, dirname
from os.path import join as pjoin

from core.logging import InterceptHandler
from loguru import logger
from starlette.config import Config
from starlette.datastructures import Secret

ROOT_DIR = dirname(dirname(dirname(abspath(__file__))))

config = Config(pjoin(ROOT_DIR, ".env"))

API_PREFIX = "/api"
VERSION = "{{cookiecutter.version}}"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="")

PROJECT_NAME: str = config("PROJECT_NAME", default="{{cookiecutter.project_name}}")

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
# 让logging的日志也是走loguru
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(
    handlers=[
        {"sink": sys.stderr, "level": LOGGING_LEVEL},
        {"sink": pjoin(ROOT_DIR, "app/logs/err.log"), "level": logging.ERROR}, # 只保存error级别以上的日志
    ]
)


MODEL_DIR = pjoin(
    ROOT_DIR, config("MODEL_DIR", default="{{cookiecutter.machine_learn_model_dir}}")
)

MODEL_NAME = config("MODEL_NAME", default="{{cookiecutter.machine_learn_model_name}}")
INPUT_EXAMPLE = pjoin(
    ROOT_DIR, config("INPUT_EXAMPLE", default="{{cookiecutter.input_example_path}}")
)
