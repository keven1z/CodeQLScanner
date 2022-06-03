import argparse
import sys
from xmlrpc.client import boolean

'''
options:
    -ql:CodeQL查询规则文件相对路径
    -p/--project 项目绝对路径
    -l/--list 列举所有ql查询规则
'''


def parse_option():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ql", dest="ql", help="Please specify a ql rule path to query")
    parser.add_argument("-p", "--project", dest="project", help="Please specify a project absolute path to scan")
    parser.add_argument("--proxy", dest="proxy", help="Set proxy for downloading CodeQL dependent file")

    parser.add_argument("-l", "--list", dest="list",action='store_true', help="Holds if list all query rules")

    options = parser.parse_args()
    option = Option()
    ql = options.ql

    option.ql = ql
    option.project = options.project
    option.proxy = options.proxy
    option.list = options.list
    return option


class Option(object):
    def __init__(self):
        self._ql = None
        self._project = None
        self._list = None
        self._proxy = None

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

    @property
    def proxy(self):
        return self._proxy

    @proxy.setter
    def proxy(self, value):
        self._proxy = value
