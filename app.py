from pprint import pprint as pp

class Flight:
    def __init__(self, flight_number, airplane):
        self.flight_number = flight_number
        self.airplane = airplane
        rows, seats = airplane.get_seating_plan()
        self.seats = [{seat: None for seat in seats} for row in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_flight_number(self):
        return self.flight_number[2:]

    def get_plane(self):
        return self.airplane.get_name()

    def _parse_seat(self, seat):
        rows, letters = self.airplane.get_seating_plan()

        letter = seat[-1]
        if letter in letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"invalid seat number: {row_text}")

        if row not in rows:
            raise ValueError(f"Seat number is out of range")

        return row, letter


    def allocate_passenger(self, passenger='Pawel Konior', seats='23A'):
        row, letter = self._parse_seat(self)

    def relocate_passenger(selfself, from_seat, to_seat):
        pass


class Plane:
    def get_num_seats(self):
        row, seats = self.get_seating_plan()
        return len(row) * len(seats)


class AirBusA370(Plane):
    def get_name(self):
        return "AirBusA370"

    def get_seating_plan(self):
        return range(25), "ABCDEG"


class Boeing777(Plane):
    def get_name(self):
        return "Boeing777"

    def get_seating_plan(self):
        return range(40), "ABCDEGHIK"


f = Flight("LO124", AirBusA370())
# print (f.get_plane())
# print(f.get_airline())
# print(f.get_flight_number())
pp(f.seats)