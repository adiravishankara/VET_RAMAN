import numpy as np
import h5py
import sklearn


class Noodles:
    def __init__(self):
        self.min_prominence = 10
        self.min_distance = 10

    def get_peaks(self, x=None, y=None):
        if x and y is None:
            x = self.x
            y = self.y

    def set_data(self, x, y):
        self.x = x
        self.y = y

    def save_peaks(self, append=True):



