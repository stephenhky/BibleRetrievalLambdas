
import logging
import json

import boto3

from holymining.books.biblebooks import books2idx
from holymining.featurestore import BibleChapterH5FeatureStoreRetriever


biblechap_h5configs = {
    ('NIV', 'stsb-roberta-base-v2'): 's3://pybibles/feature-stores/NIV_stsb_roberta_base_v2.h5',
    ('NIV', 'allenai-specter'): 's3://pybibles/feature-stores/NIV_allenai_specter.h5',
    ('NIV', 'nli-roberta-base-v2'): 's3://pybibles/feature-stores/NIV_nli_roberta_base_v2.h5',
    ('NIV', 'quora-distilbert-base'): 's3://pybibles/feature-stores/NIV_quora_distilbert_base.h5',
    ('ESV', 'stsb-roberta-base-v2'): 's3://pybibles/feature-stores/ESV_stsb_roberta_base_v2.h5',
    ('ESV', 'allenai-specter'): 's3://pybibles/feature-stores/ESV_allenai_specter.h5',
    ('ESV', 'nli-roberta-base-v2'): 's3://pybibles/feature-stores/ESV_nli_roberta_base_v2.h5',
    ('ESV', 'quora-distilbert-base'): 's3://pybibles/feature-stores/ESV_quora_distilbert_base.h5',
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

    # initialize S3 client
    s3_client = boto3.client('s3')
    # TODO: download file