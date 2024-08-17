import cv2
import numpy as np
from Utils import Utils
from typing import Union

class EdgeDetector:
    methods = {'Canny':{'threshold1':100,'threshold2':150},'Sobel':{'dx':1,'dy':1}}
    gaussian_kernel_size = 7
    gaussian_kernel_standard_deviation = 0.0

    def __init__(self,method:str, kernel_size:int = 3, preprocessing:bool = True):
        """
        EdgeDetector constructor.

        Args:
            method: the Edge Detection method to use [Canny | Sobel].
            kernel_size: The size of the filter convolving an image. This value should be an odd value (e.g., 3, 5, 7)
            preprocessing: Whether to perform preprocessing step before computing the edges. This is a very important step, as it reduces the noises inside an image
        """
        self.kernel_size=kernel_size
        if method not in self.methods:
            raise ValueError("Edge Detection method must be one of %r." % self.methods)
        
        self.method=method
        self.preprocessing=preprocessing

    def detect(self,image: Union[str, np.ndarray]) -> np.ndarray:
        """
        EdgeDetector detect function. This function computes the edges inside an image, using one of the methods [Canny | Sobel].

        Args:
            image: The given image.
        
        Returns:
            The detect function returns the edges inside the given image as np.ndarray.
        """
        if isinstance(image,str):
            img = Utils.read_image(image)
        else:
            img=image.copy()
        if img.shape[2] == 3:
            img = Utils.convert_rgb_to_gray(img)
        if self.preprocessing:
            img = cv2.GaussianBlur(img,ksize=(self.gaussian_kernel_size,self.gaussian_kernel_size),sigmaX=self.gaussian_kernel_standard_deviation)
        if self.method == 'Canny':
            edges=cv2.Canny(img,self.methods['Canny']['threshold1'],self.methods['Canny']['threshold2'])
        elif self.method == 'Sobel':
            horizontal_edges=cv2.Sobel(img,ddepth=cv2.CV_32F,dx=self.methods['Sobel']['dx'],dy=self.methods['Sobel']['dy'],ksize=self.kernel_size)
            vertical_edges=cv2.Sobel(img,cv2.CV_32F,dx=0,dy=1,ksize=self.kernel_size)
            
            #converting the values in horizontal_edges and vertical_edges to uint8 (0 - 255) by applying the absolute function on the values
            horizontal_edges=np.abs(horizontal_edges).astype(np.uint8)
            vertical_edges=np.abs(horizontal_edges).astype(np.uint8)
            
            #combining the horizontal and vertical edges
            edges=cv2.addWeighted(horizontal_edges,0.5,vertical_edges,0.5,0)
        
        return edges


            


