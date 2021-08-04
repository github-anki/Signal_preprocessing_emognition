import numpy as np

def normalize(signal):
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))