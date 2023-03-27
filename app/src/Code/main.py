
import os
from CroppedImagesNormalGrid import CroppedImagesNormalGrid
from CroppedImagesNormalRandom import CroppedImagesNormalRandom
from CroppedImagesTumor import CroppedImagesTumor
from CroppedImagesBenign import CroppedImagesBenign
from CroppedImagesMalignant import CroppedImagesMalignant

Resolution = 224;

def Test_crop_grid():
    
    global Resolution
    # * Create a new instance of the CroppedImagesNormal class
    CI = CroppedImagesNormalGrid(
        r'app\src\data\Mini_MIAS_PNG',
        r'app\src\data\Crop_Normal_Grid', Resolution, 
        r'app\src\data\Mini_MIAS_CSV_DATA.csv',              
    );
    
    # * Call the Crop method on the new instance
    CI.Crop();
    
    # * Check if the expected output is equal to the actual output
    assert os.path.exists(r'app\src\data\Crop_Normal_Grid') is True;

def Test_crop_random():

    global Resolution
    # * Create a new instance of the CroppedImagesNormal class
    CI = CroppedImagesNormalRandom(
        r'app\src\data\Mini_MIAS_PNG',
        r'app\src\data\Crop_Normal_Random', Resolution, 
        r'app\src\data\Mini_MIAS_CSV_DATA.csv',              
    );
    
    # * Call the Crop method on the new instance
    CI.Crop();
    
    # * Check if the expected output is equal to the actual output
    assert os.path.exists(r'app\src\data\Crop_Normal_Random') is True;

def Test_crop_tumor():

    global Resolution
    # * Create a new instance of the CroppedImagesNormal class
    CI = CroppedImagesTumor(
        r'app\src\data\Mini_MIAS_PNG',
        r'app\src\data\Crop_Tumor', Resolution, 
        r'app\src\data\Mini_MIAS_CSV_DATA.csv',              
    );
    
    # * Call the Crop method on the new instance
    CI.Crop();
    
    # * Check if the expected output is equal to the actual output
    assert os.path.exists(r'app\src\data\Crop_Tumor') is True;

def Test_crop_benign():

    global Resolution
    # * Create a new instance of the CroppedImagesNormal class
    CI = CroppedImagesBenign(
        r'app\src\data\Mini_MIAS_PNG',
        r'app\src\data\Crop_Benign', Resolution, 
        r'app\src\data\Mini_MIAS_CSV_DATA.csv',              
    );
    
    # * Call the Crop method on the new instance
    CI.Crop();
    
    # * Check if the expected output is equal to the actual output
    assert os.path.exists(r'app\src\data\Crop_Benign') is True;

def Test_crop_malignant():

    global Resolution
    # * Create a new instance of the CroppedImagesNormal class
    CI = CroppedImagesMalignant(
        r'app\src\data\Mini_MIAS_PNG',
        r'app\src\data\Crop_Malignant', Resolution, 
        r'app\src\data\Mini_MIAS_CSV_DATA.csv',              
    );
    
    # * Call the Crop method on the new instance
    CI.Crop();
    
    # * Check if the expected output is equal to the actual output
    assert os.path.exists(r'app\src\data\Crop_Malignant') is True;

# ? Create and display the menu
def main():
    Test_crop_grid();
    Test_crop_random();
    Test_crop_tumor();
    Test_crop_benign();
    Test_crop_malignant();

# ? If the script is being run directly, create and display the menu
if __name__ == "__main__":
    main();