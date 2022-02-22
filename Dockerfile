RUN apt update && apt upgrade -y

COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Grade12
WORKDIR /Grade12
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
