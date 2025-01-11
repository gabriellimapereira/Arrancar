import pygame
import threading

pygame.mixer.init()

sound1 = pygame.mixer.Sound("efeito1.mp3")
sound2 = pygame.mixer.Sound("efeito2.mp3")
sound3 = pygame.mixer.Sound("efeito3.mp3")

def playEffect(effect, effectName):
    channel = pygame.mixer.find_channel()
    if channel:
        channel.play(effect)
        print(f"tocando: {effectName}")
    else:
        print("sem canais disponíveis para tocar o efeito!")

def chooseEffect():
    availableEffects = {
        1: sound1,
        2: sound2,
        3: sound3
    }
    
    effectsNames = {
        1: "efeito1.mp3",
        2: "efeito2.mp3",
        3: "efeito3.mp3"
    }
    
    while True:
        print("\nescolha os efeitos para tocar (digite 0 para terminar):")
        for number, name in effectsNames.items():
            print(f"{number}. {name}")
        try:
            choice = int(input("escolha um efeito (ou 0 para sair): "))
            if choice == 0:
                break
            if choice in availableEffects:
                choiceEffect = availableEffects[choice]
                choiceEffectName = effectsNames[choice]
                thread = threading.Thread(target=playEffect, args=(choiceEffect, choiceEffectName))
                thread.start()
            else:
                print("escolha inválida, tente novamente")
        except ValueError:
            print("escolha inválida, tente novamente")

def main():
    chooseEffect()
    print("programa finalizado")

if __name__ == "__main__":
    main()
