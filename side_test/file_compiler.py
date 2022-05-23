import os
import numpy as np


class FileCompiler:
    def __init__(self, directory):
        self.path = directory
        self.counter = 0
        self.array = np.empty([1024, 1])

    def load_file(self, filename):
        return np.loadtxt(filename, delimiter=',', skiprows=21)

    def parse_directory(self):
        for i in os.listdir(self.path):
            self.append_array(self.load_file("{}/{}".format(self.path, i)))

    def append_array(self, array):
        self.array = np.concatenate((self.array, array))

    def save_array(self):
        np.savetxt(self.array, 'C:/Users/arka_/PycharmProjects/VET_RAMAN/side_test/compiled.csv', delimiter=',', fmt='%.10f')
        print('File Saved')


if __name__ == '__main__':
    A = FileCompiler('C:/Users/arka_/PycharmProjects/VET_RAMAN/side_test/data/good')
    A.parse_directory()
    A.save_array()
