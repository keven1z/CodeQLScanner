import os

from core.codeql.download import get_CodeQL
from core.config import *
from core.data import *
from core.exception.env import CodeQLBinNotFoundError, CodeQLCLiNotFoundError
from core.log.log_util import LogUtil as log
from core.options.optparse import parse_option
from core.codeql.bean import CodeQLBean
from core.options.print import walk_dir
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
    codeQLbean, options = init_options()
    file_check()
    env_check(options)
    return codeQLbean


def init_options():
    '''
    初始化选项
    '''
    options = parse_option()
    project_path = options.project
    
    
    '''
    -l:打印所有存在的ql查询
    '''
    if options.list:
        ql_files = walk_dir(RUN_CODEQL_LIB_PATH)
        for _ in ql_files:
            print(_)
        exit(1)

    if project_path is not None and not isinstance(project_path, str):
        logger.error(f"输入参数类型错误：{project_path}")
        exit(-1)

    database_name = project_path[project_path.rindex('/') + 1:]
    database_path = f"{ROOT_PATH}/database/{database_name}"
    #ql_path = f"{RUN_CODEQL_LIB_PATH}/{options.ql}"
    return CodeQLBean(options.ql, database_path, database_name, project_path), options


def env_check(option):
    try:
        bin_check()
    except CodeQLBinNotFoundError:
        logger.info("没有发现CodeQL Cli bin")
        get_CodeQL(CODEQL_BIN_DOWNLOAD_URL, CODEQL_BIN, proxy=option.proxy)

    try:
        cli_check()
    except CodeQLCLiNotFoundError:
        logger.info("没有发现CodeQL Cli library")
        get_CodeQL(CODEQL_CLI_DOWNLOAD_URL, CODEQL_CLI, proxy=option.proxy)


def bin_check():
    if not os.path.isdir(RUN_CODEQL_BIN_PATH):
        raise CodeQLBinNotFoundError


def cli_check():
    if not os.path.isdir(RUN_CODEQL_LIB_PATH):
        raise CodeQLCLiNotFoundError
