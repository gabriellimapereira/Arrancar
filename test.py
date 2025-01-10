import pygame
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from classes import Music

Tk().withdraw()
caminho_do_audio = askopenfilename(title="selecione um arquivo de áudio", filetypes=[("Arquivos de áudio", "*.mp3 *.wav")])
music = Music("R U Mine", 300, caminho_do_audio)

if music.path:
    music.playMusic()

    while True:
        comando = input("digite 'p' para pausar/despausar, 's' para parar: ").lower()
        if comando == 'p':
            if music.musicIsPlaying():
                music.stopMusic()
            else:
                music.unpauseMusic()
        elif comando == 's':
            music.stopMusic()
            break
