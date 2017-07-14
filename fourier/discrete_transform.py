#import numpy
import numpy as np

#import scipy functions for peak finding

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion 
from scipy.ndimage.morphology import iterate_structure

def smooth_transform(y, max_coefs):
""" Find Most Significant Fourier Coefficients
        
        Parameters
        ----------
        y : numpy.array[float]
            N evenly-spaced samples
        max_coefs : int
        	maximun number of Fourier Coefficients to keep

        
        Returns
        -------
        numpy.array[complex]
            N//2 + 1 - max_coeefs Fourier coefficients"""
    return np.fft.rfft(y)[max_coefs]

def local_peaks(data):
""" Find local peaks in a 2D array of data.

    Parameters
    ----------
    data : numpy.ndarray
    
    Returns
    -------
    Binary indicator, of the same shape as `data`. The value of
    True indicates a local peak. """
	ffp = generate_binary_structure(rank=2 , connectivity=2)
    acceptable_values = data > 1
    peaks = data == (maximum_filter(data, footprint=fp))
    acceptable_peaks = np.logical_and(peaks, acceptable_values)
    return acceptable_peaks

def acceptable_values(data):
"""finds acceptable C values in the forier transform
	
	Parameters
	----------
	data : numpy.ndarray

	Returns
	-------
	Binary indicator, of the same shape as `data`. 
	The value of True indicates an acceptable Fourier Constant"""
	pass

def compare_peaks(input1, input2):
	""" Score Difference between  to sets of peaks represented  in 2D arrays of data.

    Parameters
    ----------
    input1 : numpy.ndarray
    input2 : numpy.ndarray
    Returns
    -------
    Binary indicator, of the same shape as `data`. The value of
    True indicates a local peak. """

    pass