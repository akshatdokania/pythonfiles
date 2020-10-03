import numpy as np
def image2vector(img):
    v = np.reshape(img[0]*img[1]*img[2],1)
    return v
