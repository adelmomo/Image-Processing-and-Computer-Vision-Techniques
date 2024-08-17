import argparse
import cv2
import edge_detector
args_parser=argparse.ArgumentParser()
args_parser.add_argument("-i","--image",type=str,required=True,help="The path to an image")
args_parser.add_argument("-m","--method_type",type=str,default="Canny",help="The Edge Detection method to use")
args_parser.add_argument("-o","--output",type=str,default="output.jpg",help="The output image path")
args=vars(args_parser.parse_args())

edge_detector=edge_detector.EdgeDetector(args['method_type'])
output=edge_detector.detect(args['image'])
try:

    cv2.imwrite(args['output'],output)
    print(f'{args['output']} is saved successfully!')
except:
    print(f'Could not save {args['output']}')

    
