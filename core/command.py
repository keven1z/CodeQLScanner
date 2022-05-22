# __*__coding=utf-8
import subprocess

from core.config import RUN_CODEQL_BIN_PATH, ROOT_PATH
from core.data import *


class Commands(object):

    def __init__(self):
        self.database_name = None
        self._CODEQL_CMD = ["cd", RUN_CODEQL_BIN_PATH, "&&"]
        self._CODEQL_ANALYSE_COMMAND = ["codeql", "database", "analyze", "--format=sarif-latest",
                                        f"--output={ROOT_PATH}/output/{COMMAND_OUTPUT_FLAG}.json", "--rerun",
                                        COMMAND_DATABASE_REPLACE_FLAG,
                                        COMMAND_RULE_REPLACE_FLAG]
        self._CODEQL_CREATE_COMMAND = ["codeql", "database", "create",
                                       f"{ROOT_PATH}/database/{COMMAND_CREATE_DATABASE_NAME_REPLACE_FLAG}",
                                       "--language=java", "--overwrite", "--command=mvn clean package",
                                       f"--source-root={COMMAND_CREATE_PROJECT_PATH_REPLACE_FLAG}"]

    def _pre_analyze(self, database, rule):
        self._CODEQL_ANALYSE_COMMAND = [item.replace(COMMAND_DATABASE_REPLACE_FLAG, database) for item in
                                        self._CODEQL_ANALYSE_COMMAND]
        self._CODEQL_ANALYSE_COMMAND = [item.replace(COMMAND_RULE_REPLACE_FLAG, rule) for item in
                                        self._CODEQL_ANALYSE_COMMAND]
        self._CODEQL_ANALYSE_COMMAND = [item.replace(COMMAND_OUTPUT_FLAG, self.database_name) for item in
                                        self._CODEQL_ANALYSE_COMMAND]

    def analyze(self, database, rule):
        """
        codeql 分析数据库
        :param database: 数据库的路径
        :param rule: 查询语句
        """
        self._pre_analyze(database, rule)
        self._run_cmd(self._CODEQL_CMD + self._CODEQL_ANALYSE_COMMAND)

    def _pre_create(self, database_name, project):
        self.database_name = database_name
        self._CODEQL_CREATE_COMMAND = [item.replace(COMMAND_CREATE_DATABASE_NAME_REPLACE_FLAG, database_name) for item
                                       in
                                       self._CODEQL_CREATE_COMMAND]
        self._CODEQL_CREATE_COMMAND = [item.replace(COMMAND_CREATE_PROJECT_PATH_REPLACE_FLAG, project) for item in
                                       self._CODEQL_CREATE_COMMAND]

    def create(self, database_name, project):
        """
        codeql创建数据库
        :param database_name:  生成数据库名称
        :param project: 项目路径
        """
        self._pre_create(database_name, project)
        self._run_cmd(self._CODEQL_CMD + self._CODEQL_CREATE_COMMAND)

    def _run_cmd(self, cmd):
        print(cmd)
        result = subprocess.run(cmd, shell=True,
                                stdout=subprocess.PIPE)  # 当命令是错误的时候，返回的状态码就不是0了
        # print("result: %s" % ret2.stdout.decode("gbk"))
        return result
