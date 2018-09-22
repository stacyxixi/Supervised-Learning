from matplotlib.colors import Normalize
import numpy as np


# Utility function to move the midpoint of a colormap to be around
# the values of interest.
# adapted from http://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html

class MidpointNormalize(Normalize):

    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))