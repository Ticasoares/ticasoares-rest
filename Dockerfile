FROM ubuntu:14.04
MAINTAINER Leticia Santiago

RUN apt-get update
RUN apt-get install python-webpy -y
ADD /restserver.py /opt/
RUN chmod 755 /opt/restserver.py 

EXPOSE 8080

CMD ["/opt/restserver.py"]
