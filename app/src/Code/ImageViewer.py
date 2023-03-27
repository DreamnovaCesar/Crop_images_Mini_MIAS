import numpy as np
import matplotlib.pyplot as plt

from typing import List

class ImageViewer(object):
    """
    A class for displaying a grid of cropped images.
    """

    @staticmethod
    def show_cropped_images(
        Crops : List[np.ndarray],
        Grid_size : int
    ): 
        """
        Displays a grid of cropped images.

        Parameters:
        -----------
        Crops : list of numpy.ndarray
            The list of cropped images to display.
        Grid_size : int
            The number of rows/columns in the grid of images to display.

        Raises:
        -------
        ValueError
            If Crops is not a list of NumPy arrays or if Grid_size is not a positive integer.
        
        Returns:
        --------
        None
        """

        # * Validate the input parameters
        if(not isinstance(Crops, list) or not all(isinstance(c, np.ndarray) for c in Crops)):
            raise ValueError("Crops must be a list of NumPy arrays.");
        
        if(not isinstance(Grid_size, int) or Grid_size <= 0):
            raise ValueError("Grid size must be a positive integer.");
        
        # * Display the cropped images as a grid
        fig, axs = plt.subplots(Grid_size, Grid_size);
        for i, ax in enumerate(axs.flatten()):
            ax.imshow(Crops[i]);
        
        #plt.show();
        plt.close();