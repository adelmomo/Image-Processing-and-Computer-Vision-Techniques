import numpy as np
import cv2

class Segmentation:

    def __init__(self, k: int = 10, iterations: int = 20):
        """
        Initializes the Segmentation class with specified parameters.

        Args:
            k (int): The number of clusters for k-means segmentation. Default is 10.
            iterations (int): The number of iterations for the k-means algorithm. Default is 20.
        """
        self.k=k
        self.iterations=iterations

    def predict(self, image : str) -> np.ndarray:
        """
        Segments the input image using k-means clustering.

        Args:
            image (str): The file path to the image to be segmented.

        Returns:
            np.ndarray: The segmented image with the same dimensions as the input, 
                        but with pixels assigned to their respective cluster colors.
        """
        img=cv2.imread(image)
        flattened_img=np.reshape(img,(-1,3))
        clusters=flattened_img[np.random.choice(len(flattened_img),self.k)].astype(np.float32)
    
        for _ in range(self.iterations):
            
            cost=np.zeros((len(flattened_img),self.k),dtype=np.float32)
            for i in range(self.k):
                cost[:,i]=np.sum(np.abs(clusters[i]-flattened_img),axis=-1)
            
            candidates=np.argmin(cost,axis=-1)
            for i in range(self.k):
                clusters[i]=np.mean(flattened_img[candidates==i],axis=0)
        
        flattened_img=clusters[candidates]
        segmented_img=np.reshape(flattened_img,(img.shape[0],img.shape[1],3)).astype(np.uint8)
        return segmented_img