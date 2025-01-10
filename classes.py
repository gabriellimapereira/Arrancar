from abc import ABC, abstractmethod
import pygame

class Music:
    def __init__(self, name, duration, path):
        self._name = name
        self._duration = duration
        self._path = path

    @property
    def path(self):
        return self._path

    def displayData(self):
        print(self._name, self._duration, self._path)

    def playMusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self._path)
        pygame.mixer.music.play()

    def stopMusic(self):
        pygame.mixer.music.stop()

    def musicIsPlaying(self):
        return pygame.mixer.music.get_busy()
    
    def pauseMusic(self):
        pygame.mixer.music.pause()

    def unpauseMusic(self):
        pygame.mixer.music.unpause()