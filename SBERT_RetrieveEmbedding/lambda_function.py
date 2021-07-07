
import json
import os
import tarfile

import boto3
from sentence_transformers import SentenceTransformer


s3_bucket = 'huggingfacesentencebert'


def lambda_handler(event, context):
    # getting text
    query = json.loads(event['body'])
    text = query['text']
    sbertmodel = query['sbertmodel']

    # copying models from s3
    docker_model_path = os.path.join('/', 'tmp', sbertmodel)
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(s3_bucket, sbertmodel+'.tar.gz', docker_model_path+'.tar.gz')
    model_tar = tarfile.open(docker_model_path+'.tar.gz')
    model_tar.extractall(os.path.join('/', 'tmp'))

    # loading SentenceBERT model
    model = SentenceTransformer(docker_model_path)
    embedding = model.encode([text])
    embedding = embedding[0]c

    # return
    return {
        'statusCode': 200,
        # 'body': query,
        'embedding': json.dumps(list(embedding))
    }
