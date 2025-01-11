import sounddevice as sd
import numpy as np
import pygame
import threading
from scipy.io.wavfile import write

from audio import AudioArquive

class Recorder():
    def __init__(self):
        self._musics = []
        self._podcasts = []
        self._soundEffects = []

    def addMusic(self, newMusic):
        self._musics.append(newMusic)

    def addPodcast(self, newPodcast):
        self._podcasts.append(newPodcast)

    def addSoundEffect(self, newSoundEffect):
        self._soundEffects.append(newSoundEffect)

    def recordAudio(self):
        isRecording = True

        audio = []
        while isRecording:
            audioBlock = sd.rec(frames=44100, samplerate=44100, channels=2, dtype='float32')
            sd.wait()
            audio.append(audioBlock)

        audio = np.concatenate(audio, axis=0)
        write("recordAudio.wav", 44100, (audio * 32767).astype(np.int16))

        return True

    def deleteAudio(self, path):
        pass