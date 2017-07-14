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
<<<<<<< HEAD
        
        for i in range(len(songs)):
            list_songs = parse_fileName(s for s in songs)

        for i in range(len(list_songs) - 1):
            dict_songs[ list_songs[i] ] = list_songs[i + 1]

        database.update(dict_songs)
=======
>>>>>>> 1ad52ef9254970b2e0073026dadd9184a3035c7c
        
        for i in range(len(songs)):
           #  list_songs = parse_fileName(s for s in songs)
           # TODO: implement with song class functionality

        for i in range(len(list_songs) - 1):
            dict_songs[ list_songs[i] ] = list_songs[i + 1]

        database.update(dict_songs)
        
        pass

<<<<<<< HEAD
    def get_song(title):
=======
    def get_song(self, title):
>>>>>>> 1ad52ef9254970b2e0073026dadd9184a3035c7c
        """Given song title, returns the Song object

        Parameters
        ----------
        info: String song name


        Returns
        -------
        song: desired Song object
        """
        song = None

<<<<<<< HEAD
        if find(title):
=======
        song = None

        if find(title) == true:
>>>>>>> 1ad52ef9254970b2e0073026dadd9184a3035c7c
            song = database[title]
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
