from pprint import pprint as pp

from flight import Flight
from airplanes import *
from helpers import *
f = Flight("LO124", AirbusA370())


def make_flight():
    f.allocate_passenger('leszek', '4B')
    f.allocate_passenger('kasia', '2A')
    # print (f.get_plane())
    # print(f.get_airline())
    # print(f.get_flight_number())

    f.relocate_passenger('2A', '3C')

    pp(f.seats)
    print(f.num_empty_seats())
    f.print_tickets(card_printer)

make_flight()