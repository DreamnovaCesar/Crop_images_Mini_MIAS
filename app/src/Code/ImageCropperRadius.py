import numpy as np
import pandas as pd

from ImageCropper import ImageCropper

class ImageCropperCoord(ImageCropper):
    """
    A class for cropping an input image into a smaller image using coordinate values.

    Methods
    -------
    crop_image(
        Dataframe : pd.DataFrame, 
        Index : int, 
        Image : np.ndarray, 
        X_column : int,
        Y_column : int,
        Shape : int
    ) -> numpy.ndarray:

        Crop an input image into a grid of smaller images.
    """

    @staticmethod
    def crop_image(
        Dataframe : pd.DataFrame, 
        Index : int,
        Image : np.ndarray, 
        X_column : int,
        Y_column : int,
        Radius : int
    ) -> np.ndarray:
        """
        Crop an input image into a smaller image using coordinate values.

        Parameters
        ----------
        Dataframe : pd.DataFrame
            A pandas DataFrame containing the coordinate values of each image to be cropped.
        Index : int
            The index of the image to be cropped.
        Image : np.ndarray
            The input image to be cropped.
        X_column : int
            The index of the column in Dataframe that contains the x-coordinate value of the image.
        Y_column : int
            The index of the column in Dataframe that contains the y-coordinate value of the image.
        Radius : int
            The desired Radius of the cropped image. The cropped image will be of size (Radius, Radius).

        Returns
        -------
        np.ndarray
            The cropped image(s).

        Raises
        ------
        ValueError
            If the input image is not a NumPy array.

        Examples
        --------
        >>> import numpy as np
        >>> import pandas as pd
        >>> from ImageCropperCoord import ImageCropperCoord

        >>> # create a sample DataFrame with coordinate values
        >>> data = {'x': [10, 20, 30], 'y': [20, 30, 40]}
        >>> df = pd.DataFrame(data)

        >>> # load an input image to be cropped
        >>> img = np.zeros((100, 100))

        >>> # create an instance of the ImageCropperCoord class
        >>> cropper = ImageCropperCoord(df, 1, img, 0, 1, 50)

        >>> # crop the image
        >>> cropped_img = cropper.crop_image()

        """

        # * Validate the input parameters
        if(not isinstance(Image, np.ndarray)):
            raise ValueError("Input image must be a NumPy array.");
    
        # * Obtaining the center using the radius
        Image_center = (Dataframe.iloc[Index - 1, Radius] / 2)

        # * Obtaining dimension
        Height_Y = Image.shape[0];

        # * Extract the value of X and Y of each image
        X_size = Dataframe.iloc[Index - 1, X_column];
        Y_size = Dataframe.iloc[Index - 1, Y_column];

        # * Extract the value of X and Y of each image
        XDL = X_size - Image_center;
        XDM = X_size + Image_center;

        # * Extract the value of X and Y of each image
        YDL = Height_Y - Y_size - Image_center;
        YDM = Height_Y - Y_size + Image_center;

        # * Cropped image
        Cropped_Image = Image[int(YDL):int(YDM), int(XDL):int(XDM)];
        
        return Cropped_Image