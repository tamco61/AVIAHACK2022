from data.driver import Driver
from data.road import Road
from data.point import Point
from data import db_session

import math


BUS_SPEED = 500 # met/min



def check_free_bus():
    session = db_session.create_session()
    free_drivers = session.query(Driver).filter(Driver.status == 0).all()
    free_drivers_on_50 = []
    free_drivers_on_100 = []

    return free_drivers_on_50, free_drivers_on_100


def find_bus_count(d50, d100, event):
    count = event.count
    count_100 = len(d100)
    count_50 = len(d50)
    n100 = 0
    n50 = 0

    if count_100 <= count // 100:
        n100 += count_100
        count_100 = 0
    else:
        n100 += count // 100
        count_100 -= n100
    count -= n100 * 100

    if count_50 <= count // 50:
        n50 += count_50
    else:
        if count_100 == 0:
            n50 = math.ceil(count / 50)
        elif 50 > count:
            n50 = 1
        elif count_50 >= 2:
            if abs(count - 50) > abs(count - 100):
                n50 = 2
            else:
                n100 += 1
    return n50, n100


def func(x, session, point_id):
    x = session.query(Road).filter(Road.source_point_id == x.point and Road.target_point_id == point_id).first().distance
    if not x:
        return 3
    else:
        return x / 500


def sort_for_low_distance(d50, d100, point_id):
    session = db_session.create_session()
    d50.sort(d50,
             key=lambda x:func(x, session, point_id))

    d100.sort(d100,
             key=lambda x: func(x, session, point_id))

    return d50, d100


def choice_bus(d50, d100, n50, n100):
    return d50[:n50], d100[:n100]




