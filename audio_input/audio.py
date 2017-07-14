import numpy as np
import librosa
import pyaudio

class Audio:
    def __init__(self):
        pass

    def read_audio_file(self,path,sample_rate = 44100):
        """ Read Audio File from File System

        Parameters
        ----------
        path: global path to file
        sample_rate: int
        
        Returns
        -------
        Array of audio data"""

        song, song_sample_rate = librosa.load(path,sr=sample_rate, mono=True)
        return song, song_sample_rate

    def read_mic(self,seconds=5):
        """ Read audio from the mic and returns as a numpy array

        Parameters
        ----------
        secconds: secconds of audio to read
        
        Returns
        -------
        Array of audio data"""

        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        npaudio = np.fromstring(stream.read(RATE*seconds),dtype=np.int16)
        stream.stop_stream()
        stream.close()
        p.terminate()
        return npaudio


    def play_audio(self,soundArray):
        """ Plays audio from a numpy array

        Parameters
        ----------
        soundArray: numpy array

        Returns
        -------
        Nothing"""
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        stream.write(np.tile(soundArray,2), num_frames=None, exception_on_underflow=False)#repeat the data because pyaudio plays only half of the data -_- ?
        stream.stop_stream()
        stream.close()
        p.terminate()
