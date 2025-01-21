from audio import Music, Podcast, SoundEffect, Recording
import time
import threading
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
            podcastMenu(memorySystem)
        elif choice == "4":
            recordingsMenu(user)
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
            superPodcastMenu(memorySystem)
        elif choice == "4":
            recordingsMenu(superUser)
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
        print("5 - listar músicas curtidas")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            if not memorySystem.musics:
                print("nenhuma música na lista!")
            else:
                print("músicas cadastradas: ")
                for i in memorySystem.musics:
                    i.displayData()

        elif choice == "2":
            print("cadastrando música...\n")
            name = input("qual o nome da música a ser adicionada? ")
            musicType = input("qual o tipo da música? ")
            singer = input("por último, qual o cantor/banda da música? ")
            print("agora escolha o caminho do arquivo da música: ")
            time.sleep(1)
            newMusic = Music(name, singer, musicType)
            memorySystem.musics.append(newMusic)
            print("música cadastrada com sucesso!")
        elif choice == "3":
            print("músicas disponíveis:")
            for i, music in enumerate(memorySystem.musics):
                print(f"{i + 1} - {music.name}")

            choice = int(input("escolha a música para reproduzir: ")) - 1

            if 0 <= choice < len(memorySystem.musics):
                musicMenu(memorySystem.musics[choice], user)
            else:
                print("opção inválida! tente novamente :/\n")
        elif choice == "4":
            name = input("digite o nome da música a ser removida: ")
            music = memorySystem.findAudioByName(memorySystem.musics, name)
            if music == None:
                print("música não encontrada. verifique se ela está cadastrada ou se o nome foi digitado corretamente")
            else:
                memorySystem.removeAudio(memorySystem.musics, music)
                print("música removida com sucesso!")
        elif choice == '5':
            if not user.likedSongs:
                print("você não curtiu nenhuma música!")
            else:
                print("músicas curtidas: ")
                for i in user.likedSongs:
                    print(i.name)
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
            if not memorySystem.soundEffects:
                print("não há efeitos sonoros cadastrados!")
            else:
                print("efeitos sonoros: ")
                for i in memorySystem.soundEffects:
                    i.displayData()
        elif choice == "2":
            name = input("qual o nome do efeito a ser adicionado? ")
            newEffect = SoundEffect(name)
            memorySystem.addSoundEffect(newEffect)
            print(f"efeito {name} cadastrada com sucesso!")
        elif choice == "3":
            if len(memorySystem.soundEffects) > 0:
                menuSoundEffects(memorySystem)
            else:
                print("não há nenhum efeito disponível para ser reproduzido!")
        elif choice == "4":
            name = input("digite o nome do efeito a ser removido: ")
            soundEffect = memorySystem.findAudioByName(memorySystem.soundEffects, name)
            if soundEffect == None:
                print("efeito não encontrado. verifique se ele está cadastrado ou se o nome foi digitado corretamente")
            else:
                memorySystem.removeAudio(memorySystem.soundEffects, soundEffect)
                print("efeito removido com sucesso!")
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente!")

def podcastMenu(memorySystem):
    while True:
        print("\nmenu de podcasts (usuário comum):")
        print("1 - listar podcasts")
        print("2 - escutar podcast")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            if not memorySystem.podcasts:
                print("nenhum podcast cadastrado!")
            else: 
                print("podcasts cadastrados:")
                for i in memorySystem.podcasts:
                    i.displayData()
        elif choice == "2":
            name = input("qual o nome do podcast a ser reproduzido? ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast:
                audioMenu(podcast)
            else:
                print("o podcast não foi encontrado! tente novamente :/")
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente!")

def superPodcastMenu(memorySystem):
    while True:
        print("\nmenu de podcasts (super usuário):")
        print("1 - listar podcasts")
        print("2 - escutar podcast")
        print("3 - adicionar podcast")
        print("4 - apagar podcast")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            if not memorySystem.podcasts:
                print("nenhum podcast cadastrado!")
            else:
                for i in memorySystem.podcasts:
                    i.displayData()
        elif choice == "2":
            name = input("qual o nome do podcast a ser reproduzido? ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast:
                audioMenu(podcast)
            else:
                print("o podcast não foi encontrado! tente novamente :/")
        elif choice == "3":
            print("cadastrando podcast...")
            name = input("qual o nome do podcast a ser adicionado? ")
            host = input("qual o nome do host dele? ")
            category = input("qual a categoria? ")
            date = input("por último, qual a data de lançamento do podcast? ")
            newPodcast = Podcast(name, host, category, date)
            memorySystem.addPodcast(newPodcast)
            print("podcast cadastrada com sucesso!")
        elif choice == "4":
            name = input("digite o nome do podcast a ser removido: ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast == None:
                print("podcast não encontrado. verifique se ele está cadastrado ou se o nome foi digitado corretamente")
            else:
                memorySystem.removeAudio(memorySystem.podcasts, podcast)
                print("podcast removido com sucesso!")
        elif choice == "0":
            break
        else:
            print("opção inválida. tente novamente!")

def recordingsMenu(user):
    while True:
        print("\nmenu de gravações:")
        print("1 - listar gravações")
        print("2 - iniciar gravação")
        print("3 - reproduzir gravação")
        print("4 - apagar reprodução")
        print("0 - voltar")
        choice = input("escolha uma opção: ")

        if choice == "1":
            if not user.recordings:
                print("não há nenhuma gravação cadastrada!")
            else:
                print(f"gravações do usuário {user.name}:")
                for i in user.recordings:
                    i.displayData()
        elif choice == "2":
            while True:
                name = input("digite o nome do áudio que será gravado: ")
                audio_file = name + '.mp3'
                print("iniciando gravação...")

                Recording.record(name) 
                newRecord = Recording(name, audio_file, user.name)

                print("o áudio ficou assim...")
                newRecord.playAudio()

                while True:
                    option = input("deseja manter (1) ou regravar (0)? ")
                    if option == "1":
                        user.recordings.append(newRecord)
                        print("foi adicionado à sua lista de gravações!")
                        if newRecord.audioIsPlaying():
                            newRecord.stopAudio()
                        break
                    elif option == "0":
                        if os.path.exists(audio_file):
                            os.remove(audio_file)
                            print("o arquivo antigo foi excluído!")
                        else:
                            print("não foi encontrado um arquivo antigo para excluir")

                        print("regravando áudio...")
                        break
                    else:
                        print("opção inválida, digite 1 para manter ou 0 para regravar!")

                if option == "1":
                    break
        elif choice == "3":
            if not user.recordings:
                print("não há gravações para reproduzir!")
            else:
                for i, recording in enumerate(user.recordings):
                    print(f"{i + 1} - {recording.name}")
                choice = int(input("escolha a gravação para reproduzir: ")) - 1
                if 0 <= choice < len(user.recordings):
                    audioMenu(user.recordings[choice])
                else:
                    print("opção inválida!")
        elif choice == '4':
            name = input("digite o nome da gravação a ser removida: ")
            recording = user.findRecording(name)
            if recording == None:
                print("gravação não encontrada. verifique se ela está cadastrada ou se o nome foi digitado corretamente")
            else:
                user.removeRecording(recording)
                print("gravação removida com sucesso!")
        elif choice == "0":
            print("voltando ao menu anterior...")
            break
        else:
            print("opção inválida, tente novamente!")

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
                user.likeSong(audio)
            elif choice == 4:
                if audio.audioIsPlaying():
                    audio.stopAudio()
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
                if audio.audioIsPlaying():
                    audio.stopAudio()
                print("saindo do menu...")
                break
            else:
                print("opção inválida, tente novamente!")
        except ValueError:
            print("opção inválida, tente novamente!")

def menuSoundEffects(memorySystem):
    while True:
        print("\nmenu de efeitos sonoros:\n")
        for i in range(0, len(memorySystem.soundEffects)):
            print("{} - {}\n".format(i, memorySystem.soundEffects[i].name))

        choice = input("escolha um efeito sonoro pelo número (ou digite -1 para sair): ")
        try:
            choice = int(choice)
            if 0 <= choice < len(memorySystem.soundEffects):
                effect = memorySystem.soundEffects[choice]
                thread = threading.Thread(target=effect.playEffect)
                thread.start()
            elif choice == -1:
                print("encerrando a reprodução de áudios...")
                break
            else:
                print("opção inválida, tente novamente!")
        except ValueError:
            print("opção inválida, tente novamente!")