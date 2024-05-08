import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('./ShanghaiTech_Logo_RGBA.png', cv2.IMREAD_UNCHANGED)
    print(img.shape)
    # Remove Edge Pixel's Color And Alpha
    # Set Color To White
    img[:, :, 0:3] = 255
    cv2.imwrite('./ShanghaiTech_Logo_RGBA_1.png', img)