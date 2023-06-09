"""This file contains the Movie development of the Cinema system"""

class Movie:
    """The Movie class represents a movie in our cinema system"""

    def __init__(self, name: str, description: str, duration: int) -> None:
        self.name = name
        self.description = description
        self.duration = duration
        self.__showtimes = []
    
    def __str__(self) -> str:
        """
        The string representation of the Movie object

        Returns: -> str
        """
        return f"({self.__class__.__name__}) -> {self.name} - {self.duration} minutes"
    
    def __repr__(self) -> str:
        """
        The representation of the Movie object
        
        Returns: -> str
        """
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """
        Checks if two Movie objects are equal

        Args:
            other (object): The other object to compare with.
        
        Returns: -> bool
        """
        return self.name == other.name
    
    def add_showtime(self, showtime: str) -> None:
        """
        Adds a showtime to the movie

        Args:
            showtime (str): The showtime to add
        
        Returns: -> None
        """
        self.__showtimes.append(showtime)

    def get_showtimes(self) -> list:
        """
        Returns a list of the showtimes for the movie

        Returns: -> list
        """
        return self.__showtimes