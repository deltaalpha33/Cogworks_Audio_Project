Class Database:
    
    """Contains all songs in a Python dictionary, whose key is the song name
    and value is the author. Mapped to the file name.
    """
    private database # dictionary

    def __init__(self):
        pass


    def add_song(song):
        """Add a song to the database.

        Parameters
        ----------
        song: array of string title and author, already parsed, to be added
        """
        
    
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

        pass

    def load_song(info):
        """Given either the song title and/or author, returns the song or asks
        for more information.

        Parameters
        ----------
        info: array of size 1 or 2 containing information about the song
        """

        pass

    def switch(new_database):
        """Switches to new_database.

        Parameters
        ----------
        new_database: desired database to which to switch.
        """
        pass

    def remove(song):
        pass

    def find(song):
        pass

    def list():
        pass
