import os
import cv2
import pandas as pd

from SortImages import SortImages
from CroppedImages import CroppedImages

from ImageCropperCoord import ImageCropperCoord

class CroppedImagesTumor(CroppedImages):
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
    _Shape : int. Default is 224
            Resolution of the crop

    Attributes
    ----------
    _Malignant_label : int
        The label value for malignant images.

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
        _Shape : int
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
        _Dataframe : pandas.DataFrame
            The DataFrame containing information about the images, such as their names, severity, and coordinates.
        _Shape : int. Default is 224
            Resolution of the crop

        Returns
        -------
        None.

        """
        super().__init__(
            _Folder, 
            _Folder_store,
            _Resolution,
            _Dataframe,
            _Shape
        );

        # * Set the label value for malignant images
        self._Malignant_label = 1;
    
    def CropMIAS(self) -> None:
    
        # * Change the current working directory to the folder containing the images
        os.chdir(self._Folder);

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
            if (self._Dataframe.iloc[Index - 1, Severity] == self._Malignant_label):
                if(self._Dataframe.iloc[Index - 1, X_column] > 0  or self._Dataframe.iloc[Index - 1, Y_column] > 0):

                    try:
                    
                        print(f"Working with {Count} of {Total_images} {Format} Malignant images, {Filename} X: {self._Dataframe.iloc[Index - 1, X_column]} Y: {self._Dataframe.iloc[Index - 1, Y_column]}");
                        print(self._Dataframe.iloc[Index - 1, Name_column], " ------ ", Filename, " ✅");
                        Count += 1;

                        # * Reading the image
                        Path_file = os.path.join(self._Folder, File);
                        Image = cv2.imread(Path_file);
                        
                        # * Crop the image
                        Crop_image = ImageCropperCoord.crop_image(
                            self._Dataframe, 
                            Index,
                            Image, 
                            X_column,
                            Y_column,
                            self._Shape
                        );

                        New_name_filename = f"{Filename}_Malignant_cropped{Format}";

                        # * Print the dimensions of the original and cropped images for debugging purpose
                        print(Image.shape, " ----------> ", Crop_image.shape);

                        New_folder_store = os.path.join(self._Folder_store, New_name_filename);
                        cv2.imwrite(New_folder_store, Crop_image);

                    except OSError:
                        print("It must be a 'Malignant images', label: {}, X and Y must be postive, not: {}, {}❌".format(
                            self._Malignant_label, 
                            self._Dataframe.iloc[Index - 1, X_column],
                            self._Dataframe.iloc[Index - 1, Y_column])
                        ) #! Alert
            else:
                pass;
            
            Index += 1   