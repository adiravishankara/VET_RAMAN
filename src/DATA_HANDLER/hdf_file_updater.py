import datetime
import sys

import h5py
import numpy as np
from PyQt5.QtWidgets import QApplication, QFileDialog


class FileUpdater:
    def __init__(self, filename=None):
        self.metadata_key = True
        self.load_file(filename)
        self.counter = 0

    def metadata_status(self, status):
        self.metadata_key = status

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
            self.hdf5_file = h5py.File(self.filename, 'r+')
            assert not self.hdf5_file.swmr_mode

            print("Successfully Loaded: {}".format(self.filename))
            if 'data' not in self.hdf5_file.keys():
                self.set_group('data')
        except FileNotFoundError:
            print("File Not Found")

    def new_group(self, group_name):
        try:
            assert group_name not in self.hdf5_file.keys()
            ng = self.hdf5_file.create_group(group_name)
            ng.attrs['Creation Time'] = datetime.datetime.now().strftime('%y_%m_%d_%H:%M:%S')
        except AssertionError:
            print('Group Exists')

    def set_group(self, group_name):
        if group_name not in self.hdf5_file.keys():
            print('Group does not exist. Creating group: {}'.format(group_name))
            self.new_group(group_name)

        self.group = self.hdf5_file[group_name]
        #self.group.swmr_mode = True
        print(self.group)

    def new_dataset(self, group_name=None, metadata=None, data=None):
        # This creates a new dataset within a group. If the dataset should be outside of any group, set self.gn to "".
        if group_name is None:
            print('Using Default')
            self.set_group('data')
        else:
            self.set_group(group_name)

        if not isinstance(data, np.ndarray):
            print("Value is in the wrong format")
            try:
                data = np.array(data)
            except:
                print('Something went wrong')

        self._ = self.group.create_dataset(str(self.counter), data.shape, data.dtype, data)
        self._.swmr_mode = True
        if self.metadata_key:
            self._.attrs["Measurement Count"] = self.counter
            self._.attrs["Measurement Time"] = datetime.datetime.now().strftime('%H:%M:%S')
            if metadata is not None:
                for element in metadata.keys():
                    self._.attrs[element] = metadata[element]
        self.counter += 1

    def write_metadata(self, metadata, group_name, data_set):
        _ = self.hdf5_file[group_name][data_set]
        _.attrs['Metadata Update Time'] = datetime.datetime.now().strftime('%y_%m_%d_%H:%M:%S')
        if metadata is not None:
            for element in metadata.keys():
                _.attrs[element] = metadata[element]

    def reset_counter(self):
        self.counter = 0

    def close_file(self):
        self.hdf5_file.close()


if __name__ == '__main__':
    A = FileUpdater()
