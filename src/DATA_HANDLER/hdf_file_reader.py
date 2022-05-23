import sys

import h5py
import numpy as np
from PyQt5.QtWidgets import QApplication, QFileDialog


class FileReader:
    def __init__(self, filename=None, group_name=None):
        self.load_file(filename)
        self.set_group(group_name)
        self.create_array()

    def load_file(self, filename):
        if filename is None:
            self.qapp = QApplication(sys.argv)
            filename = QFileDialog.getOpenFileName(
                caption="Experiment Name",
                directory="C:/Users/arka_/PycharmProjects/VET_RAMAN/data/test/")

            if filename[0] != "":
                if filename[0].find(".hdf5") == -1:
                    fname = "{}.hdf5".format(filename[0])
                else:
                    fname = filename[0]
                self.filename = fname
            else:
                print("No File Selected")
        else:
            self.filename = filename

        try:
            self.hdf5_file = h5py.File(self.filename, 'r', swmr=True)
            assert self.hdf5_file.swmr_mode

            print("Successfully Loaded: {}".format(self.filename))
        except FileNotFoundError:
            print('File Not Found')

    def set_group(self, group_name):
        if self.hdf5_file.keys() is not None:
            if group_name is None:
                group_name = 'data'
            self.file = self.hdf5_file[group_name]
        else:
            print('None groups yet.')

    def create_array(self):
        self.array = []
        for element in self.file:
            self.array.append(self.file[element][:, 1])
        self.array = np.array(self.array).transpose()
        print("Initial Array Shape: {}".format(self.array.shape))

    def update_array(self, array=None):
        if array is None:
            _ = self.file.keys()[-1][:, 1]
        else:
            _ = array
        _ = np.array(array)
        assert isinstance(_, np.ndarray)
        if _.shape[1] != 1:
            _ = _.transpose()
        assert _.shape[0] == self.array.shape[0]
        self.array = np.c_[self.array, _]

    def get_array(self):
        return self.array

    def close_file(self):
        self.hdf5_file.close()


if __name__ == '__main__':
    A = FileReader()
    B = np.random.rand(40, 1)
    A.update_array(B)
    C = A.get_array()
    print(C.shape)
    A.close_file()


