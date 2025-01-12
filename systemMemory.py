class SystemMemory:
    def __init__(self):
        self._musics = [] 
        self._podcasts = []  
        self._soundEffects = []

    @property
    def musics(self):
        return self._musics
    
    @property
    def podcasts(self):
        return self._podcasts
    
    @property
    def soundEffects(self):
        return self._soundEffects

    def addMusic(self, newMusic):
        self.musics.append(newMusic)

    def addPodcast(self, newPodcast):
        self.podcasts.append(newPodcast)

    def addSoundEffect(self, newEffect):
        self.soundEffects.append(newEffect)

    def findAudioByName(self, list, name):
        for audio in list:
            if audio._name == name:
                return audio
        return None