FROM python:alpine

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip \
      && pip install --no-cache-dir searchor

WORKDIR /usr/src/searchor/examples
COPY examples .
RUN python searchamazon.py \
    && python searchbing.py \
    && python searchduckduckgo.py \
    && python searchgoogle.py \
    && python searchyahoo.py \
    && python custom_engine.py
