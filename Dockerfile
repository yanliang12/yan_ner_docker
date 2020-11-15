############Dockerfile###########
FROM openjdk:8

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN apt-get install -y tar

RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

RUN pip3 install stanza==1.1.1
RUN python3 -c "import stanza;stanza.download('en')"
RUN python3 -c "import stanza;stanza.download('ar')"

RUN echo "dsgnk"

RUN git clone https://github.com/yanliang12/yan_ner_docker.git
RUN mv yan_ner_docker/* ./

############Dockerfile###########
