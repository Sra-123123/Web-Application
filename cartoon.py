import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\M V PRASAD\OneDrive\Attachments\Documents\dog.jpg")
img = cv2.resize(img, (400,400))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
gray_blur = cv2.medianBlur(gray, 5)
# Create edge mask using adaptive thresholding
edges = cv2.adaptiveThreshold(gray_blur, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth color regions
color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)

# Combine edges with smoothed image
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Show all images
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)

cv2.destroyAllWindows();
