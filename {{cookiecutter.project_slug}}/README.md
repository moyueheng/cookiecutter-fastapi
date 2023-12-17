# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## 开发需求

- Python 3.11.0
- Pip
- conda (python 版本管理器)
- Poetry（Python 包管理器）

### 机器学习模型环境

```sh
MODEL_DIR=./ml/model/
MODEL_NAME=model.pkl
```

### 更新 `/predict`

要更新你的机器学习模型，请在 `predictor.py` 中[在此修改](app/api/routes/predictor.py#L19)你的 `load` 和 `method`

## 安装

```sh
conda create -n {{cookiecutter.project_slug}} -y  python=3.11
conda activate {{cookiecutter.project_slug}}
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
pip install poetry
poetry config virtualenvs.create false
make install
```

## 本地运行

`make run`

## 部署应用

`make deploy`

## 运行测试

`make test`

## 访问 Swagger 文档

> [http://localhost:8080/docs](http://localhost:8080/docs)

## 访问 Redocs 文档

> [http://localhost:8080/redoc](http://localhost:8080/redoc)

## 项目结构

与应用程序相关的文件位于 `app` 或 `tests` 目录。
应用程序部分包括：

    app
    |
    | # FastAPI 相关内容
    ├── api                 - 网络相关内容。
    │   └── routes          - 网络路由。
    ├── core                - 应用配置、启动事件、日志记录。
    ├── models              - 本应用的 pydantic 模型。
    ├── services            - 不仅仅是 CRUD 相关的逻辑。
    ├── main-aws-lambda.py  - [可选] AWS Lambda 创建和配置的 FastAPI 应用。
    └── main.py             - FastAPI 应用创建和配置。
    |
    | # 机器学习相关内容
    ├── data             - 本地持久化数据的位置
    │   ├── interim      - 已转换的中间数据。
    │   ├── processed    - 模型最终的、规范的数据集。
    │   └── raw          - 原始的、不可变的数据转储。
    │
    ├── notebooks        - Jupyter 笔记本。命名约定是一个数字（用于排序），
    |
    ├── ml               - 本项目使用的建模源代码。
    │   ├──__init__.py  - 使 ml 成为一个 Python 模块
    │   ├── pipeline.py  - 安排整个管道的脚本
    │   │
    │   ├── data         - 下载或生成数据的脚本
    │   │   └── make_dataset.py
    │   │
    │   ├── features     - 将原始数据转换为模型特征的脚本
    │   │   └── build_features.py
    │   │
    │   └── model        - 训练模型和进行预测的脚本
    │       ├── predict_model.py
    │       └── train_model.py
    │
    └── tests            - pytest
