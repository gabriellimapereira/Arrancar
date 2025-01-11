import sounddevice as sd
import numpy as np
import pygame
import threading
from scipy.io.wavfile import write

from audio import AudioArquive

class Recorder():
    def RecordAudio(self):
        isRecording = True

        duration = []
        while isRecording:
            audioBlock = sd.rec(frames=44100, samplerate=44100, channels=2, dtype='float32')
            sd.wait()
            duration.append(audioBlock)

        duration = np.concatenate(duration, axis=0)
        write("recordAudio.wav", 44100, (duration * 32767).astype(np.int16))

        return True