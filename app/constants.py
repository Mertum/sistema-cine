"""Constants for the app."""

from .seat import Seat
from .movie import Movie

class Constants:

    MOVIES = [
        Movie("The Matrix", "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", 136),
        Movie("The Lord of the Rings: The Fellowship of the Ring", "A meek hobbit of the Shire and eight companions set out on a journey to Mount Doom to destroy the One Ring and the dark lord Sauron.", 178),
        Movie("Forrest Gump", "The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate and other historical events unfold through the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.", 142)
    ]

    REGULAR_SEATS = [Seat(i) for i in range(1, 51)]

    VIP_SEATS = [Seat(i) for i in range(51, 61)]
    
    SEATS_3D = [Seat(i) for i in range(61, 71)]