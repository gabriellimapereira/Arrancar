from user import User, SuperUser
from audio import AudioArquive, Music, Podcast, SoundEffect, Recording
from systemMemory import SystemMemory
import time
import threading

def menuUsuario(user, memorySystem):
    while True:
        print("\nmenu de usuário comum:")
        print("1 - menu de músicas")
        print("2 - menu de efeitos sonoros")
        print("3 - menu de podcasts")
        print("4 - menu de gravações")
        print("0 - sair")
        choice = input("escolha uma opção: ")

        if choice == "1":
            musicsMenu(user, memorySystem)
        elif choice == "2":
            soundEffectsMenu(memorySystem)
        elif choice == "3":
            podcastMenu(user, memorySystem)
        elif choice == "4":
            recordingsMenu(user, memorySystem)
        elif choice == "0":
            print(f"{user._name} saiu do sistema")
            break
        else:
            print("opção inválida. tente novamente")

def menuSuperUsuario(superUser, memorySystem):
    while True:
        print("\nmenu de super usuário:")
        print("1 - menu de músicas")
        print("2 - menu de efeitos sonoros")
        print("3 - menu de podcasts")
        print("4 - menu de gravações")
        print("0 - sair")
        choice = input("escolha uma opção: ")

        if choice == "1":
            musicsMenu(superUser, memorySystem)
        elif choice == "2":
            soundEffectsMenu(memorySystem)
        elif choice == "3":
            superPodcastMenu(superUser, memorySystem)
        elif choice == "4":
            recordingsMenu(superUser, memorySystem)
        elif choice == "0":
            print(f"{superUser._name} saiu do sistema!")
            break
        else:
            print("opção inválida. tente novamente!")

def musicsMenu(user, memorySystem):
    while True:
        print("\nmenu de músicas:")
        print("1 - listar músicas")
        print("2 - cadastrar música")
        print("3 - reproduzir música")
        print("4 - apagar música")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            if len(memorySystem.musics) == 0:
                print("nenhuma música na lista!\n")
            else:
                for i in memorySystem.musics:
                    i.displayData()

        elif choice == "2":
            print("cadastrando música...\n")
            name = input("qual o nome da música a ser adicionada? ")
            musicType = input("qual o tipo da música? ")
            singer = input("por último, qual o cantor/banda da música? ")
            newMusic = Music(name, singer, musicType)
            memorySystem.musics.append(newMusic)
            print("música cadastrada com sucesso!\n")
        elif choice == "3":
            name = input("qual o nome da música a ser reproduzida?")
            music = memorySystem.findAudioByName(memorySystem.musics, name)
            if music:
                musicMenu(music, user)
            else:
                print("a música não foi encontrada! tente novamente :/\n")
        elif choice == "4":
            name = input("digite o nome da música a ser removida: ")
            music = memorySystem.findAudioByName(memorySystem.musics, name)
            memorySystem.musics.remove(music)
        elif choice == "5":
            print("curtindo música...")
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente!")

def soundEffectsMenu(memorySystem):
    while True:
        print("\nmenu de efeitos sonoros:")
        print("1 - listar efeitos sonoros")
        print("2 - cadastrar efeito sonoro")
        print("3 - reproduzir efeitos sonoros")
        print("4 - apagar efeito sonoro")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            for i in memorySystem.soundEffects:
                i.displayData()
        elif choice == "2":
            name = input("qual o nome do efeito a ser adicionado? ")
            newEffect = SoundEffect(name)
            memorySystem.addSoundEffect(newEffect)
            print("música cadastrada com sucesso!\n")
        elif choice == "3":
            if len(memorySystem.soundEffects) > 0:
                menuSoundEffects(memorySystem)
            else:
                print("não há nenhum efeito disponível para ser reproduzido!\n")
        elif choice == "4":
            name = input("digite o nome do efeito a ser removido: ")
            effect = memorySystem.findAudioByName(memorySystem.soundEffects, name)
            memorySystem.soundEffects.remove(effect)
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente.")

def podcastMenu(user, memorySystem):
    while True:
        print("\nmenu de podcasts (usuário comum):")
        print("1 - listar podcasts")
        print("2 - escutar podcast")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            for i in memorySystem.podcasts:
                i.displayData()
        elif choice == "2":
            name = input("qual o nome do podcast a ser reproduzido? ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast:
                audioMenu(podcast)
            else:
                print("o podcast não foi encontrado! tente novamente :/\n")
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente!")

def superPodcastMenu(superUser, memorySystem):
    while True:
        print("\nmenu de podcasts (super usuário):")
        print("1 - listar podcasts")
        print("2 - escutar podcast")
        print("3 - adicionar podcast")
        print("4 - apagar podcast")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            for i in memorySystem.podcasts:
                i.displayData()
        elif choice == "2":
            name = input("qual o nome do podcast a ser reproduzido? ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast:
                audioMenu(podcast)
            else:
                print("o podcast não foi encontrado! tente novamente :/\n")
        elif choice == "3":
            print("cadastrando música...")
            name = input("qual o nome do podcast a ser adicionado? ")
            host = input("qual o nome do host dele? ")
            category = input("qual a categoria? ")
            date = input("por último, qual a data de lançamento do podcast? ")
            newPodcast = Podcast(name, host, category, date)
            memorySystem.addPodcast(newPodcast)
            print("música cadastrada com sucesso!\n")
        elif choice == "4":
            name = input("digite o nome do podcast a ser removido: ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            memorySystem.podcasts.remove(podcast)
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente.")

def recordingsMenu(user, memorySystem):
    while True:
        print("\nmenu de gravações:")
        print("1 - listar gravações")
        print("2 - iniciar gravação")
        print("3 - reproduzir gravação")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            for i in user.recordings:
                i.displayData()
        elif choice == "2":
            while True:
                name = input("digite o nome do áudio que será gravado: ")
                print("iniciando gravação...")

                Recording.record(name)
                newRecord = Recording(name, name + '.mp3', user.name)

                print("o áudio ficou assim...")
                newRecord.playAudio()

                while True:
                    option = input("deseja manter (1) ou regravar (0)? ")
                    if option == "1":
                        user.recordings.append(newRecord)
                        print("foi adicionado à sua lista de gravações!")
                        break
                    elif option == "0":
                        print("regravando áudio...")
                        break
                    else:
                        print("opção inválida, digite 1 para manter ou 0 para regravar!")
                
                if option == "1":
                    break

        elif choice == "3":
            name = input("qual o nome da música a ser reproduzida?")
            recording = memorySystem.findAudioByName(memorySystem.recordings, name)
            if recording:
                audioMenu(recording, user)
            else:
                print("a música não foi encontrada! tente novamente :/\n")
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente")

def musicMenu(audio, user):
    audio.playAudio()
    while True:
        print("\nmenu:")
        print("1 - pausar/despausar música")
        print("2 - parar música")
        print("3 - curtir música")
        print("4 - sair")
        
        try:
            choice = int(input("escolha uma opção: "))
            
            if choice == 1:
                if audio.audioIsPlaying():
                    print("música pausada")
                    audio.pauseAudio()
                else:
                    print("música retomada")
                    audio.unpauseAudio()
            elif choice == 2:
                print("música parada")
                audio.stopAudio()
                break
            elif choice == 3:
                if audio in user.linkedSongs:
                    time.sleep(1)
                    print("música retirada da playlist de músicas curtidas!\n")
                    user.linkedSongs.remove(audio)
                else:
                    time.sleep(1)
                    print("música adicionada à playlist de músicas curtidas!\n")
                    user.linkedSongs.append(audio)
            elif choice == 4:
                print("saindo do menu...")
                break
            else:
                print("opção inválida, tente novamente")
        except ValueError:
            print("opção inválida, tente novamente")

def audioMenu(audio):
    audio.playAudio()

    while True:
        print("\nmenu:")
        print("1 - pausar/despausar")
        print("2 - parar")
        print("0 - sair")
        
        try:
            choice = int(input("escolha uma opção: "))
            
            if choice == 1:
                if audio.audioIsPlaying():
                    print("áudio pausado")
                    audio.pauseAudio()
                else:
                    print("áudio retomado")
                    audio.unpauseAudio()
            elif choice == 2:
                print("áudio parado")
                audio.stopAudio()
                break
            elif choice == 0:
                print("saindo do menu")
                break
            else:
                print("opção inválida, tente novamente")
        except ValueError:
            print("opção inválida, tente novamente")

def menuSoundEffects(memorySystem):
    while True:
        print("\nmenu de efeitos sonoros:\n")
        for i in range(0, len(memorySystem.soundEffects)):
            print("{} - {}\n".format(i, memorySystem.soundEffects[i].name))

        choice = input("escolha um efeito sonoro pelo número: ")
        try:
            choice = int(choice)
            if 0 <= choice < len(memorySystem.soundEffects):
                effect = memorySystem.soundEffects[choice]
                thread = threading.Thread(target=effect.playEffect)
                thread.start()
            elif choice == -1:
                print("encerrando reprodução de áudios...")
                break
            else:
                print("opção inválida, tente novamente!")
        except ValueError:
            print("opção inválida, tente novamente!")