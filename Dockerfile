FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ARG APP_HOME=/DRF_CRUD
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install \
#  $(test "${DEBUG}" = 0 && echo "--no-dev")
  --no-interaction --no-ansi