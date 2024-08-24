import argparse
from segmentation import Segmentation
import cv2

args_parser=argparse.ArgumentParser()
args_parser.add_argument("-i","--image",type=str,required=True,help="The path to an image")
args_parser.add_argument("-k","--clusters",type=int,default=10,help="The number of clusters")
args_parser.add_argument("-n","--iterations",type=str,default=20,help="The number of iterations")
args_parser.add_argument("-o","--output",type=str,default="output.jpg",help="The output image path")
args=vars(args_parser.parse_args())

segmentation=Segmentation(args['clusters'],args['iterations'])
output=segmentation.predict(args['image'])
try:

    cv2.imwrite(args['output'],output)
    print(f'{args['output']} is saved successfully!')
except:
    print(f'Could not save {args['output']}')