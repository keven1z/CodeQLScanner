import sys

from core.command import Commands
from core.config import RUN_CODEQL_BIN_PATH, RUN_CODEQL_LIB_PATH, ROOT_PATH
from core.init import init
from core.options.print import walk_dir


def main():

    codeQLbean = init()
    command = Commands()
    result = command.create(codeQLbean.database_name, codeQLbean.project_path)
    command.analyze(codeQLbean.database_path, codeQLbean.ql_path)


def _main():
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(-1)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    _main()
