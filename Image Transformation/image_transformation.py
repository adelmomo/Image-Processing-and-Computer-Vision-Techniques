import cv2
import numpy as np

class ImageTransformation:
    def histogram_equalization(self, image : str) -> np.ndarray:
        """
        The `histogram_equalization` function enhances an image by redistributing pixel intensities, resulting in a more uniform intensity distribution.

        Args:
            image (np.ndarray): The input image to be processed.

        Returns:
            np.ndarray: The enhanced image with equalized histogram.
        """

        img = cv2.imread(image)

        hist,_=np.histogram(img.flatten(),256,(0,256))
        cumsum=np.cumsum(hist)
        masked_cumsum=np.ma.masked_equal(cumsum,0)
        
        new_cumsum=np.round(255 * (masked_cumsum-masked_cumsum.min())/(img.shape[0]*img.shape[1]-masked_cumsum.min()))
        new_cumsum=np.ma.filled(new_cumsum,0).astype(np.uint8)
        
      
        img=new_cumsum[img]
    
        return img
        