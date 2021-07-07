
import os
import tarfile
from argparse import ArgumentParser

from sentence_transformers import SentenceTransformer


# reference: https://colab.research.google.com/drive/1eyVi8tkCr7N-sE-yyhDB_lduowp1EZ78?usp=sharing#scrollTo=IgBWFbGK0h9T
def pack_model(model_path, tar_file_name):
    root, dirs, files = list(os.walk(model_path))[0]
    with tarfile.open(tar_file_name, 'w:gz') as f:
        for file in files:
            f.add(f'{model_path}/{file}', arcname=file)
        for dir in dirs:
            f.add(f'{model_path}/{dir}', arcname=dir)


def get_argparser():
    argparser = ArgumentParser(description='Saving SentenceBERT model to a desginated path')
    argparser.add_argument('modelname', help='model name')
    argparser.add_argument('outputname', help='output name')
    argparser.add_argument('--pack', default=False, action='store_true', help='pack model (default: False)')
    return argparser


if __name__ == '__main__':
    args = get_argparser().parse_args()
    modelname = args.modelname
    outputname = args.outputname
    topack = args.pack

    model = SentenceTransformer(modelname)
    model.save(outputname)
    pack_model(outputname, outputname+'.tar.gz')
