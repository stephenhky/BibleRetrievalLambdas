
from argparse import ArgumentParser

from sentence_transformers import SentenceTransformer


def get_argparser():
    argparser = ArgumentParser(description='Saving SentenceBERT model to a desginated path')
    argparser.add_argument('modelname', help='model name')
    argparser.add_argument('outputdir', help='output directory')
    return argparser


if __name__ == '__main__':
    args = get_argparser().parse_args()
    modelname = args.modelname
    outputdir = args.outputdir

    model = SentenceTransformer(modelname)
    model.save(outputdir)
