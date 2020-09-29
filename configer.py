import json

class Config:
    def __init__(self, filename="config.json"):
        self.filename = filename
        with open(self.filename, 'r') as f:
            self.data = json.load(f)
    def getTheme(self):
        return self.data['theme']
    def getMusic(self):
        return self.data['music']
    def getSong(self):
        return self.data['song']
    
        



    