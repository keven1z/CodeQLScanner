# -*- coding: utf-8 -*-
from tqdm import tqdm
import requests
import zipfile

from core.config import RUN_CODEQL_ROOT_PATH
from core.exception.env import DownloadCodeQLError
from core.log.log_util import LogUtil as log

logger = log.getLogger(__name__)


def get_CodeQL(url, file_name, proxy=None):
    try:
        logger.info(f"正在下载{file_name}.zip")
        _download(url, f"{file_name}.zip", proxy)
        _unzip(f"{RUN_CODEQL_ROOT_PATH}/{file_name}.zip", f"{RUN_CODEQL_ROOT_PATH}")
    except Exception as e:
        raise DownloadCodeQLError(e)


def _download(url, download_file, proxy=None):
    """
    下载文件
    :param url: 下载文件url
    :param download_file: 下载文件的路径
    """
    if proxy is None:
        proxies = None
    else:
        proxies = {
            "http": proxy,
        }

    try:
        response = requests.get(url, stream=True, proxies=proxies)
    except ConnectionError as e:
        raise ConnectionError(f"Connection {url} timeout")
    with open(f"{RUN_CODEQL_ROOT_PATH}/{download_file}", "wb") as f:
        content_length = response.headers.get("content-length")
        if content_length is None: raise DownloadCodeQLError(f"没有获取到response content length, "
                                                             f"response.headers.get(\"content-length\") "
                                                             f"return {content_length}")

        content_size = int(response.headers.get("content-length")) / 1024
        for data in tqdm(iterable=response.iter_content(1024), total=content_size, unit='k', desc=download_file):
            f.write(data)


def _unzip(zip_path, unzip_path):
    zip_file = zipfile.ZipFile(zip_path)
    with tqdm(total=len(zip_file.namelist()), desc=f'unzip {zip_path}', leave=True, ncols=100, unit='it',
              unit_scale=True) as pbar:
        for names in zip_file.namelist():
            zip_file.extract(names, unzip_path)
            pbar.update(1)
        zip_file.close()
