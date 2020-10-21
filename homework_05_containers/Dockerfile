# Чтобы запустить контейнер необходимо:
#docker build . -t itoys
#docker run -p=5000:5000 itoys
FROM python:3.8.6-buster

WORKDIR /app

#install and configure poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY itoys-project/pyproject.toml itoys-project/poetry.lock ./

RUN poetry install

COPY itoys-project .

CMD ["python", "main.py"]