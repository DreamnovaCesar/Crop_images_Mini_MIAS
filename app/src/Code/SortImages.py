import os
from typing import Tuple

class SortImages(object):
    """
    A class for sorting images in a folder and displaying them.

    Parameters
    ----------
    Folder : str
        The path to the folder containing the images.

    Attributes
    ----------
    Folder : str
        The path to the folder containing the images.

    Methods
    -------
    sort_images(Folder_path: str) -> Tuple[list[str], int]:
        Sorts the images in the given folder and displays them.

    """

    # * Initializing (Constructor)
    def __init__(self, Folder : str) -> None:
        """
        Constructs an instance of SortImages class.

        Parameters
        ----------
        Folder : str
            The path to the folder containing the images.

        Returns
        -------
        None
        """
        self.Folder = Folder; 
    
    @staticmethod
    def sort_images(Folder_path: str) -> Tuple[list[str], int]: 
        """
        Sorts the images in the given folder and displays them.

        Parameters
        ----------
        Folder_path : str
            The path to the folder containing the images.

        Returns
        -------
        Tuple[list[str], int]
            A tuple containing the sorted list of image files and the number of images in the folder.
        """

        Asterisks : int = 60;

        # * This function sort the files and show them
        Number_images : int = len(os.listdir(Folder_path));
        print("\n");
        print("*" * Asterisks);
        print('Images: {}'.format(Number_images));
        print("*" * Asterisks);
        print("\n");

        # * Get the list of image files in the folder
        Files : list[str] = os.listdir(Folder_path);
        # * Sort the image files alphabetically
        Sorted_files : list[str] = sorted(Files);

        # * Print the sorted image files with their indices
        for Index, Sort_file in enumerate(Sorted_files):
            print('Index: {} ---------- {} ✅'.format(Index, Sort_file));

        print("\n")

        return Sorted_files, Number_images