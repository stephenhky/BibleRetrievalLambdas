FROM anibali/pytorch

ADD . /code

WORKDIR /code
ADD . /models

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

RUN python save_sbert_model.py allenai-specter models/allenai-specter
RUN python save_sbert_model.py nli-roberta-base-v2 models/nli-roberta-base-v2
RUN python save_sbert_model.py quora-distilbert-base models/quora-distilbert-base
RUN python save_sbert_model.py stsb-roberta-base-v2 models/stsb-roberta-base-v2

ENTRYPOINT [ "python", "-m", "awslambdaric" ]
CMD [ "lambda_function.lambda_handler" ]
