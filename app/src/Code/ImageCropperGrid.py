import numpy as np

from typing import List
from ImageCropper import ImageCropper

class ImageCropperGrid(ImageCropper):
    """
    A class for cropping an input image into a grid of smaller images.

    Methods
    -------
    crop_image(Image: numpy.ndarray, Grid_size: int) -> List[numpy.ndarray]:
        Crop an input image into a grid of smaller images.
    
    """

    def crop_image(
        Image : np.ndarray, 
        Grid_size : int
    ) -> List[np.ndarray]:
        
        """
        Crop an input image into a grid of smaller images.

        Parameters
        ----------
        Image : numpy.ndarray
            The input image as a NumPy array.
        
        Grid_size : int
            The number of rows and columns in the grid.

        Returns
        -------
        list of numpy.ndarray
            A list of cropped images as NumPy arrays.

        Raises
        ------
        ValueError
            If the input image is not a valid NumPy array or the grid size is not a positive integer.

        Examples
        --------
        >>> image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> crops = ImageCropper.crop_image(image, 2)
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
        
        if(not isinstance(Grid_size, int) or Grid_size <= 0):
            raise ValueError("Grid size must be a positive integer.");
        
        # * Initialize an empty list to store the cropped images
        Crops = [];

        # * Get the height and width of the input image
        H, W = Image.shape[:2];

        # * Calculate the height and width of each crop
        Crop_H = H // Grid_size;
        Crop_W = W // Grid_size;

        # * Loop over each row and column of the grid
        for i in range(Grid_size):
            for j in range(Grid_size):

                # * Extract the crop at the current row and column
                Crop = Image[i * Crop_H:(i + 1) * Crop_H, 
                             j * Crop_W:(j + 1) * Crop_W];
                
                Crops.append(Crop);

        return Crops