import cv2
import numpy as np

def no(x):
    pass

img = np.zeros((900,1000,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,no)
cv2.createTrackbar('G','image',0,255,no)
cv2.createTrackbar('B','image',0,255,no)



while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    

    
    img[:] = [b,g,r]

cv2.destroyAllWindows()