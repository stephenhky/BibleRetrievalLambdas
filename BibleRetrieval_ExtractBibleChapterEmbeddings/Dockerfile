FROM anibali/pytorch

ADD . /code

WORKDIR /code

ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN sudo ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
RUN sudo apt-get update && \
  sudo apt-get install -y \
  tzdata \
  g++ \
  libc6 \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

RUN pip install -U pip
RUN pip install -U numpy
RUN pip install -U git+https://github.com/stephenhky/PyBibleNLP3
RUN pip install -r requirements.txt
RUN pip install awslambdaric boto3

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "lambda_function.lambda_handler" ]
