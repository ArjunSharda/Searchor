FROM python:3

WORKDIR /usr/src/searchor

COPY requirements.txt ./

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --no-cache-dir --upgrade pip \
      && pip install --no-cache-dir searchor

COPY . .

WORKDIR /usr/src/searchor/examples

RUN python searchamazon.py
RUN python searchbing.py
RUN python searchduckduckgo.py
RUN python searchgoogle.py
RUN python searchyahoo.py
RUN python custom_engine.py