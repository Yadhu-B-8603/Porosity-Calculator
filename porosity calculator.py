#Importing the necessary libraries
import os
import cv2 as cv
import numpy as np

#Initialise the image directory
img_dir = "SAGITAL Z-Y"

#Finding the total number of images in the directory
n = len(os.listdir(img_dir))

# Iterate through all files in the specified folder
def total_pore_sum():
    total_dark_pixel_sum = 0
    for filename in os.listdir(img_dir):
        # Check if the file has a .bmp extension
        if filename.endswith(".bmp"):
            # Construct the full path to the image
            img_path = os.path.join(img_dir, filename)

            # Read the image
            img = cv.imread(img_path)
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # Finding the region of interest (ROI). Considering an ambient area of 50 pixels in the center.
            # This value will be optimized later.
            x1, x2, y1, y2 = 63, 263, 34, 784

            # Create a ROI rectangle in the image for representation purposes
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Crop the image to keep only the region defined by the rectangle
            cropped_img = img[y1:y2, x1:x2]

            # Apply thresholding to the cropped image
            _, thresholded_img = cv.threshold(cropped_img, 50, 255, cv.THRESH_BINARY)
            cv.imshow('img',thresholded_img)
            cv.waitKey(0)
            

            # Count the number of black pixels
            black_pixels = np.sum(thresholded_img == 0)

            total_dark_pixel_sum += black_pixels

    return total_dark_pixel_sum

# Calculate porosity for 200 pixels
perc_porosity = (total_pore_sum())/(n*150000)
print("% porosity for the 200 * 750 pixel section = ",perc_porosity*100,"%")