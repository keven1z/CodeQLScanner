import argparse
import sys

'''
options:
    -ql:CodeQL查询规则文件相对路径
    -p/--project 项目绝对路径
    -l/--list 列举所有ql查询规则
'''


def parse_option():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ql", dest="ql", help="Please specify a ql rule path to query", required=True)
    parser.add_argument("-p", "--project", dest="project", help="Please specify a project absolute path to scan",
                        required=True)
    parser.add_argument("-l", "--list", dest="list", help="List all query rules")

    options = parser.parse_args()
    option = Option()
    ql = options.ql

    option.ql = ql
    option.project = options.project
    return option


class Option(object):
    def __init__(self):
        self._ql = None
        self._project = None
        self._list = None

    @property
    def ql(self):
        return self._ql

    @ql.setter
    def ql(self, value):
        self._ql = value

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, value):
        self._project = value

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        self._list = value