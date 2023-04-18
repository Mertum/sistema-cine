"""
This module or file contains Ticket class with its attributes and methods and logic development
TODO: Check better ways to implement this module.
"""

from .constants import TICKETS
from .movie import Movie
from .seat import Seat

class Ticket:
    """The Ticket class which contains attributes and methods for the ticket object"""

    def __init__(self, _movie_title: str, seat: tuple[int, int], price: float) -> None:
        """The constructor of the Ticket class"""
        self.movie_title = _movie_title
        self.seat = seat
        self.price = price
    
    def __str__(self) -> str:
        """The string representation of the Ticket class"""
        return f"{self.movie_title} | {self.seat} | {self.price}"
    
    def __repr__(self) -> str:
        """Represents the Ticket class"""
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """Checks if two Ticket objects are equal"""
        if isinstance(other, Ticket):
            return self.movie_title == other.movie_title \
                and self.seat == other.seat \
                    and self.price == other.price
        return NotImplemented
    
    def __ne__(self, other: object) -> bool:
        """Checks if two Ticket objects are not equal"""
        if isinstance(other, Ticket):
            return not self.__eq__(other)
        return NotImplemented

class TicketManager(Ticket):
    """The TicketManager class which contains attributes and methods for the ticket manager object"""

    def __init__(self) -> None:
        """The constructor of the TicketManager class"""
        self._tickets = TICKETS

    def buy_tickets(self) -> None:
        """
        This method basically allows the user to buy tickets

        Args:
            This method takes no arguments
        
        Returns: -> None
        """
        selected_seat = Seat().select_seat()
        if selected_seat is None: 
            return
        selected_movie = Movie().get_selected_movie()
        ticket_price = selected_movie.price
        new_ticket = Ticket(selected_movie.title, selected_seat, ticket_price)
        self._tickets.append(new_ticket)
    
    def display_tickets_info(self) -> None:
        """
        This method displays the tickets information

        Args:
            This method takes no arguments
        
        Returns: -> None
        """
        print("Bought tickets information")
        for ticket in self._tickets:
            print(f"Movie: {ticket.movie_title} | Seat: {chr(ticket.seat[0] + 65)} | ${ticket.price}")