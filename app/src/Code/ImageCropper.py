
from abc import ABC
from abc import abstractmethod

class ImageCropper(ABC):
    """
    Abstract base class for cropping an input image into a list of smaller images.
    """

    @abstractmethod
    def crop_image():
        """
        Crop an input image into a list of smaller images.
        """
        pass;