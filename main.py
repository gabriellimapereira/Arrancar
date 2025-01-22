import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" 

from user import User, SuperUser
from systemMemory import SystemMemory
import userMenu
from userMenu import clear

def manual():
    while True:
        print("MANUAL DE USO:\n")

        print("1. ÁUDIO:")
        print("   Existem quatro classes de áudio: Músicas, Podcasts, Efeitos Sonoros e Gravações.")
        print("   - As Músicas, Podcasts e Efeitos Sonoros devem estar no computador do usuário (de preferência no formato .mp3).")
        print("   - Para reproduzí-los, é necessário cadastrá-los.")
        print("   - No menu de cadastro de qualquer um desses áudios, preencha os campos solicitados.")
        print("   - Após preencher os campos, será aberta uma janela para a seleção do arquivo de áudio.")
        print("   - Novamente, recomenda-se a escolha de arquivos .mp3.")
        print("   - Todos os áudios cadastrados podem ser acessados por todos os usuários, exceto as Gravações, que são particulares.")
        print("   - Apenas os Super Usuários podem registrar Podcasts.\n")

        print("2. EFEITOS SONOROS E GRAVAÇÕES:")
        print("   - Os Efeitos Sonoros podem ser reproduzidos simultaneamente. Fique à vontade para reproduzir vários ao mesmo tempo.")
        print("   - Para Gravações, recomenda-se o uso de um microfone para captação do áudio.\n")

        print("3. RESSALVAS:")
        print("   - Super Usuários devem cadastrar senhas para acesso.")
        print("   - Quando qualquer tipo de usuário for cadastrado, será gerado um identificador único para ele.\n")

        verification = input("ENTENDIDO? (PRESSIONE ENTER PARA CONTINUAR): ")
        if verification.strip() or verification == "":
            break


def idInput():
    while True:
        id = input("Digite o id: ")
        if id.isdigit():
            return int(id)
        else:
            print("Por favor, digite apenas números inteiros!")

def loginUser(userList, memorySystem):
    userId = idInput()
    for user in userList:
        if user.id == userId:
            print(f"\nLogin bem-sucedido para o usuário {user._name}!")
            userMenu.menuUsuario(user, memorySystem)
            return user
    print("\nId de usuário não encontrado. Tente novamente!")
    return None

def loginSuperUser(superUserList, memorySystem):
    userId = idInput()
    password = input("Digite sua senha: ")
    for superUser in superUserList:
        if superUser.id == userId and superUser.password == password:
            print(f"\nLogin bem-sucedido para o super usuário {superUser.name}!")
            userMenu.menuSuperUsuario(superUser, memorySystem)
            return superUser
    print("\nId ou senha de super usuário incorretos! Tente novamente!")
    return None

def registerUser(userList, superUserList):
    choice = None
    while choice not in {"0", "1"}:
        choice = input("Você quer registrar um usuário comum ou um super usuário? (0 para comum / 1 para super usuário): ")
        if choice not in {"0", "1"}:
            print("Entrada inválida. Digite 0 para usuário comum ou 1 para super usuário!")

    if choice == "0":
        name = input("Digite o seu nome como usuário: ")
        newUser = User(name, userList, superUserList)
        print(f"Usuário cadastrado! o seu id é: {newUser.id}. Não se esqueça dele!")
        userList.append(newUser)
    else:
        name = input("Digite o seu nome como super usuário: ")
        password = input("Agora digite a senha. Se lembre dela, ou será f: ")
        newUser = SuperUser(name, userList, superUserList, password)
        print(f"Usuário cadastrado! O seu id é: {newUser.id}. Não se esqueça dele!")
        superUserList.append(newUser)

def deleteUser(userList, superUserList):
    choice = None
    while choice not in {"0", "1"}:
        choice = input("Você deseja apagar um usuário comum (0) ou um super usuário (1)? ")
        if choice not in {"0", "1"}:
            print("Entrada inválida. Digite 0 para usuário comum ou 1 para super usuário!")

    userId = idInput()

    if choice == "0": 
        if not userList:
            print("A lista de usuários está vazia!")
            return
        for user in userList[:]:  
            if user.id == userId:
                userList.remove(user)
                print(f"Usuário comum com id {userId} foi apagado com sucesso!")
                return
        print("Id de usuário comum não encontrado. Tente novamente!")
    else:  
        if not superUserList:
            print("A lista de super usuários está vazia!")
            return
        for superUser in superUserList[:]:  
            if superUser.id == userId:
                superUserList.remove(superUser)
                print(f"Super usuário com id {userId} foi apagado com sucesso!")
                return
        print("Id de super usuário não encontrado. Tente novamente!")

def listUsers(userList, superUserList):
    print("Lista de usuários comuns:")
    if userList:
        for i in userList:
            i.displayUser()
    else:
        print("Não há usuários comuns cadastrados!")
    
    print("Lista de super usuários:")
    if superUserList:
        for i in superUserList:
            i.displayUser()
    else:
        print("Não há super usuários cadastrados!")

def exitProgram():
    print("Saindo do sistema... Até logo!")
    exit()

def invalidChoice():
    print("Opção inválida. Por favor, tente novamente!")

def loginMenu(userList, superUserList, memorySystem):
    print("Bem-vindo(a) ao Arrancar!\nDê uma arrancada na sua vida! :)")
    while True:
        print("\nSelecione uma opção:")
        print("1 - Entrar como usuário comum")
        print("2 - Entrar como super usuário")
        print("3 - Registrar-se como usuário (ou super usuário)")
        print("4 - Apagar registro de usuário")
        print("5 - Listar todos os usuários")
        print("0 - Sair")
        
        try:
            choice = int(input("\nDigite a opção: "))
        except ValueError:
            choice = -1

        options = {
            1: lambda: loginUser(userList, memorySystem),
            2: lambda: loginSuperUser(superUserList, memorySystem),
            3: lambda: registerUser(userList, superUserList),
            4: lambda: deleteUser(userList, superUserList),
            5: lambda: listUsers(userList, superUserList),
            0: exitProgram
        }
        
        options.get(choice, invalidChoice)()

if __name__ == "__main__":
    manual()
    clear()
    userList = []
    superUserList = []
    memorySystem = SystemMemory()
    loginMenu(userList, superUserList, memorySystem)
