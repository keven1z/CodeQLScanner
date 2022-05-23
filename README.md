# CodeQLScanner
集成CodeQL生成数据库，分析数据库的能力，更方便的使用CodeQL扫描代码
# 环境
* python 3.6
* maven
* jdk

# 使用
```shell
git clone https://github.com/keven1z/CodeQLScanner.git
cd CodeQLScanner
pip install requirements.txt
python main.py -p {项目绝对路径} -ql {查询规则相对java/ql/src/Security路径}
```

```
  -h, --help            show this help message and exit
  -ql QL                Please specify a ql rule path to query
  -p PROJECT, --project PROJECT
                        Please specify a project absolute path to scan
  --proxy PROXY         set proxy for downloading file
  -l LIST, --list LIST  List all query rules
```
