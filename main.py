from user import User, SuperUser
from systemMemory import SystemMemory
import userMenu

userList = []
superUserList = []
memorySystem = SystemMemory()

def loginUser():
    userId = int(input("Digite seu ID de usuário: "))
    for user in userList:
        if user.id == userId:
            print(f"\nLogin bem-sucedido para o usuário {user._name}!")
            userMenu.menuUsuario(user, memorySystem)
            return user
    print("\nID de usuário não encontrado. Tente novamente!")
    return None

def loginSuperUser():
    userId = int(input("Digite seu ID de super usuário: "))
    password = input("Digite sua senha: ")
    for superUser in superUserList:
        if superUser.id == userId and superUser.password == password:
            print(f"\nLogin bem-sucedido para o super usuário {superUser.name}!")
            userMenu.menuSuperUsuario(superUser, memorySystem)
            return superUser
    print("\nID ou senha de super usuário incorretos! Tente novamente!")
    return None

def registerUser():
    choice = None
    while choice not in {"0", "1"}:
        choice = input("\nVocê quer registrar um usuário comum ou um super usuário? (0 para comum / 1 para super usuário): ")
        if choice not in {"0", "1"}:
            print("\nEntrada inválida. Digite 0 para usuário comum ou 1 para super usuário!\n")

    if choice == "0":
        name = input("\nDigite o seu nome como usuário: ")
        newUser = User(name, userList, superUserList)
        print(f"\nUsuário cadastrado! O seu ID é: {newUser.id}. Não se esqueça dele!\n")
        userList.append(newUser)
    else:
        name = input("\nDigite o seu nome como super usuário: ")
        password = input("Agora digite a senha. Se lembre dela, ou será F: ")
        newUser = SuperUser(name, userList, superUserList, password)
        print(f"\nUsuário cadastrado! O seu ID é: {newUser.id}. Não se esqueça dele!\n")
        superUserList.append(newUser)

def deleteUser():
    choice = None
    while choice not in {"0", "1"}:
        choice = input("\nvocê deseja apagar um usuário comum (0) ou um super usuário (1)? ")
        if choice not in {"0", "1"}:
            print("entrada inválida. digite 0 para usuário comum ou 1 para super usuário!")

    userId = int(input("\ndigite o id do usuário que deseja apagar: "))

    if choice == "0":  
        for user in userList:
            if user.id == userId:
                userList.remove(user)
                print(f"\nusuário comum com id {userId} foi apagado com sucesso!")
                return
        print("\nid de usuário comum não encontrado. tente novamente!")
    else: 
        for superUser in superUserList:
            if superUser.id == userId:
                superUserList.remove(superUser)
                print(f"\nsuper usuário com id {userId} foi apagado com sucesso!")
                return
        print("\nid de super usuário não encontrado. tente novamente!")


def listUsers():
    print("\nLista de Usuários Comuns:")
    if userList:
        for i in userList:
            i.displayUser()
    else:
        print("Não há usuários comuns cadastrados.")
    
    print("\nLista de Super Usuários:")
    if superUserList:
        for i in superUserList:
            i.displayUser()
    else:
        print("Não há super usuários cadastrados.")

def exitProgram():
    print("\nSaindo do sistema... Até logo!")
    exit()

def invalidChoice():
    print("\nOpção inválida. Por favor, tente novamente.")

def loginMenu():
    print("\nBem-vindo(a) ao Arrancar!\nDê uma arrancada na sua vida!")
    while True:
        print("\nSelecione uma opção:")
        print("1 - Entrar como usuário comum")
        print("2 - Entrar como super usuário")
        print("3 - Registrar-se como usuário (ou super usuário)")
        print("4 - Apagar registro de usuário")
        print("5 - Listar todos os usuários")
        print("0 - Sair")
        
        try:
            choice = int(input("\nDigite sua escolha: "))
        except ValueError:
            choice = -1
            
        options = {
            1: loginUser,
            2: loginSuperUser,
            3: registerUser,
            4: deleteUser,
            5: listUsers,
            0: exitProgram
        }
        
        options.get(choice, invalidChoice)()

if __name__ == "__main__":
    loginMenu()

