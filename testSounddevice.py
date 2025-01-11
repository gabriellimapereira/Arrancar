import sounddevice as sd
import numpy as np
import pygame
import threading
from scipy.io.wavfile import write

fs = 44100
duration = []
is_recording = True
audio_filename = 'gravacao.wav'

def record_audio():
    global duration, is_recording
    while is_recording:
        audio_block = sd.rec(frames=fs, samplerate=fs, channels=2, dtype='float32')
        sd.wait()
        duration.append(audio_block)

    duration = np.concatenate(duration, axis=0)
    write(audio_filename, fs, (duration * 32767).astype(np.int16))

def main():
    global is_recording

    record_thread = threading.Thread(target=record_audio)
    record_thread.start()

    input("pressione ENTER para parar a gravação\n")
    is_recording = False

    record_thread.join()

    pygame.mixer.init()

    print("reproduzindo o áudio gravado...")
    pygame.mixer.music.load(audio_filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    print("reprodução finalizada")

if __name__ == "__main__":
    main()
