import cv2 as cv

# Function to display an image with a rectangle
def show_image_with_rectangle(img_path, x1, x2, y1, y2):
    # Read the image
    img = cv.imread(img_path)
    h,w,c = img.shape
    print(h," ",w)
    # Draw a rectangle on the image
    cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show the image with the rectangle
    cv.imshow("Image with Rectangle", img)
    _, thresholded_img = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
    cv.imshow('img',thresholded_img)
    cv.waitKey(0)

# Specify the path to the image
img_path = "SAGITAL Z-Y\h3_ir_rec_rs2_sag_voi__Scr_1379.bmp"

# Specify the pixel area for the rectangle (example values, replace with your desired values)
x1, x2, y1, y2 = 63, 263, 34, 784

# Display the image with the rectangle
show_image_with_rectangle(img_path, x1, x2, y1, y2)

# Close the OpenCV window
cv.destroyAllWindows()
