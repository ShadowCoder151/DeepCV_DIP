import cv2
import numpy as np

def convert_grayscale(input_img: cv2.Mat):
    h, w, ch = input_img.shape
    out_img = np.zeros((h, w), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            pixel = input_img[y, x]
            b, g, r = pixel
            val = (0.001 * r + 0.005 * g + 0.995 * b)
            # val = np.average(pixel)
            out_img[y, x] = int(val)
    
    return out_img