# from preconditions import preconditions

Class Database:
    
    """Contains all songs in a Python dictionary, whose key is the song name
    and value is the author. Mapped to the file name.
    """
    private database # dictionary

    def __init__(self, dict):
        database = dict
        pass


    def add_songs(songs):
        """Add (a) song(s) to the database.

        Parameters
        ----------
        songs: dictionary of key title and value author to be added
        """
        database.update(songs)
        
        pass


    def parse_fileName(song):
        """Parse a song filename to return an array of the title and author.
    
        Parameters
        ----------
        song: filename, in mp3 format, to be parsed


        Returns
        -------
        info: array of two elements: song title, and author
        """
        # TODO: implement
        pass

    def load_song(title):
        """Given song title, returns the song or asks for more information.

        Parameters
        ----------
        info: String song name


        Returns
        -------
        song: filename retrieved from dictionary
        """

        if find(title):
            pass # TODO: implement
        else:
            raise Exception("Song not in database.")
        pass

    def switch(new_database):
        """Switches to new_database.

        Parameters
        ----------
        new_database: desired database to which to switch.
        """
        pass

    def remove(title):
        """Given song title, remove it from the database.
        @preconditions(database.contains(song)) # TODO: proper format
        
        Parameters
        ----------
        title: String of song name to be removed
        """
        del database[song]
        pass
    
    def find(title):

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

    def list():

        """Lists all items in database.

        Returns
        -------
        items: list of (key, value) tuple pairs for each element in database.
        """
        items = database.items()
        return items
