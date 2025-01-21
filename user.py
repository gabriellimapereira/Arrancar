import random
import time

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
    def recordings(self):
        return self._recordings
    
    @property
    def likedSongs(self):
        return self._likedSongs

    def generateUniqueId(self, userList, superUserList):
        usedIds = {user._id for user in userList + superUserList}
        while True:
            newId = random.randint(0, 999)
            if newId not in usedIds:
                return newId
            
    def displayUser(self):
        print("nome: {} id: {}\n".format(self._name, self._id))

    def findRecording(self, name):
        for recording in self._recordings:
            if recording._name == name:
                return recording
        return None
    
    def removeRecording(self, recording):
        if recording in self._recordings:
            self._recordings.remove(recording)

    def likeSong(self, music):
        if music in self._likedSongs:
            time.sleep(1)
            print("música retirada da playlist de músicas curtidas!")
            self._likedSongs.remove(music)
        else:
            time.sleep(1)
            print("música adicionada à playlist de músicas curtidas!")
            self._likedSongs.append(music)

class SuperUser(User):
    def __init__(self, name, userList, superUserList, password):
        super().__init__(name, userList, superUserList)
        self._password = password

    @property
    def password(self):
        return self._password