import numpy as np
from multiprocessing import Process, Event, Pipe

from hdf_file_creator import FileCreator
from hdf_file_updater import FileUpdater
from hdf_file_reader import FileReader

class FileHandler:
    def __init__(self):
        pass




if __name__ == '__main__':
    A = FileCreator()
    B = A.get_file_name()
    C = FileUpdater(B)
    from time import sleep

    metadata = {'device id': 1, 'software version': 1.0, 'measurement id': 749}

    for i in range(10):
        C.new_dataset(metadata=metadata, data=np.random.rand(40, 2))
        sleep(0.5)
    C.close_file()
