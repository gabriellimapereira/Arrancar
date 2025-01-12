from audio import AudioArquive
import random

class User():
    def __init__(self, name, userList, superUserList):
        self._name = name
        self._id = self.generateUniqueId(userList, superUserList)
        self._playLists = []
        self._likedSongs = []
        self._recordings = []

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id
    
    @property
    def linkedSongs(self):
        return self._likedSongs

    def generateUniqueId(self, userList, superUserList):
        usedIds = {user._id for user in userList + superUserList}
        while True:
            newId = random.randint(0, 9999)
            if newId not in usedIds:
                return newId
            
    def displayUser(self):
        print("nome: {} id: {}\n".format(self._name, self._id))

class SuperUser(User):
    def __init__(self, name, userList, superUserList, password):
        super().__init__(name, userList, superUserList)
        self._password = password

    @property
    def password(self):
        return self._password