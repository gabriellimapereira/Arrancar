import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" 

from user import User, SuperUser
from systemMemory import SystemMemory
import userMenu

def loginUser(userList, memorySystem):
    userId = int(input("digite seu id de usuário: "))
    for user in userList:
        if user.id == userId:
            print(f"\nlogin bem-sucedido para o usuário {user._name}!")
            userMenu.menuUsuario(user, memorySystem)
            return user
    print("\nid de usuário não encontrado. tente novamente!")
    return None

def loginSuperUser(superUserList, memorySystem):
    userId = int(input("digite seu id de super usuário: "))
    password = input("digite sua senha: ")
    for superUser in superUserList:
        if superUser.id == userId and superUser.password == password:
            print(f"\nlogin bem-sucedido para o super usuário {superUser.name}!")
            userMenu.menuSuperUsuario(superUser, memorySystem)
            return superUser
    print("\nid ou senha de super usuário incorretos! tente novamente!")
    return None

def registerUser(userList, superUserList):
    choice = None
    while choice not in {"0", "1"}:
        choice = input("você quer registrar um usuário comum ou um super usuário? (0 para comum / 1 para super usuário): ")
        if choice not in {"0", "1"}:
            print("entrada inválida. digite 0 para usuário comum ou 1 para super usuário!")

    if choice == "0":
        name = input("digite o seu nome como usuário: ")
        newUser = User(name, userList, superUserList)
        print(f"usuário cadastrado! o seu id é: {newUser.id}. não se esqueça dele!")
        userList.append(newUser)
    else:
        name = input("digite o seu nome como super usuário: ")
        password = input("agora digite a senha. se lembre dela, ou será f: ")
        newUser = SuperUser(name, userList, superUserList, password)
        print(f"usuário cadastrado! o seu id é: {newUser.id}. não se esqueça dele!")
        superUserList.append(newUser)

def deleteUser(userList, superUserList):
    choice = None
    while choice not in {"0", "1"}:
        choice = input("você deseja apagar um usuário comum (0) ou um super usuário (1)? ")
        if choice not in {"0", "1"}:
            print("entrada inválida. digite 0 para usuário comum ou 1 para super usuário!")

    userId = int(input("digite o id do usuário que deseja apagar: "))

    if choice == "0":  
        for user in userList:
            if user.id == userId:
                userList.remove(user)
                print(f"usuário comum com id {userId} foi apagado com sucesso!")
                return
        print("id de usuário comum não encontrado. tente novamente!")
    else: 
        for superUser in superUserList:
            if superUser.id == userId:
                superUserList.remove(superUser)
                print(f"super usuário com id {userId} foi apagado com sucesso!")
                return
        print("id de super usuário não encontrado. tente novamente!")

def listUsers(userList, superUserList):
    print("lista de usuários comuns:")
    if userList:
        for i in userList:
            i.displayUser()
    else:
        print("não há usuários comuns cadastrados.")
    
    print("lista de super usuários:")
    if superUserList:
        for i in superUserList:
            i.displayUser()
    else:
        print("não há super usuários cadastrados.")

def exitProgram():
    print("saindo do sistema... até logo!")
    exit()

def invalidChoice():
    print("opção inválida. por favor, tente novamente!")

def loginMenu(userList, superUserList, memorySystem):
    print("bem-vindo(a) ao arrancar!\ndê uma arrancada na sua vida!")
    while True:
        print("\nselecione uma opção:")
        print("1 - entrar como usuário comum")
        print("2 - entrar como super usuário")
        print("3 - registrar-se como usuário (ou super usuário)")
        print("4 - apagar registro de usuário")
        print("5 - listar todos os usuários")
        print("0 - sair")
        
        try:
            choice = int(input("\ndigite sua escolha: "))
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
    userList = []
    superUserList = []
    memorySystem = SystemMemory()
    loginMenu(userList, superUserList, memorySystem)
