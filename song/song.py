class Song:
    def __init__(self):
        self.author = 'unknown'
        self.title = 'unknown'
        self.frequencyDeltas = []
    def __init__(self,frequencyDeltas, author,title):
        self.author = author
        self.title = title
        self.frequencyDeltas = frequencyDeltas

    def get_name(self):
        return self.author + " - " + self.title
    def author_title_from_filename(self,filename):
        """sets title and author from a filename

        Parameters
        ----------
        filename: the string name of the file. (not the path)

        Returns
        -------
        Nothing
        """
        filename = filename.replace('.mp3','')
        filename = filename.replace('_',' ')
        parts = filename.split(' - ')
        self.author = parts[0]
        self.title = parts[1]