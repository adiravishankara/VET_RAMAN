import numpy as np
from scipy.spatial import distance


class matcher:
    def __init__(self, test_array=[], check_array=[]):
        self.test_array = np.array(test_array)
        self.check_array = np.array(check_array)
        print('Test Array Shape: {}\nCheck Array Shape: {}'.format(self.test_array.shape, self.check_array.shape))

        # STEP 1.