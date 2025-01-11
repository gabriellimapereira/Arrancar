from audio import AudioArquive

class User():
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self._playLists = []
        self._likedSongs = []

class SuperUser(User):
    def __init__(self):
        super().__init__()