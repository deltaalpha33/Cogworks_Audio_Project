#import numpy
import numpy as np
import numpy.ma as ma

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
    ##acceptable_values = data > 1
    peaks = data == (maximum_filter(data, footprint=fp))
    ##acceptable_peaks = np.logical_and(peaks, acceptable_values)
    ##return acceptable_peaks
    return peaks

def pair frequencies(data, peaks , look_ahead = 15):
    """ Calculate Differences between  to sets of peaks represented  in 2D arrays of data.

    Parameters
    ----------
    data : numpy.ndarray
    peaks : numpy.ndarray 
        mask of peaks
    look_ahead : int
        how many other points of data to consider

    Returns
    -------
    Binary indicator, of the same shape as `data`. The value of
    True indicates a local peak. """

    masked_data = ma.masked_array(data,  mask=peaks)

    time_array = np.hsplit(x, x.shape[0]) #list of numpy arrays
    
    analyzed_freq = list()
    for current_time in range(len(time_array) - look_ahead): #dont compare last element
        current_frequencies = time_array[current_time]
        for frequency1 in current_frequencies:
            
            for compare_time in range(look_ahead):
                compare_frequencies = time_array[compare_time]
                for frequency2 in compare_frequencies:
                    delta_t = compare_time - current_time
                    analyzed_freq.append((frequency1, frequency2, delta_t))
    return analyzed_freq
            
            













