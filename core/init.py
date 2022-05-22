import os

from core.codeql.download import get_CodeQL
from core.config import *
from core.data import *
from core.exception.env import CodeQLBinNotFoundError, CodeQLCLiNotFoundError
from core.log.log_util import LogUtil as log

logger = log.getLogger(__name__)


def init():
    env_check()


def env_check():
    try:
        bin_check()
    except CodeQLBinNotFoundError:
        logger.info("没有发现CodeQL Cli bin")
        get_CodeQL(CODEQL_BIN_DOWNLOAD_URL, CODEQL_BIN)

    try:
        cli_check()
    except CodeQLCLiNotFoundError:
        logger.info("没有发现CodeQL Cli library")
        get_CodeQL(CODEQL_CLI_DOWNLOAD_URL, CODEQL_CLI)


def bin_check():
    if not os.path.isdir(RUN_CODEQL_BIN_PATH):
        raise CodeQLBinNotFoundError


def cli_check():
    if not os.path.isdir(RUN_CODEQL_LIB_PATH):
        raise CodeQLCLiNotFoundError
