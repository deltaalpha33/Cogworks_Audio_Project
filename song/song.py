class Song:
    def __init__(self,author='Unknown',title='SongName',requencyDeltas):
        self.author = author
        self.title = title
        self.frequencyDeltas = frequencyDeltas
    def get_name(self):
        return self.author + " - " + self.title
