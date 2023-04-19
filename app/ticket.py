"""This file contains the Ticket development of the Cinema system"""

class Ticket:
    """
    The Ticket class represents a ticket for a movie in our cinema system

    Attributes:
        movie_name (str): The name of the movie
        ticket_type (str): The type of ticket
        seat_num (int): The seat number
    """
    
    def __init__(self, movie_name: str, ticket_type: str, seat_num: int) -> None:
        self.movie_name = movie_name
        self.ticket_type = ticket_type
        self.seat_num = seat_num
        self.price = self.calculate_price()
    
    def __str__(self) -> str:
        """The string representation of the Ticket object"""
        return f"({self.__class__.__name__}) -> {self.movie_name} {self.ticket_type} {self.seat_num}"
    
    def __repr__(self) -> str:
        """The representation of the Ticket object"""
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """Checks if two Ticket objects are equal"""
        return self.movie_name == other.movie_name \
            and self.ticket_type == other.ticket_type \
                and self.seat_num == other.seat_num
    
    def calculate_price(self) -> float:
        """Calculates the price of the ticket based on the ticket type"""
        if self.ticket_type == "regular":
            return 10.0
        elif self.ticket_type == "vip":
            return 20.0
        elif self.ticket_type == "3d":
            return 15.0
        else:
            raise ValueError(f"({self.__class__.__name__}) -> Invalid ticket type")