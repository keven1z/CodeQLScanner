import os
import os


def walk_dir(filepath):
    ql_files = []
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for _ in files:
        fi_d = os.path.join(filepath, _)
        if os.path.isdir(fi_d):
            ql_files += walk_dir(fi_d)
        elif os.path.splitext(fi_d)[1] == '.ql':
            ql_files.append(os.path.join(filepath, fi_d))
    return ql_files
