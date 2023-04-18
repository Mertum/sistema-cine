"""
This file contains the room seat configuration and handling of Seat class and data.
NOTE: Currently in development, this file is not used in the system production.
"""

class Seat:
    """This is the Seat class which is used to store seat data"""
    
    def __init__(self, row: int, column: int) -> None:
        """The constructor for Seat class"""
        self.row = row
        self.column = column
    
    def __str__(self) -> str:
        """The string representation of Seat class"""
        return f"Seat: {self.row}-{self.column}"
    
    def __repr__(self) -> str:
        """The representation of Seat class"""
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """The equality operator for Seat class"""
        return self.row == other.row and self.column == other.column
    
class SeatManager(Seat):
    """This is the SeatManager class which is used to manage seat data"""

    def __init__(self) -> None:
        """The SeatManager used to manage seat data"""
        self.__seats = \
            [[("🪑", False) for _ in range(10)] for _ in range(10)]
        self.__selected_seat = None

    def seat_availability(self) -> bool:
        """The method to check if seat is available"""
        for i, row in enumerate(self.__seats):
            print(f"{chr(i + 65)}", end="")
            for c, seat in enumerate(row):
                if seat[1]:
                    print(f"\033[91m{c}" + seat[0] + "\033[0m", end=" ")
                else:
                    print(f"\033[92m{c}" + seat[0] + "\033[0m", end=" ")
    
    def select_seat(self) -> None:
        """The method to select a seat in the room"""
        row_option = input("Select the row (A-J): ")
        row_index = ord(row_option.upper()) - 65
        column_option = input("Select the column (1-10): ") - 1

        if not self.__seats[row_index][column_option][1]:
            self.__selected_seat = (row_index, column_option)
            self.__seats[row_index][column_option] = ("🔒", True)
            print(f"You have been selected seat {row_option} | {column_option + 1}")
        else:
            print("Seat is not available, please select another seat")
            self.seat_availability()
    
    def get_selected_seat(self) -> tuple:
        """The method to get the selected seat"""
        return self.__selected_seat