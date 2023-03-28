import random
import numpy as np

from typing import List
from ImageCropper import ImageCropper

class ImageCropperRandomly(ImageCropper):
    """
    A class for cropping an input image into smaller images randomly.

    Methods
    -------
    crop_image(Image: numpy.ndarray, Crop_size : int, Num_crops : int = 5) -> List[numpy.ndarray]:
        Crop an input image into smaller images randomly.
    
    """

    @staticmethod
    def crop_image(
        Image : np.ndarray, 
        Crop_size : int,
        Num_crops : int = 5
    ) -> List[np.ndarray]:
        
        """
        Crop an input image into a list of smaller images.

        Parameters
        ----------
        Image : numpy.ndarray
            The input image as a NumPy array.

        Crop_size : int
            The size of each cropped image.

        Num_crops : int, optional
            The number of crops to generate. Default is 5.

        Returns
        -------
        List of numpy.ndarray
            A list of cropped images as NumPy arrays.

        Raises
        ------
        ValueError
            If the input image is not a valid NumPy array or Crop_size/Num_crops are not positive integers.

        Examples
        --------
        >>> image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> crops = ImageCropperRandomly.crop_image(image, 2)
        >>> print(crops)
        [array([[1, 2],
                [4, 5]]),
        array([[3],
                [6]]),
        array([[7, 8],
                [1, 2]]),
        array([[9],
                [4]]),
        array([[5, 6],
                [8, 9]]),
        array([[7],
                [2]])]

        """

        # * Validate the input parameters
        if(not isinstance(Image, np.ndarray)):
            raise ValueError("Input image must be a NumPy array.");
        
        if(not isinstance(Crop_size, int) or Crop_size <= 0):
            raise ValueError("Crop size must be a positive integer.");
        
        if(not isinstance(Num_crops, int) or Num_crops <= 0):
            raise ValueError("Num_crops must be a positive integer.");
    
        # * Initialize an empty list to store the cropped images
        Crops = [];

        # * Get the height and width of the input image
        H, W = Image.shape[:2];

        for _ in range(Num_crops):

            i = random.randint(0, H - Crop_size);
            j = random.randint(0, W - Crop_size);

            Crop = Image[i : i + Crop_size, 
                         j : j + Crop_size];
            
            Crops.append(Crop);

        return Crops