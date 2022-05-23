import datetime
import os
import sys

import h5py
import yaml
from PyQt5.QtWidgets import QApplication, QFileDialog


class FileCreator:
    def __init__(self):
        self.set_file_name()

    def set_file_name(self):
        self.qapp = QApplication(sys.argv)
        filename = QFileDialog.getSaveFileName(
            caption="Experiment Name",
            directory="C:/Users/arka_/PycharmProjects/VET_RAMAN/data/test/"
                      "{}.hdf5".format(datetime.datetime.now().strftime("%y%m%d_%H%M%S")))

        if filename[0] != "":
            if filename[0].find(".hdf5") == -1:
                fname = "{}.hdf5".format(filename[0])

            else:
                fname = filename[0]
            print("Sucessfully Created: \n{}".format(fname))

            self.filename = fname
            self.create_file(self.filename)

            self.add_metadata()
            self.hdf5_file.close()

        else:
            print("No File Created")

    def get_file_name(self):
        return self.filename

    def create_file(self, filename=None, path=None):
        if filename is None:
            filename = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

        if path is not None:
            filename = "{}/{}".format(path, filename)

        try:
            self.hdf5_file = h5py.File('{}'.format(filename), 'w-')
        except FileExistsError:
            print("Overwriting Existing File")
            os.remove(filename)
            self.hdf5_file = h5py.File('{}'.format(filename), 'w-')

    def add_metadata(self):
        with open('file_creation_metadata.yaml', 'r') as f:
            self.yaml_data = yaml.safe_load(f)

        self.hdf5_file.attrs['Creation Date'] = datetime.datetime.now().strftime('%y-%m-%d')
        self.hdf5_file.attrs['Creation Time'] = datetime.datetime.now().strftime('%H:%M:%S')
        for element in self.yaml_data.keys():
            self.hdf5_file.attrs[element] = self.yaml_data[element]


if __name__ == '__main__':
    A = FileCreator()

