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
        print("\nMenu de usuário comum:")
        print("1 - Menu de músicas")
        print("2 - Menu de efeitos sonoros")
        print("3 - Menu de podcasts")
        print("4 - Menu de gravações")
        print("0 - Sair")
        choice = input("Escolha uma opção: ")

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
            print("Opção inválida. Tente novamente!")

def menuSuperUsuario(superUser, memorySystem):
    while True:
        print("\nMenu de super usuário:")
        print("1 - Menu de músicas")
        print("2 - Menu de efeitos sonoros")
        print("3 - Menu de podcasts")
        print("4 - Menu de gravações")
        print("0 - Sair")
        choice = input("Escolha uma opção: ")

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
            print("Opção inválida. Tente novamente!")

def musicsMenu(user, memorySystem):
    while True:
        print("\nMenu de músicas:")
        print("1 - Listar músicas")
        print("2 - Cadastrar música")
        print("3 - Reproduzir música")
        print("4 - Apagar música")
        print("5 - Listar músicas curtidas")
        print("0 - Voltar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            if not memorySystem.musics:
                print("Nenhuma música na lista!")
            else:
                print("Músicas cadastradas: ")
                print("------------------")
                for i in memorySystem.musics:
                    i.displayData()
                    print("------------------")

        elif choice == "2":
            print("Cadastrando música...\n")
            name = input("Qual o nome da música a ser adicionada? ")
            musicType = input("Qual o tipo da música? ")
            singer = input("Por último, qual o cantor/banda da música? ")
            print("Agora escolha o caminho do arquivo da música: ")
            time.sleep(1)
            newMusic = Music(name, singer, musicType)
            memorySystem.addMusic(newMusic)
            print("Música cadastrada com sucesso!")
        elif choice == "3":
            print("Músicas disponíveis:")
            for i, music in enumerate(memorySystem.musics):
                print(f"{i + 1} - {music.name}")
                print("------------------")

            choice = int(input("Escolha a música para reproduzir: ")) - 1

            if 0 <= choice < len(memorySystem.musics):
                musicMenu(memorySystem.musics[choice], user)
            else:
                print("Opção inválida! Tente novamente :/\n")
        elif choice == "4":
            name = input("Digite o nome da música a ser removida: ")
            music = memorySystem.findAudioByName(memorySystem.musics, name)
            if music == None:
                print("Música não encontrada. Verifique se ela está cadastrada ou se o nome foi digitado corretamente")
            else:
                memorySystem.removeAudio(memorySystem.musics, music)
                print("Música removida com sucesso!")
        elif choice == '5':
            if not user.likedSongs:
                print("Você não curtiu nenhuma música!")
            else:
                print("Músicas curtidas: ")
                for i in user.likedSongs:
                    print(i.name)
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")

def soundEffectsMenu(memorySystem):
    while True:
        print("\nMenu de efeitos sonoros:")
        print("1 - Listar efeitos sonoros")
        print("2 - Cadastrar efeito sonoro")
        print("3 - Reproduzir efeitos sonoros")
        print("4 - Apagar efeito sonoro")
        print("0 - Voltar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            if not memorySystem.soundEffects:
                print("Não há efeitos sonoros cadastrados!")
            else:
                print("Efeitos sonoros: ")
                print("------------------")
                for i in memorySystem.soundEffects:
                    i.displayData()
                    print("------------------")
        elif choice == "2":
            name = input("Qual o nome do efeito a ser adicionado? ")
            newEffect = SoundEffect(name)
            print("Agora escolha o caminho do arquivo do efeito sonoro: ")
            time.sleep(1)
            memorySystem.addSoundEffect(newEffect)
            print(f"Efeito {name} cadastrada com sucesso!")
        elif choice == "3":
            if not memorySystem.soundEffects:
                print("Não há nenhum efeito disponível para ser reproduzido!")
            else:
                menuSoundEffects(memorySystem)              
        elif choice == "4":
            name = input("Digite o nome do efeito a ser removido: ")
            soundEffect = memorySystem.findAudioByName(memorySystem.soundEffects, name)
            if soundEffect == None:
                print("Efeito não encontrado. Verifique se ele está cadastrado ou se o nome foi digitado corretamente")
            else:
                memorySystem.removeAudio(memorySystem.soundEffects, soundEffect)
                print("Efeito removido com sucesso!")
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")

def podcastMenu(memorySystem):
    while True:
        print("\nMenu de podcasts (usuário comum):")
        print("1 - Listar podcasts")
        print("2 - Escutar podcast")
        print("0 - Voltar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            if not memorySystem.podcasts:
                print("Nenhum podcast cadastrado!")
            else: 
                print("Podcasts cadastrados:")
                for i in memorySystem.podcasts:
                    i.displayData()
                    print("------------------")
        elif choice == "2":
            name = input("Qual o nome do podcast a ser reproduzido? ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast:
                audioMenu(podcast)
            else:
                print("O podcast não foi encontrado! tente novamente :/")
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")

def superPodcastMenu(memorySystem):
    while True:
        print("\nMenu de podcasts (super usuário):")
        print("1 - Listar podcasts")
        print("2 - Escutar podcast")
        print("3 - Adicionar podcast")
        print("4 - Apagar podcast")
        print("0 - Voltar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            if not memorySystem.podcasts:
                print("Nenhum podcast cadastrado!")
            else:
                print("Podcasts cadastrados: ")
                for i in memorySystem.podcasts:
                    i.displayData()
                    print("------------------")
        elif choice == "2":
            name = input("Qual o nome do podcast a ser reproduzido? ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast:
                audioMenu(podcast)
            else:
                print("O podcast não foi encontrado! tente novamente :/")
        elif choice == "3":
            print("Cadastrando podcast...")
            name = input("Qual o nome do podcast a ser adicionado? ")
            host = input("Qual o nome do host dele? ")
            category = input("Qual a categoria? ")
            date = input("Por último, qual a data de lançamento do podcast? ")
            print("Agora escolha o caminho do arquivo do podcast: ")
            time.sleep(1)
            newPodcast = Podcast(name, host, category, date)
            memorySystem.addPodcast(newPodcast)
            print("Podcast cadastrada com sucesso!")
        elif choice == "4":
            name = input("Digite o nome do podcast a ser removido: ")
            podcast = memorySystem.findAudioByName(memorySystem.podcasts, name)
            if podcast == None:
                print("Podcast não encontrado. Verifique se ele está cadastrado ou se o nome foi digitado corretamente")
            else:
                memorySystem.removeAudio(memorySystem.podcasts, podcast)
                print("Podcast removido com sucesso!")
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")

def recordingsMenu(user):
    while True:
        print("\nMenu de gravações:")
        print("1 - Listar gravações")
        print("2 - Iniciar gravação")
        print("3 - Reproduzir gravação")
        print("4 - Apagar reprodução")
        print("0 - Voltar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            if not user.recordings:
                print("Não há nenhuma gravação cadastrada!")
            else:
                print(f"Gravações do usuário {user.name}:")
                for i in user.recordings:
                    i.displayData()
                    print("------------------")
        elif choice == "2":
            while True:
                name = input("Digite o nome do áudio que será gravado: ")
                audio_file = name + '.mp3'
                print("Iniciando gravação...")

                Recording.record(name) 
                newRecord = Recording(name, audio_file, user.name)

                print("O áudio ficou assim...")
                newRecord.playAudio()

                while True:
                    option = input("Deseja manter (1) ou regravar (0)? ")
                    if option == "1":
                        user.recordings.append(newRecord)
                        print("Foi adicionado à sua lista de gravações!")
                        if newRecord.audioIsPlaying():
                            newRecord.stopAudio()
                        break
                    elif option == "0":
                        if os.path.exists(audio_file):
                            os.remove(audio_file)
                            print("O arquivo antigo foi excluído!")
                        else:
                            print("Não foi encontrado um arquivo antigo para excluir")

                        print("Regravando áudio...")
                        break
                    else:
                        print("Opção inválida, digite 1 para manter ou 0 para regravar!")

                if option == "1":
                    break
        elif choice == "3":
            if not user.recordings:
                print("Não há gravações para reproduzir!")
            else:
                for i, recording in enumerate(user.recordings):
                    print(f"{i + 1} - {recording.name}")
                choice = int(input("Escolha a gravação para reproduzir: ")) - 1
                if 0 <= choice < len(user.recordings):
                    audioMenu(user.recordings[choice])
                else:
                    print("Opção inválida!")
        elif choice == '4':
            name = input("Digite o nome da gravação a ser removida: ")
            recording = user.findRecording(name)
            if recording == None:
                print("Gravação não encontrada. Verifique se ela está cadastrada ou se o nome foi digitado corretamente")
            else:
                user.removeRecording(recording)
                print("Gravação removida com sucesso!")
        elif choice == "0":
            print("Voltando ao menu anterior...")
            break
        else:
            print("Opção inválida, tente novamente!")

def musicMenu(audio, user):
    audio.playAudio()
    while True:
        print("\nMenu:")
        print("1 - Pausar/despausar música")
        print("2 - Parar música")
        print("3 - Curtir música")
        print("4 - Sair")
        
        try:
            choice = int(input("Escolha uma opção: "))
            
            if choice == 1:
                if audio.audioIsPlaying():
                    print("Música pausada")
                    audio.pauseAudio()
                else:
                    print("Música retomada")
                    audio.unpauseAudio()
            elif choice == 2:
                print("Música parada")
                audio.stopAudio()
                break
            elif choice == 3:
                user.likeSong(audio)
            elif choice == 4:
                if audio.audioIsPlaying():
                    audio.stopAudio()
                print("Saindo do menu...")
                break
            else:
                print("Opção inválida, tente novamente")
        except ValueError:
            print("Opção inválida, tente novamente")

def audioMenu(audio):
    audio.playAudio()

    while True:
        print("\nMenu:")
        print("1 - Pausar/despausar")
        print("2 - Parar")
        print("0 - Sair")
        
        try:
            choice = int(input("Escolha uma opção: "))
            
            if choice == 1:
                if audio.audioIsPlaying():
                    print("Áudio pausado")
                    audio.pauseAudio()
                else:
                    print("Áudio retomado")
                    audio.unpauseAudio()
            elif choice == 2:
                print("Áudio parado")
                audio.stopAudio()
                break
            elif choice == 0:
                if audio.audioIsPlaying():
                    audio.stopAudio()
                print("Saindo do menu...")
                break
            else:
                print("Opção inválida, tente novamente!")
        except ValueError:
            print("Opção inválida, tente novamente!")

def menuSoundEffects(memorySystem):
    while True:
        print("\nMenu de efeitos sonoros:\n")
        for i in range(0, len(memorySystem.soundEffects)):
            print("{} - {}\n".format(i, memorySystem.soundEffects[i].name))

        choice = input("Escolha um efeito sonoro pelo número (ou digite -1 para sair): ")
        try:
            choice = int(choice)
            if 0 <= choice < len(memorySystem.soundEffects):
                effect = memorySystem.soundEffects[choice]
                thread = threading.Thread(target=effect.playEffect)
                thread.start()
            elif choice == -1:
                print("Encerrando a reprodução de áudios...")
                break
            else:
                print("Opção inválida, tente novamente!")
        except ValueError:
            print("Opção inválida, tente novamente!")