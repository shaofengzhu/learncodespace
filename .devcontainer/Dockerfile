FROM mcr.microsoft.com/vscode/devcontainers/python:3.8

COPY requirements-docker.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements-docker.txt \
   && rm -rf /tmp/pip-tmp
