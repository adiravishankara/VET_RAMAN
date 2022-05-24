import numpy as np
import h5py
from scipy.signal import find_peaks


class Noodles:
    def __init__(self):
        self.min_prominence = 10
        self.min_distance = 10

    def get_peaks(self, x=None, y=None):
        if x is None:
            x = self.x
            y = self.y

        self.peaks, self.properties= find_peaks(y, prominence=self.min_prominence, distance=self.min_distance)
        self.z = []
        for element in self.peaks:
            self.z.append(x[element])
        print("Peaks Index: {}"
              "\nWavenumber: {}"
              "\nOther Values: {}".format(self.peaks, self.z, self.properties))

    def set_data(self, x, y):
        self.x = x
        self.y = y

    def save_peaks(self):
        np.savetxt('C:/Users/arka_/PycharmProjects/VET_RAMAN/side_test/data/peaks_list.csv', self.z, delimiter=',', fmt='%.10f')


def

if __name__ == '__main__':
    filename = 'C:/Users/arka_/PycharmProjects/VET_RAMAN/side_test/data/good/Acetaminophen-01.csv'
    A = np.loadtxt(filename, delimiter=',')

    B.get_peaks(A[:, 0], A[:, 1])
