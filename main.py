from user import User, SuperUser
from systemMemory import SystemMemory
import userMenu

userList = []
superUserList = []
memorySystem = SystemMemory()

def loginUser():
    userId = int(input("digite seu id de usuário: "))
    for user in userList:
        if user.id == userId:
            print(f"login bem-sucedido para o usuário {user._name}!")
            userMenu.menuUsuario(user, memorySystem)
            return user
    print("id de usuário não encontrado!")
    return None

def loginSuperUser():
    userId = int(input("digite seu id de super usuário: "))
    password = input("digite sua senha: ")
    for superUser in superUserList:
        if superUser.id == userId and superUser.password == password:
            print(f"login bem-sucedido para o super usuário {superUser.name}!")
            userMenu.menuSuperUsuario(superUser, memorySystem)
            return superUser
    print("id ou senha de super usuário incorretos!")
    return None

def registerUser():
    choice = None

    while choice not in {"0", "1"}:
        choice = input("você quer registrar um usuário comum ou um super usuário? (0 ou 1): ")
        if choice not in {"0", "1"}:
            print("entrada inválida. digite 0 para usuário comum ou 1 para super usuário!\n")

    if choice == "0":
        name = input("digite o seu nome como usuário: ")
        newUser = User(name, userList, superUserList)
        print("usuário cadastrado! o seu id é:", newUser.id, ". não se esqueça dele!\n")
        userList.append(newUser)
    else:
        name = input("digite o seu nome como super usuário: ")
        password = input("agora digite a senha. se lembre da senha, ou caso contrário, é F: ")
        newUser = SuperUser(name, userList, superUserList, password)
        print("usuário cadastrado! o seu id é:", newUser.id, ". não se esqueça dele!\n")
        superUserList.append(newUser)

def deleteUser():
    print("você escolheu apagar o registro de um usuário")

def listUsers():
    for i in userList:
        i.displayUser()
    for i in superUserList:
        i.displayUser()

def exitProgram():
    print("saindo do sistema...")
    exit()

def invalidaChoice():
    print("opção inválida. por favor, tente novamente.")

def loginMenu():
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
        opcoes = {
            1: loginUser,
            2: loginSuperUser,
            3: registerUser,
            4: deleteUser,
            5: listUsers,
            0: exitProgram
        }
        opcoes.get(choice, invalidaChoice)()

if __name__ == "__main__":
    loginMenu()
