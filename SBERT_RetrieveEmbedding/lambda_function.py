
import json
import os

from sentence_transformers import SentenceTransformer


def lambda_handler(event, context):
    # getting text
    query = json.loads(event['body'])
    text = query['text']
    sbertmodel = query['sbertmodel']

    # loading SentenceBERT model
    model = SentenceTransformer(os.path.join('/', 'models', sbertmodel))
    embedding = model.encode([text])
    embedding = embedding[0]

    # return
    return {
        'statusCode': 200,
        # 'body': query,
        'embedding': json.dumps(list(embedding))
    }
