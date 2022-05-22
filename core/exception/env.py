class EnvError(FileNotFoundError):
    pass


class CodeQLBinNotFoundError(EnvError):
    """
    CodeQl bin 文件缺少异常
    """
    pass


class CodeQLCLiNotFoundError(EnvError):
    """
    CodeQl cli 文件缺少异常
    """
    pass


class DownloadCodeQLError(EnvError):
    pass
