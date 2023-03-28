
import os
import cv2

from ImageCropperGrid import ImageCropperGrid
from ImageViewer import ImageViewer


def Test_crop_grid() -> None:
    
    Grid : int = 4
    Image = cv2.imread(r'app\src\data\Mini_MIAS_PNG\mdb001.png');

    # * Crop the image (256 x 4 = 1024)
    Crops = ImageCropperGrid.crop_image(Image, Grid);
    ImageViewer.show_cropped_images(Crops, Grid)
    
# ? Create and display the menu
def main():
    Test_crop_grid();

# ? If the script is being run directly, create and display the menu
if __name__ == "__main__":
    main();