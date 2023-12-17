FROM python:3.11.7

ENV PYTHONUNBUFFERED 1

WORKDIR /ctbu/{{cookiecutter.project_slug}}

COPY poetry.lock pyproject.toml ./
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false 

ARG DEV=false
RUN if [ "$DEV" = "true" ] ; then poetry install --with dev ; else poetry install --only main ; fi

COPY ./app/ ./app/
COPY ./ml/model/ ./ml/model/

ENV PYTHONPATH "${PYTHONPATH}:/ctbu/{{cookiecutter.project_slug}}/app"

EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port 8080
