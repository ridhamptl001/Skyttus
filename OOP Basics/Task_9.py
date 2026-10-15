
class Flight:
    def __init__(self, flight_name, total_seats):
        self.flight_name=flight_name
        self.total_seats=total_seats
        self.booked_seats=0

    def book_seat(self):
        if self.booked_seats<self.total_seats:
            self.booked_seats+=1
            print("Seat booked successfully.")
        else:
            print("Sorry, no seats available.")


    def display_seats(self):
        available = self.total_seats-self.booked_seats
        print("Flight:", self.flight_name)
        print("Available seats:", available)


flight1 = Flight("Air India", 2)

flight1.display_seats()
flight1.book_seat()
flight1.book_seat()
flight1.book_seat()
flight1.display_seats()
