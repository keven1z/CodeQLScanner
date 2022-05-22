import sys

from core.command import Commands
from core.config import RUN_CODEQL_LIB_PATH, ROOT_PATH
from core.init import init
from core.options.optparse import parse_option


def main():
    options = parse_option()
    init(options)

    project_path = options.project
    if not isinstance(project_path, str): return
    database_name = project_path[project_path.rindex('\\\\') + 2:]
    command = Commands()
    command.create(database_name, project_path)
    database_path = f"{ROOT_PATH}/database/{database_name}"
    ql_path = f"{RUN_CODEQL_LIB_PATH}/{options.ql}"
    command.analyze(database_path, ql_path)


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
