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
    && python searchwikipedia.py \
    && python scrape.py \
    && python open_web.py \
    && python getinfo.py \
    && python copy_url.py \
    && python custom_engine.py
