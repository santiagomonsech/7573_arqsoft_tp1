FROM python:3.6
RUN mkdir /opt/app
WORKDIR /opt/app
COPY . ./
RUN pip install -r requirements.txt
CMD bash docker_entrypoint.sh
