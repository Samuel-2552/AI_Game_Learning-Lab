import cv2
import numpy as np

image = cv2.imread('Samuel.png')

height,width = image.shape[:2]

center = (width/2, height/2)

rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)

rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width,height))

M= np.float32 ([[1,0,50],[0,1,25]])
trans_image = cv2.warpAffine(image, M, (image.shape[1],image.shape[0]))

canny_image = cv2.Canny(image, 00 , 300)

#cv2.imshow("Original Image", image)
#cv2.imshow("Rotated Image", rotated_image)
#cv2.imshow("Translated Image", trans_image)
cv2.imshow("Translated Image", canny_image)

cv2.waitKey()


cv2.destroyAllWindows()
