FROM python:3.9
WORKDIR /workdir
COPY . /workdir
RUN pip install pip --upgrade && \  
    pip install -r requirements.txt