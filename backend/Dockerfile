FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY poetry.lock pyproject.toml /app
COPY backend/ /app/
RUN pip3 install poetry
RUN poetry install