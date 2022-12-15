import sys

import numpy as np
from BaselineRemoval import BaselineRemoval as BR
from PyQt5.QtWidgets import QFileDialog, QApplication


class BaselineCorrector:
    def __init__(self, *args, **kwargs):
        self.correction_type = "ZhangFit"
        self.load_file()
        self.correct_array()
        self.save_file()
        print('All Done')

    def load_file(self):
        qapp = QApplication(sys.argv)
        self.filename = QFileDialog.getOpenFileName(caption='Load File')[0]
        self.array = np.loadtxt(self.filename, delimiter=',')

    def correct_array(self):
        self.bobj = BR(self.array)
        self.corrected_array = self.bobj.ZhangFit()

    # def correct_arrays(self):
    #     for i in range(self.array.shape[1]):



    def save_file(self):
        qapp = QApplication(sys.argv)
        self.save_file_name = QFileDialog.getSaveFileName(caption='Save File')[0]
        print(self.save_file_name)
        np.savetxt("{}.csv".format(self.save_file_name), self.corrected_array, delimiter=',')


if __name__ == '__main__':
    BaselineCorrector()