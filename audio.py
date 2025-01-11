from abc import ABC, abstractmethod
import pygame
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pydub.utils import mediainfo
from systemMemory import SystemMemory

class AudioArquive(ABC):
    def __init__(self, name):
        self._name = name
        self._path = self.findPath()
        self._duration = self.getDuration()

    @property
    def path(self):
        return self._path

    def displayData(self):
        print(self._name, self._duration, self._path)

    def playAudio(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self._path)
        pygame.mixer.music.play()

    def stopAudio(self):
        pygame.mixer.music.stop()

    def audioIsPlaying(self):
        return pygame.mixer.music.get_busy()
    
    def pauseAudio(self):
        pygame.mixer.music.pause()

    def unpauseAudio(self):
        pygame.mixer.music.unpause()

    def findPath(self):
        Tk().withdraw() 
        path = askopenfilename(title="escolha um arquivo de áudio", filetypes=[("arquivos de áudio", "*.mp3;*.wav")])
        return path
    
    def getDuration(self):
        audioInfo = mediainfo(self._path)
        return float(audioInfo['duration'])
    
    @abstractmethod
    def findAudioByName(self):
        pass

class Music(AudioArquive):
    def __init__(self, name, singer, musicalType):
        super().__init__(name)
        self._singer = singer
        self._musicalType = musicalType

    def displayData(self):
        print(self._name, self._duration, self._path, self._musicalType)

    def findAudioByName(self, systemMemory, name):
        for music in systemMemory.musics:
            if music._name == name:
                return music
        return None

class Podcast(AudioArquive):
    def __init__(self, name, host, category, date):
        super().__init__(name)
        self._host = host
        self._category = category
        self._date = date

    def displayData(self):
        print(self._name, self._duration, self._path, self._host, self._category, self._date)

    def findAudioByName(self, systemMemory, name):
        for podcast in systemMemory.podcasts:
            if podcast._name == name:
                return podcast
        return None

class SoundEffect(AudioArquive):
    def __init__(self, name):
        super().__init__(name)

    def displayData(self):
        print(self._name, self._duration, self._path)

    def findAudioByName(self, systemMemory, name):
        for effect in systemMemory.soundEffects:
            if effect._name == name:
                return effect
        return None

class Recording(AudioArquive):
    def __init__(self, name):
        super().__init__(name)

    def displayData(self):
        print(self._name, self._duration, self._path)

    def findAudioByName(self, user, name):
        for music in user.recordings:
            if music._name == name:
                return music
        return None