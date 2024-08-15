import argparse
import cv2
import image_transformation
args_parser=argparse.ArgumentParser()
args_parser.add_argument("-i","--image",type=str,required=True,help="The path to an image")
args_parser.add_argument("-o","--output",type=str,default="output.jpg",help="The output image path")
args=vars(args_parser.parse_args())

transform=image_transformation.ImageTransformation()
output=transform.histogram_equalization(args['image'])
try:

    cv2.imwrite(args['output'],output)
    print(f'{args['output']} is saved successfully!')
except:
    print(f'Could not save {args['output']}')
