import numpy as np

def normalize_rows(x):
    x_norm = np.linalg.norm(x, ord = 2 , axis = 1 , keepdims = True)
    x = x/x_norm
    return x
