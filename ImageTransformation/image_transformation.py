import cv2
import numpy as np
from typing import Union

class ImageTransformation:
    def histogram_equalization(self, image : Union[str, np.ndarray]) -> np.ndarray:
        """
        The `histogram_equalization` function enhances an image by redistributing pixel intensities, resulting in a more uniform intensity distribution.

        Args:
            image (str): The path to the image to be processed.

        Returns:
            np.ndarray: The enhanced image with equalized histogram.
        """
        if isinstance(image,str):
            img = cv2.imread(image)
        else:
            img=image.copy()

        hist,_=np.histogram(img.flatten(),256,(0,256))
        cumsum=np.cumsum(hist)
        masked_cumsum=np.ma.masked_equal(cumsum,0)
        
        new_cumsum=np.round(255 * (masked_cumsum-masked_cumsum.min())/(masked_cumsum.max()-masked_cumsum.min()))
        new_cumsum=np.ma.filled(new_cumsum,0)
        
      
        img=new_cumsum[img]
        img=img.astype(np.uint8)
    
        return img
    
    def gaussian_blurring(self, image : Union[str, np.ndarray], ksize : int, sigma : int) -> np.ndarray:
        """
        The `gaussian_blurring` function enhances an image by removing noises in the given image (e.g., Gaussian Noise / White Noise), resulting in a smoother image.

        Args:
            image (str): The path to the image to be processed.
            ksize (int): The size of the filter (e.g., 3).
            sigma (ing): The standard deviation of the Gaussian kernel.
        Returns:
            np.ndarray: The smoothed version of the given image.
        """

        if ksize%2==0:
            raise ValueError(f"Kernel size should be an odd number")
        
        sigma=max(1,sigma)
        
        if isinstance(image,str):
            img=cv2.imread(image)
        else:
            img=image.copy()

        #creating the Gaussian kernel
        gaussian_kernel=np.zeros((ksize,ksize),dtype=np.float32)
        for i in range(ksize):
            for j in range(ksize):
                horizontal_distance=np.abs(i-ksize//2)**2
                vertical_distance=np.abs(j-ksize//2)**2
                gaussian_kernel[i,j]=np.exp(-(horizontal_distance+vertical_distance)/(2*sigma**2))
        
        #Making the Gaussian kernel 3D by replicating the kernel along the channels dimension
        gaussian_kernel=gaussian_kernel[...,np.newaxis]
        gaussian_kernel=np.repeat(gaussian_kernel,img.shape[-1],-1)

        #normalizing the Gaussian kernel
        gaussian_kernel=gaussian_kernel/np.sum(gaussian_kernel)
        

        '''convolving the Gaussian kernel with the image
        applying mirror padding to maintain the same size as the input image after convolution'''
        padded_img=np.pad(img,((ksize//2,ksize//2),(ksize//2,ksize//2),(0,0)),'reflect')
        output_img=np.zeros_like(padded_img)
        
        for i in range(ksize//2,padded_img.shape[0] - ksize//2):
            for j in range(ksize//2,padded_img.shape[1] - ksize//2):

                output_img[i,j]=np.sum(padded_img[i-ksize//2:i+ksize//2+1,j-ksize//2:j+ksize//2+1]*gaussian_kernel).astype(np.uint8)
        
        #unpadding
        output_img=output_img[ksize//2:output_img.shape[0]-ksize//2, ksize//2:output_img.shape[1]-ksize//2]
        return output_img
    
    def median_filter(self, image : Union[str, np.ndarray], ksize : int) -> np.ndarray:
        """
        The `median_filter` function enhances an image by removing noises in the given image (e.g., Salt & Pepper), resulting in a image without noises.

        Args:
            image (str): The path to the image to be processed.
            ksize (int): The size of the filter (e.g., 3).
        Returns:
            np.ndarray: An image without outliers (e.g., Salt & Pepper).
        """

        if ksize%2==0:
            raise ValueError(f"Kernel size should be an odd number")
        
        if isinstance(image,str):
            img=cv2.imread(image)
        else:
            img=image.copy()
            
        '''convolving the image with the median filter (subimage)
        applying mirror padding to maintain the same size as the input image after convolution'''
        padded_img=np.pad(img,((ksize//2,ksize//2),(ksize//2,ksize//2),(0,0)),'reflect')
        output_img=np.zeros_like(padded_img)

        for i in range(ksize//2,padded_img.shape[0] - ksize//2):
            for j in range(ksize//2,padded_img.shape[1] - ksize//2):
                subimage=padded_img[i-ksize//2:i+ksize//2+1,j-ksize//2:j+ksize//2+1].flatten()
                output_img[i,j]=np.sort(subimage)[len(subimage)//2]
        
        
        #unpadding
        output_img=output_img[ksize//2:output_img.shape[0]-ksize//2, ksize//2:output_img.shape[1]-ksize//2]
        return output_img