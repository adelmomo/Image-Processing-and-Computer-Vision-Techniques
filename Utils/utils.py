import numpy as np
import cv2

class Utils:
    
    @staticmethod
    def count_non_zeros_pixels(img : np.ndarray) -> int:
        """
        Counts the number of non-zero pixels in a given image.

        Args:
            img (np.ndarray): The image array in which to count non-zero pixels.

        Returns:
            int: The count of non-zero pixels.
        """
        count = np.count_nonzero(img)
        return count
    
    @staticmethod
    def create_video_capture(capture_id : int) -> cv2.VideoCapture:
        """
        Creates a video capture object for a given device or video file.

        Args:
            capture_id (int): Device index for camera input or path to video file.

        Returns:
            cv2.VideoCapture: Video capture object.

        Raises:
            ValueError: If the video capture could not be opened.
        """
        cap = cv2.VideoCapture(capture_id)
        if not cap.isOpened():
            raise ValueError(f'Failed to open video capture with ID: {capture_id}')
        return cap
    
    @staticmethod
    def read_image(img_path : str) -> np.ndarray:
        """
        Reads an image from the specified file path.

        Args:
            img_path (str): Path to the image file.

        Returns:
            np.ndarray: The image as a NumPy array.

        Raises:
            ValueError: If the image is not found at the specified path.
        """
        img = cv2.imread(img_path)
        if img is None:
            raise ValueError(f'The image is not found in the path provided: {img_path}')
        return img
    
    @staticmethod
    def convert_rgb_to_gray(img: np.ndarray) -> np.ndarray:
        """
        Converts an RGB image to grayscale.

        Args:
            img (np.ndarray): The RGB image to be converted. Should have shape (H, W, 3).

        Returns:
            np.ndarray: The resulting grayscale image with shape (H, W).

        Raises:
            ValueError: If the input image is not a 3-channel RGB image.
        """
        if img.ndim != 3 or img.shape[2] != 3:
            raise ValueError('Input image must be an RGB image with 3 channels.')
        
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return gray_img
    
    @staticmethod
    def write_string_to_frame(frame: np.ndarray, text: str, position: tuple = (50, 50),
                          font_scale: float = 1.0, color: tuple = (255, 255, 255), thickness: int = 2) -> np.ndarray:
        """
        Writes a string onto a given frame with specified font size and color.

        Args:
            frame (np.ndarray): The image/frame where the text will be written.
            text (str): The string to write on the frame.
            position (tuple): The (x, y) coordinates for the bottom-left corner of the text.
            font_scale (float): Font scale factor that is multiplied by the base font size.
            color (tuple): The color of the text in BGR format (default is white).
            thickness (int): Thickness of the text strokes.

        Returns:
            np.ndarray: The frame with the string written on it.
        """
        # Choose the font
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Write the text on the frame
        cv2.putText(frame, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    
        return frame