from abc import ABC
import pygame
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pydub.utils import mediainfo
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import threading
import os

class AudioArquive(ABC):
    def __init__(self, name, path=None):
        self._name = name
        self._path = path if path else self.findPath()
        self._duration = self.getDuration()

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path

    def displayData(self):
        print(f"nome: {self._name} duração: {self._duration} caminho: {self._path}")

    def playAudio(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self._path)
            pygame.mixer.music.play()
        except pygame.error as e:
            print(f"erro ao tentar tocar o áudio: {e}")
        except Exception as e:
            print(f"erro inesperado: {e}")

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
        path = askopenfilename(title="escolha um arquivo de áudio", filetypes=[("arquivos de áudio", "*.mp3"), ("arquivos de áudio", "*.wav")])
        if not path:
            raise ValueError("nenhum arquivo foi selecionado!\n")
        return path

    def getDuration(self):
        if not os.path.exists(self._path):
            print(f"Erro: O arquivo {self._path} não existe.")
            return
        audioInfo = mediainfo(self._path)
        return float(audioInfo['duration'])

class Music(AudioArquive):
    def __init__(self, name, singer, musicalType):
        super().__init__(name)
        self._singer = singer
        self._musicalType = musicalType

    def displayData(self):
        print(
            f"nome:           {self._name}\n"
            f"duração:        {self._duration}\n"
            f"caminho:        {self._path}\n"
            f"cantor/banda:   {self._singer}\n"
            f"tipo musical:   {self._musicalType}"
        )

class Podcast(AudioArquive):
    def __init__(self, name, host, category, date):
        super().__init__(name)
        self._host = host
        self._category = category
        self._date = date

    def displayData(self):
        print(
            f"nome:     {self._name}\n"
            f"host:     {self._host}\n"
            f"categoria:     {self._category}\n"
            f"data:     {self._date}"
        )

class SoundEffect(AudioArquive):
    def __init__(self, name):
        super().__init__(name)

    def displayData(self):
        print(
            f"nome:     {self._name}\n"
            f"duração:  {self._duration}\n"
            f"caminho:  {self._path}"
        )

    def playEffect(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        sound = pygame.mixer.Sound(self._path)
        channel = pygame.mixer.find_channel()

        if channel:
            channel.play(sound)
            print(f"tocando: {self._name}...")
            while channel.get_busy():
                pass  
        else:
            print("sem canais disponíveis para tocar o efeito!\n")

from pydub import AudioSegment

class Recording(AudioArquive):
    def __init__(self, name, path, autor):
        super().__init__(name, path)
        self._autor = autor

    def displayData(self):
        print(
            f"nome:     {self._name}\n"
            f"autor:    {self._autor}\n"
            f"caminho:  {self._path}"
        )

    @staticmethod
    def record(name):
        audioBlocks = []
        isRecording = [True]

        def recordAudio():
            while isRecording[0]:
                audioBlock = sd.rec(frames=44100, samplerate=44100, channels=2, dtype='float32')
                sd.wait()
                audioBlocks.append(audioBlock)

        recordThread = threading.Thread(target=recordAudio)
        recordThread.start()

        input("pressione ENTER para parar a gravação: \n")
        isRecording[0] = False

        recordThread.join()

        audioBlocks = np.concatenate(audioBlocks, axis=0)
        wavFile = f"{name}.wav"
        write(wavFile, 44100, (audioBlocks * 32767).astype(np.int16))

        mp3File = f"{name}.mp3"
        try:
            AudioSegment.from_wav(wavFile).export(mp3File, format="mp3")
            print(f"arquivo convertido para mp3: {mp3File}")
        except Exception as e:
            print(f"erro ao converter o arquivo para mp3: {e}")
            return

        try:
            os.remove(wavFile)
            print(f"arquivo temporário wav removido: {wavFile}")
        except Exception as e:
            print(f"erro ao remover o arquivo wav: {e}")
