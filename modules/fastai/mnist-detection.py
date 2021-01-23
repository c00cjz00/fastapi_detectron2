#import warnings
#warnings.filterwarnings("ignore")
import argparse
import fastai
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
        help="A list of space separated input images; "
        "or a single glob pattern such as 'directory/*.jpg'",
    )
    parser.add_argument(
        "--output",
        help="A file or directory to save output visualizations. "
        "If not given, will show output in an OpenCV window.",
    )
    return parser

args = get_parser().parse_args()
if args.input:
    model = (args.model)
    inputImg = (args.input)
    outputImg = (args.output)
    fastai.device = torch.device('cpu')
    learn=load_learner(model)
    file = '2032.png'
    prediction= (learn.predict(file))
    print(prediction)