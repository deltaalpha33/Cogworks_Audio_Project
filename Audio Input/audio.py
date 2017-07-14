import numpy as np
import librosa
import pyaudio

class Audio:
    def __init__(self):
        pass
    #gets a file path and returns a numpy array
    def read_file(self,path,sample_rate = 44100):
        song, song_sample_rate = librosa.load(path,sr=sample_rate, mono=True)
        return song, song_sample_rate
    #Reads 'seconds' seconds of audio from the mic and returns as a numpy array
    def read_mic(self,seconds=5):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100//2 #For some reason the stream reads at twice the input rate. -_- ?
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