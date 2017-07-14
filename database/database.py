# from preconditions import preconditions

Class Database:
    
    """Contains all songs in a Python dictionary, whose key is the song name
    and value is the author.
    """
    private database # dictionary

    def __init__(self, dict):
        database = dict
        pass


    def add_songs(songs):
        """Add (a) song(s) to the database.

        Parameters
        ----------
        songs: array of songs to be added, still in mp3 file form
        """
        list_songs = None
        dict_songs = None # dictionary of songs to be added to existing database
        
        for i in range(len(songs)):
            list_songs = parse_fileName(s for s in songs)

        for i in range(len(list_songs) - 1):
            dict_songs[ list_songs[i] ] = list_songs[i + 1]

        database.update(dict_songs)
        
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

    def get_song(title):
        """Given song title, returns the title and author or asks for more information if not found

        Parameters
        ----------
        info: String song name


        Returns
        -------
        song: list of String title and author
        """
        song = None

        if find(title):
            song = [ title, database[title] ]
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
