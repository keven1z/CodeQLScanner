import os

from core.codeql.download import get_CodeQL
from core.config import *
from core.data import *
from core.exception.env import CodeQLBinNotFoundError, CodeQLCLiNotFoundError
from core.log.log_util import LogUtil as log

logger = log.getLogger(__name__)


def file_check():
    '''
    检测关键文件夹的创建
    '''

    if not os.path.isdir(RUN_CODEQL_ROOT_PATH):
        os.makedirs(RUN_CODEQL_ROOT_PATH)
    if not os.path.isdir(LOGS_PATH):
        os.makedirs(LOGS_PATH)

    if not os.path.isdir(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    if not os.path.isdir(DATABASE_PATH):
        os.makedirs(DATABASE_PATH)


def init():
    file_check()
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
