import numpy as np
from scipy.signal import find_peaks

import os


class Backend:
    def __init__(self):
        self.skip_rows = 21
        self.num_peaks = 0
        self.x_min = 275
        self.x_max = 1750
        self.min_prominence = None
        self.min_distance = None
        self.min_height = None
        self.threshold = None
        self.width = None
        self.plateau_size = None

    def load_directory(self, directory):
        self.directory = directory
        self.file_list = os.listdir(directory)

    def load_file(self, filename):
        self.current_file = np.loadtxt(filename, delimiter=',', skiprows=self.skip_rows)

    def crop_dataset(self):
        ind1 = np.where(self.current_file[0] < self.x_min)[-1]+1
        ind2 = np.where(self.current_file[0] > self.x_max)[0] -1

        self.x = self.current_file[ind1:ind2, 0]
        self.y = self.current_file[ind1:ind2, 1]

    def get_peaks(self):
        self.peaks, self.properties = find_peaks(self.y,
                                                 prominence=self.min_prominence, distance=self.min_distance,
                                                 height=self.min_height, width=self.width, threshold=self.threshold,
                                                 plateau_size=self.plateau_size)
        self.peak_x = []
        self.peak_y = []
        for element in self.peaks:
            self.peak_x.append(self.x[element])
            self.peak_y.append(self.y[element])
        self.peak_x = np.array(self.peak_x)
        self.peak_y = np.array(self.peak_y)


    def set_skiprows(self, val):
        self.skip_rows = val

    def set_min_prominence(self, val):
        if val == 0:
            self.min_prominence = None
        else:
            self.min_prominence = val

    def set_min_distance(self, val):
        if val == 0:
            self.min_distance = None
        else:
            self.min_distance = val

    def set_min_height(self, val):
        if val == 0:
            self.min_height = None
        else:
            self.min_height = val

    def set_threshold(self, val):
        if val == 0:
            self.threshold = None
        else:
            self.threshold = val

    def set_width(self, val):
        if val == 0:
            self.width = None
        else:
            self.width = val

    def set_plateau(self, val):
        if val == 0:
            self.plateau_size = None
        else:
            self.plateau_size = val

    def set_x_range(self, min, max):
        self.x_min = min
        self.x_max = max



