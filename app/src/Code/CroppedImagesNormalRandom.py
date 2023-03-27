import os
import cv2
import pandas as pd

from SortImages import SortImages
from CroppedImages import CroppedImages

from ImageCropperRandomly import ImageCropperRandomly
from ImageViewer import ImageViewer

class CroppedImagesNormalRandom(CroppedImages):
    """
    A class that crops images from a specific folder based on the provided DataFrame.

    Parameters
    ----------
    _Folder : str
        The path of the folder containing the original images to be cropped.
    _Folder_store : str
        The path of the folder where the cropped images will be stored.
    _Resolution : int
        The desired resolution of the cropped images.
    _Dataframe : pandas.DataFrame
        The DataFrame containing information about the images, such as their names, severity, and coordinates.

    Attributes
    ----------
    _Normal_images_grid : int
        The number of images to crop in a grid for normal images.
    _Normal_label : int
        The label value for normal images.

    Methods
    -------
    CropMIAS()
        Crops the images based on the provided DataFrame.

    """

    # * Initializing (Constructor)
    def __init__(self, 
        _Folder : str, 
        _Folder_store : str,
        _Resolution : int,
        _Dataframe : pd.DataFrame,
    ) -> None:
        """
        Initializes the CroppedImages object.

        Parameters
        ----------
        _Folder : str
            The path of the folder containing the original images to be cropped.
        _Folder_store : str
            The path of the folder where the cropped images will be stored.
        _Resolution : int
            The desired resolution of the cropped images.
        _Dataframe : pd.DataFrame
            The DataFrame containing information about the images, such as their names, severity, and coordinates.

        Returns
        -------
        None.

        """
        super().__init__(
            _Folder, 
            _Folder_store,
            _Resolution,
            _Dataframe,
        );

        # * Set the default number of images to crop in a grid for normal images
        self._Normal_images_grid = 4;

        # * Set the label value for normal images
        self._Normal_label = 2;
    
    def Crop(self) -> None:
        """
        Crops the images based on the provided DataFrame.

        Returns
        -------
        None.

        """

        # * Create a string of asterisks for formatting purposes
        Asterisks : int = 100;

        # ? Set the column numbers for the DataFrame

        # * Column 0 from the DataFrame (Name of the image, ID)
        Name_column : int = 0;
        # * Column 3 from the DataFrame (Severity of the Image)
        Severity : int = 3;
        # * Column 4 from the DataFrame (X value)
        X_column : int = 4;
        # * Column 5 from the DataFrame (Y value)
        Y_column : int = 5;

        # * Initial index
        Index : int = 1;
        
        # * Using sort function
        Sorted_files, Total_images = SortImages.sort_images(self._Folder);
        Count : int = 1;

        # * Iterate through the sorted images
        for File in Sorted_files:

            # * Get the filename and format of the image
            Filename, Format = os.path.splitext(File);

            # * Print the image name and filename for debugging purposes
            print("*" * Asterisks);
            print(self._Dataframe.iloc[Index - 1, Name_column]);
            print(Filename);
            print("*" * Asterisks);
            
            # * Check if the image is normal and has invalid coordinates
            if(self._Dataframe.iloc[Index - 1, Severity] == self._Normal_label):
                if(self._Dataframe.iloc[Index - 1, X_column] == 0  or self._Dataframe.iloc[Index - 1, Y_column] == 0):

                    try:

                        print(f"Working with {Count} of {Total_images} {Format} Normal images, {Filename}");
                        print(self._Dataframe.iloc[Index - 1, Name_column], " ------ ", Filename, " ✅");
                        Count += 1;

                        # * Read the image
                        Path_file = os.path.join(self._Folder, File);
                        Image = cv2.imread(Path_file);

                        # * Crop the image
                        Crops = ImageCropperRandomly.crop_image(Image, self._Resolution, 20);
                        #ImageViewer.show_cropped_images(Crops, self._Normal_images_grid)
                        
                        # * Save each crop as a new image
                        for i in range(len(Crops)):

                            New_name_filename = f"{Filename}_Normal_cropped_{i} {Format}";

                            # * Print the dimensions of the original and cropped images for debugging purposes
                            print(Image.shape, " ----------> ", Crops[i].shape);

                            New_folder_store = os.path.join(self._Folder_store, New_name_filename);
                            cv2.imwrite(New_folder_store, Crops[i]);

                    except OSError:
                        print("It must be a 'Normal images', label: {}, X and Y must be postive, not: {}, {}❌".format(
                            self._Normal_label, 
                            self._Dataframe.iloc[Index - 1, X_column],
                            self._Dataframe.iloc[Index - 1, Y_column])
                        ) #! Alert
            else:
                pass ; 

            Index += 1   