import pandas as pd

from abc import ABC
from abc import abstractmethod

from Decorators.Timer import Timer

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

    @Timer.timer
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