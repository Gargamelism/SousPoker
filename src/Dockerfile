# base image
FROM python:3.11.2-slim-bullseye

# env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# work directory
WORKDIR /app
RUN pwd
# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project files
COPY . .

ENTRYPOINT [ "/app/entrypoint.sh" ]