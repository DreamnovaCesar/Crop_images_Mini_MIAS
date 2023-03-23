import os
import cv2
import pandas as pd

from CroppedImages import CroppedImages
from SortImages import SortImages

class CroppedImages(CroppedImages):


    # * Initializing (Constructor)
    def __init__(self, 
        _Folder : str, 
        _Folder_store : str,
        _Resolution : int,
        _Dataframe : pd.DataFrame
    ) -> None:

        super().__init__(
            _Folder, 
            _Folder_store,
            _Resolution,
            _Dataframe
        );

        self._Normal_label = 2;
    
    def CropMIAS(self) -> None:
        
        
        os.chdir(self._Folder)

        Asterisks : int = 100;

        # * Column 0 from the DataFrame (Name of the image, ID)
        Name_column : int = 0

        # * Column 3 from the DataFrame (Severity of the Image)
        Severity : int = 3

        # * Column 4 from the DataFrame (X value)
        X_column : int = 4

        # * Column 5 from the DataFrame (Y value)
        Y_column : int = 5

        # * Initial index
        Index : int = 1
        
        # * Using sort function
        Sorted_files, Total_images = SortImages.sort_images(self._Folder)
        Count : int = 1

        # * Reading the files
        for File in Sorted_files:
        
            Filename, Format = os.path.splitext(File)

            print("*" * Asterisks);
            print(self._Dataframe.iloc[Index - 1, Name_column])
            print(Filename)
            print("*" * Asterisks);
            
            if(self._Dataframe.iloc[Index - 1, Severity] == self._Normal_label):
                if(self._Dataframe.iloc[Index - 1, X_column] == 0  or self._Dataframe.iloc[Index - 1, Y_column] == 0):

                    try:

                        print(f"Working with {Count} of {Total_images} {Format} Normal images, {Filename}")
                        print(self._Dataframe.iloc[Index - 1, Name_column], " ------ ", Filename, " ✅")
                        Count += 1

                        Path_file = os.path.join(self._Folder, File)
                        Image = cv2.imread(Path_file)

                        Distance = self._Shapes # Perimetro de X y Y de la imagen.
                        Image_center = Distance / 2 # Centro de la imagen.
                        #CD = self.df.iloc[Index - 1, Radius] / 2
                        # * Obtaining dimension
                        Height_Y = Image.shape[0] 
                        print(Image.shape[0])

                        # * Extract the value of X and Y of each image
                        X_size = self._X_mean
                        Y_size = self._Y_mean
                            
                        # * Extract the value of X and Y of each image
                        XDL = X_size - Image_center
                        XDM = X_size + Image_center
                            
                        # * Extract the value of X and Y of each image
                        YDL = Height_Y - Y_size - Image_center
                        YDM = Height_Y - Y_size + Image_center

                        # * Cropped image
                        Cropped_Image_Normal = Image[int(YDL):int(YDM), int(XDL):int(XDM)]

                        # * Comparison two images
                        print(Image.shape, " ----------> ", Cropped_Image_Normal.shape)

                        # print(Cropped_Image_Normal.shape)
                        # Display cropped image
                        # cv2_imshow(cropped_image)
                    
                        New_name_filename = Filename + '_Normal_cropped' + Format

                        New_folder = os.path.join(self.__Normalfolder, New_name_filename)
                        cv2.imwrite(New_folder, Cropped_Image_Normal)

                        #Images.append(Cropped_Image_Normal)

                    except OSError:
                        print('Cannot convert %s' % File)

            Index += 1   