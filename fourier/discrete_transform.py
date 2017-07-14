#import numpy
import numpy as np
import numpy.ma as ma

#import scipy functions for peak finding

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion 
from scipy.ndimage.morphology import iterate_structure

class Fourier(class):
    def filterlowamplitudes(C, threshold):
    """ Read

        Parameters
        ----------
        C: 2D numpy array of amplitudes from FFT
            Time on x, Frequency on y
        threshold: Threshold to determine high or low
        Returns
        -------
        2D boolean mask, True is high, False is low """
    m = np.copy(C)
    u = m < threshold
    ge = m > threshold
    m[u] = False
    m[ge] = True
    return m

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

    def pair_frequencies(data, peaks , look_ahead = 15):
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
        for current_time in range(len(time_array) - look_ahead): #dont compare last element(s)
            current_frequencies = time_array[current_time]
            for frequency1 in current_frequencies:
                
                for compare_time in range(look_ahead):
                    compare_frequencies = time_array[compare_time]
                    for frequency2 in compare_frequencies:
                        delta_t = compare_time - current_time
                        analyzed_freq.append((frequency1, frequency2, delta_t))
        return analyzed_freq


class Song(Fourier):
    def __init__(self,frequencyDeltas, author,title):
        self.author = author
        self.title = title

    def get_name(self):
        return self.author + " - " + self.title

    def author_title_from_filename(self,filename):
        """sets title and author from a filename

        Parameters
        ----------
        filename: the string name of the file. (not the path)

        Returns
        -------
        Nothing
        """
        filename = filename.replace('.mp3','')
        filename = filename.replace('_',' ')
        parts = filename.split(' - ')
        self.author = parts[0]
        self.title = parts[1]

    def isSimilar(self, compare_song):
    """ Find if the compare_song is a match to the current song

    Parameters
    ----------
    compare_song : Song

    Returns
    -------
    The similarity of the songs as an integer"""
            
            













