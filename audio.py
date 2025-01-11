from abc import ABC, abstractmethod
import pygame

class AudioArquive(ABC):
    def __init__(self, name, duration, path):
        self._name = name
        self._duration = duration
        self._path = path

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

class Music(AudioArquive):
    def __init__(self, name, duration, path, singer, musicalType):
        super().__init__(name, duration, path)
        self._singer = singer
        self._musicalType = musicalType

class Podcast(AudioArquive):
    def __init__(self, name, duration, path, host, category, date):
        super().__init__(name, duration, path)
        self._host = host
        self._category = category
        self._date = date

class SoundEffect(AudioArquive):
    def __init__(self, name, duration, path):
        super().__init__(name, duration, path)

class Recording(AudioArquive):
    def __init__(self, name, duration, path):
        super().__init__(name, duration, path)