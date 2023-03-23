import matplotlib.pyplot as plt
import numpy as np

def crop_image(image, grid_size):
    h, w = image.shape[:2]
    crop_h, crop_w = h // grid_size, w // grid_size
    crops = []
    for i in range(grid_size):
        for j in range(grid_size):
            crop = image[i * crop_h:(i + 1) * crop_h, j * crop_w:(j + 1) * crop_w]
            crops.append(crop)
    return crops

# Load an example image
image = plt.imread(r"C:\Users\Cesar\Desktop\Images\Yo.png")

# Crop the image into a 3x3 grid
crops = crop_image(image, 10)

# Show the cropped images
fig, axs = plt.subplots(10, 10)
for i, ax in enumerate(axs.flatten()):
    ax.imshow(crops[i])
plt.show()