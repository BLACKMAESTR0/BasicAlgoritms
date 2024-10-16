import numpy as np
def RMSE(labels, predictions):
    n = len(labels)
    diff = np.subtract(labels,predictions)
    return np.sqrt(1.0/n * (np.dot(diff, diff))) # np.dot - скалярное произведение векторов