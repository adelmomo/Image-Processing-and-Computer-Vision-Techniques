import argparse
import cv2
import image_transformation
args_parser=argparse.ArgumentParser()
args_parser.add_argument("-i","--image",type=str,required=True,help="The path to an image")
args_parser.add_argument("transformation", type=str, choices=["histogram", "gaussian"],help="The transformation method to apply. Choose 'histogram' for Histogram Equalization or 'gaussian' for Gaussian Blurring.")
args_parser.add_argument("-ksize","--kernel_size", type=int, default=5, help="Kernel size for Gaussian Blurring (ignored for Histogram Equalization).")
args_parser.add_argument("-std","--standard_deviation", type=int, default=1, help="Standard deviation for Gaussian Blurring (ignored for Histogram Equalization).")
args_parser.add_argument("-o","--output",type=str,default="output.jpg",help="The output image path")
args=vars(args_parser.parse_args())

transform=image_transformation.ImageTransformation()
if args['transformation']=='histogram':
    output=transform.histogram_equalization(args['image'])
elif args['transformation']=='gaussian':
    output=transform.gaussian_blurring(args['image'],args['kernel_size'],args['standard_deviation'])
try:

    cv2.imwrite(args['output'],output)
    print(f'{args['output']} is saved successfully!')
except:
    print(f'Could not save {args['output']}')
