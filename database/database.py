# from preconditions import preconditions

class Database:
    
    """Contains all songs in a Python dictionary, whose key is the song name
    and value is the author.
    """

    def __init__(self):
        database = None
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
           #  list_songs = parse_fileName(s for s in songs)
           # TODO: implement with song class functionality

        for i in range(len(list_songs) - 1):
            dict_songs[ list_songs[i] ] = list_songs[i + 1]

        database.update(dict_songs)
        
        pass

    def get_song(self, title):
        """Given song title, returns the title and author or asks for more information if not found

        Parameters
        ----------
        info: String song name


        Returns
        -------
        song: list of String title and author
        """

        song = None

        if find(title) == true:
            song = [ title, database[title] ]
        else:
            raise Exception("Song not in database.")

        return song

    # TODO: make static?
    def switch(self, new_database):
        """Switches to new_database.

        Parameters
        ----------
        new_database: desired database to which to switch.
        """
        pass

    def remove(self, title):
        """Given song title, remove it from the database.
        @preconditions(database.contains(song)) # TODO: proper format
        
        Parameters
        ----------
        title: String of song name to be removed
        """
        del self[song]
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
            
            if database.has_key(title): # song is a title in database
                found = True

        return found

    def list(self):

        """Lists all items in database.

        Returns
        -------
        items: list of (key, value) tuple pairs for each element in database.
        """
        items = database.items()
        return items
