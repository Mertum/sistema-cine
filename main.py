"""This is the main file for the project."""

from app.cinema import Cinema

def main() -> None:
    """This is the main function for the project."""
    cinema = Cinema()

    # Display the available movies
    print("Available movies:")
    for movie in cinema.get_movies():
        print(movie.name)
    
    # Ask the user to select a movie
    movie_name = input("Select a movie: ")

    # Display the available ticket types
    print("Available ticket types: regular, vip, 3d")

    # Ask the user to select a ticket type
    ticket_type = input("Select a ticket type: ")

    # Display the available seats for the selected ticket type
    print("Available seats:")
    for seat in cinema.get_seats(ticket_type):
        if not seat.is_booked:
            print(seat.seat_num)
        else:
            print("X")
    
    # Ask the user to select a seat
    seat_num = int(input("Select a seat number: "))

    # Buy the ticket and display the details
    try:
        ticket = cinema.buy_ticket(movie_name, ticket_type, seat_num)
        print("Ticket purchased:")
        print("- Movie:", ticket.movie_name)
        print("- Ticket type:", ticket.ticket_type)
        print("- Seat number:", ticket.seat_num)
        print("- Price:", ticket.price)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()