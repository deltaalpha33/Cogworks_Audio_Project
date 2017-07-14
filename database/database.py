class Database:
    
    """Contains all songs in a Python dictionary, whose key is the song ID
    and value is the corresponding Song object.
    """
    # global database

    def __init__(self):
        # global database = None
        self.database = None
        pass

    def add_songs(self, songs):
        """Add (a) song(s) to the database.

        Parameters
        ----------
        songs: array of songs to be added, still in mp3 file form
        """
        list_songs = None
        dict_songs = None # dictionary of songs to be added to existing database
        
        for i in range(len(songs)):
            list_songs = author_title_from_filename(s for s in songs)

        for i in range(len(list_songs) - 1):
            dict_songs[ list_songs[i] ] = list_songs[i + 1]

        self.database.update(dict_songs)
        
        pass

    def get_song(self, title):
        """Given song title, returns the Song object

        Parameters
        ----------
        info: String song name


        Returns
        -------
        song: desired Song object
        """
        song = None

        if self.find(title):
            song = self.database[title]
        else:
            raise Exception("Song not in database.")

        return song

    # TODO: make static?
    def switch(new_database):
        """Switches to new_database.

        Parameters
        ----------
        new_database: desired database to which to switch.
        """
        pass

    def remove(self, title):
        """Given song title, remove it from the database.
        
        Parameters
        ----------
        title: String of song name to be removed
        """
        if self.find(title):
            del self.database[title]
        else:
            raise Exception("Song not originally in database.")
        pass
    
    def find(self, title):

        """
        Given incomplete song information, searches dictionary for match. 

        Parameters
        ----------
        title: String of song name to search for

        
        Returns
        -------
        found: boolean denoting whether the song is in the database or not
        """
        found = False

        if len(title) == 0:
            raise Exception("Unspecified song information")
        else:
            
            if self.database.has_key(title): # song is a title in database
                found = True

        return founddatabase.items()
        return items
