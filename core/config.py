from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
RUN_CODEQL_ROOT_PATH = f"{ROOT_PATH}/run"  # CodeQL依赖根路径
RUN_CODEQL_BIN_PATH = f"{RUN_CODEQL_ROOT_PATH}/codeql"  # CodeQL bin路径
RUN_CODEQL_LIB_PATH = f"{RUN_CODEQL_ROOT_PATH}/codeql-codeql-cli-latest/java/ql/src/Security"  # CodeQL 查询语句路径

LOGS_PATH = f"{ROOT_PATH}/logs"
OUTPUT_PATH = f"{ROOT_PATH}/output"
DATABASE_PATH = f"{ROOT_PATH}/database"



# CodeQL bin下载URL
CODEQL_BIN_DOWNLOAD_URL = "https://github.com/github/codeql-cli-binaries/releases/latest/download/codeql.zip"

# CodeQL cli下载URL
CODEQL_CLI_DOWNLOAD_URL = "https://github.com/github/codeql/archive/refs/tags/codeql-cli/latest.zip"
