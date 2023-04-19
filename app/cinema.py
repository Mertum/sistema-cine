"""The cinema file contains the all Cinema system logic"""

from .ticket import Ticket
from .seat import Seat
from .movie import Movie
from .constants import Constants

class Cinema:
    """The Cinema class which contains the cinema system"""

    def __init__(self) -> None:
        self.movies = Constants.MOVIES
        self.tickets = []
        self.seats = { 
            "Regular": Constants.REGULAR_SEATS, 
            "VIP": Constants.VIP_SEATS, 
            "3D": Constants.SEATS_3D 
        }
    
    def get_movies(self) -> list[Movie]:
        """Returns a list of all the available movies"""
        return self.movies
    
    def get_seats(self, ticket_type: str) -> list[Seat]:
        """Returns a list of all the available seats for a given ticket type"""
        return self.seats[ticket_type]

    def buy_ticket(self, movie_name: str, ticket_type: str, seat_num: int) -> Ticket:
        """This method allow buys a ticket for a movie"""
        movie = None
        for m in self.movies:
            if m.name == movie_name:
                movie = m
                break
        if not movie:
            raise ValueError("Invalid movie name")
        seats = self.seats[ticket_type]
        seat = None
        for s in seats:
            if s.seat_num == seat_num:
                seat = s
                break
        if not seat: raise ValueError("Invalid seat number")
        if seat.is_booked: raise ValueError("Seat is already booked")
        ticket = Ticket(movie_name, ticket_type, seat_num)
        self.tickets.append(ticket)
        seat.is_booked = True
        return ticket