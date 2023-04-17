"""
    This module contains the Movie class which is used to store movie data
    NOTE: Currently in development 🏓
"""

from .movies import MOVIES as movies

class Movie:
    """
    The Movie class, used to store all movie data

    Attributes:
        title (str): The title of movie
        rating (str): The rating of movie
        duration (str): The duration of movie
        seats (int): The number of seats available
        price (float): The price of movie ticket
    
    References: None
    """

    __selected_movie = None

    def __init__(self, title: str, rating: str, duration: str, seats: int, price: float) -> None:
        """The constructor for Movie class"""
        self.title = title
        self.rating = rating
        self.duration = duration
        self.seats = seats
        self.price = price
    
    def __str__(self) -> str:
        """The string representation of Movie class"""
        return f"Movie: {self.title} ({self.rating}) - {self.duration} - ${self.price} | Seats: {self.seats}"
    
    def __repr__(self) -> str:
        """The representation of Movie class"""
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """The equality operator for Movie class"""
        return self.title == other.title

    @property
    def title(self) -> str:
        """The Movie title"""
        return self.__title
    
    @property
    def rating(self) -> str:
        """The Movie rating"""
        return self.__rating
    
    @property
    def duration(self) -> str:
        """The Movie duration"""
        return self.__duration
    
    @property
    def seats(self) -> int:
        """The Movie seats"""
        return self.__seats
    
    @property
    def price(self) -> float:
        """The Movie price"""
        return self.__price | int(self.__price)
    
    # Movie logical methods in this section.

    def display_movie_info(self) -> None:
        """
            This method displays the movie information
            Args: None
            Returns: -> None
        """
        print('Available movies in our system')
        for index, movie in enumerate(movies):
            print(f"[{index + 1}] {movie['title']} ({movie['rating']}) - {movie['duration']}")
    
    def select_movie(self) -> None:
        """
            This method selects the movie from the user input
            Args: None
            Returns: -> None
        """
        self.display_movie_info()
        option = int(input('Select a movie: '))
        self.__selected_movie = movies[option - 1]
        print(f"You selected {self.__selected_movie['title']}")
    
    def get_selected_movie(self) -> dict:
        """
            This method returns the selected movie
            Args: None
            Returns: -> dict
        """
        return self.__selected_movie