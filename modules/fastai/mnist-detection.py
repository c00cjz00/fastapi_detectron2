import warnings
warnings.filterwarnings("ignore")
import argparse
#import fastai
#fastai.device = torch.device('cpu')
from fastai.vision.all import *
def get_parser():
    parser = argparse.ArgumentParser(description="fastai demo for builtin configs")
    parser.add_argument(
        "--model",
        help="A list of space separated input images; "
        "or a single glob pattern such as 'directory/*.jpg'",
    )
    parser.add_argument(
        "--input",
        help="input images; "
        "or a single glob pattern such as 'directory/*.jpg'",
    )
    parser.add_argument(
        "--output",
        help="output text; "
        "or a single glob pattern such as 'directory/*.text'",
    )
    return parser
args = get_parser().parse_args()
if args.input:
    model = (args.model)
    inputImg = (args.input)
    outputTEXT = (args.output)
    learn=load_learner(model)
    result = (learn.predict(inputImg))
    prediction = str.strip(result[0])
    f = open(outputTEXT, "w")
    f.write(prediction)
    f.close()