import pandas as pd

from abc import ABC
from abc import abstractmethod

class CroppedImages(ABC):
    """Abstract class for cropping Mini-MIAS images.

    This class defines an abstract method for cropping Mini-MIAS images. Subclasses of this class should implement
    the CropMIAS method to handle the specific image cropping logic.

    Attributes
    ----------
    Folder : str
        The folder path where the downloaded images are.
    Folder_store : str
        The folder path to store the cropped images.
    Resolution : int
        The cropping resolution
    Dataframe : pd.DataFrame
        Dataframe that contains the cropping data for each image

    Methods
    -------
    CropMIAS() -> None:
        Abstract method for cropping Mini-MIAS images. This method will be called when cropping is enabled
        (it will crop images and save them to the specified folder).

    Notes
    -----
    This class is intended to be subclassed, and the CropMIAS method should be implemented by the subclass to handle
    the specific image cropping logic.

    This code defines an abstract base class called CroppedImages that is intended to be subclassed to implement specific image cropping logic for Mini-MIAS images. 
    The class has several attributes, including the folder path for the downloaded images, the folder path to store the cropped images, the cropping resolution, 
    and a Pandas DataFrame that contains the cropping data for each image.

    The class also defines an abstract method called Crop() that must be implemented by any subclass of CroppedImages. 
    This method handles the specific image cropping logic and is called when cropping is enabled, 
    cropping the Mini-MIAS images and saving them to the specified folder.

    The __init__ method initializes the attributes of the class by assigning the values passed as arguments to the corresponding attributes. 
    The pd.read_csv method is used to read the DataFrame from the file specified in the Dataframe attribute.

    The class is defined as an abstract class using the ABC module and the abstractmethod decorator is used to declare the Crop() 
    method as an abstract method that must be implemented by any subclass of CroppedImages. Any subclass of CroppedImages that does not implement 
    the abstract method Crop() will also be considered abstract and will not be allowed to be instantiated.

    Overall, this code provides a framework for implementing image cropping logic for Mini-MIAS images by defining a base class with necessary
    attributes and an abstract method that must be implemented by any subclass of the base class.

    """

    # * Initializing (Constructor)
    def __init__(
          self, 
          Folder : str,
          Folder_store : str,
          Resolution : int,
          Dataframe : pd.DataFrame,
        ) -> None:
       
      self._Folder = Folder;
      self._Folder_store = Folder_store;
      self._Resolution = Resolution;
      self._Dataframe = Dataframe;

      self._Dataframe = pd.read_csv(self._Dataframe)
    
    @abstractmethod
    def Crop(self) -> None:
      """
        Abstract method for cropping Mini-MIAS images.

        This method will be called when cropping is enabled (it will crop images and save them to the specified folder).

        Notes
        -----
        This method should be implemented by a subclass of CroppedImages to handle the specific image cropping logic.
        When called, this method should crop the Mini-MIAS images and save them to the specified folder.

        """
      pass