"""This file contains the Seat development of the Cinema system"""

class Seat:
    """
    The Seat class represents the seats management in our cinema system
    
    Attributes:
        seat_num (int): The seat number
        is_booked (bool): The seat booking status
    """

    def __init__(self, seat_num: int) -> None:
        self.seat_num = seat_num
        self.is_booked = False
    
    def __str__(self) -> str:
        """
        The string representation of the Seat object

        Returns: -> str
        """
        return f"({self.__class__.__name__}) -> {self.seat_num}"
    
    def __repr__(self) -> str:
        """
        The representation of the Seat object

        Returns: -> str
        """
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """
        Checks if two Seat objects are equal

        Args:
            other (object): The other object to compare with.
        
        Returns: -> bool
        """
        return self.seat_num == other.seat_num