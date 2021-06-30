
import logging
import json
import os

import boto3

from holymining.books.biblebooks import books2idx
from holymining.featurestore import BibleChapterH5FeatureStoreRetriever


s3_bucket = 'pybibles'
biblechap_h5configs = {
    ('NIV', 'stsb-roberta-base-v2'): 'feature-stores/NIV_stsb_roberta_base_v2.h5',
    ('NIV', 'allenai-specter'): 'feature-stores/NIV_allenai_specter.h5',
    ('NIV', 'nli-roberta-base-v2'): 'feature-stores/NIV_nli_roberta_base_v2.h5',
    ('NIV', 'quora-distilbert-base'): 'feature-stores/NIV_quora_distilbert_base.h5',
    ('ESV', 'stsb-roberta-base-v2'): 'feature-stores/ESV_stsb_roberta_base_v2.h5',
    ('ESV', 'allenai-specter'): 'feature-stores/ESV_allenai_specter.h5',
    ('ESV', 'nli-roberta-base-v2'): 'feature-stores/ESV_nli_roberta_base_v2.h5',
    ('ESV', 'quora-distilbert-base'): 'feature-stores/ESV_quora_distilbert_base.h5',
}


def lambda_handler(event, context):
    # getting query
    logging.info(event)
    logging.info(context)
    query = json.loads(event['body'])
    translation = query['translation']
    sbertmodel = query['sbertmodel']
    bookabbr = query['bookabbr']
    chapter = query['chapter']
    bookid = books2idx[bookabbr]

    # initialize S3 client
    featurestore_path = biblechap_h5configs[(translation, sbertmodel)]
    featurestore_basename = os.path.basename(featurestore_path)
    docker_featurestore_path = os.path.join('/', 'tmp', featurestore_basename)
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(s3_bucket, featurestore_path, docker_featurestore_path)

    # initialize object
    featurestore_retriever = BibleChapterH5FeatureStoreRetriever(docker_featurestore_path)
    embedding = featurestore_retriever.extract_embedding(bookid, chapter)

    # return
    return {
        'statusCode': 200,
        # 'body': query,
        'embedding': embedding
    }