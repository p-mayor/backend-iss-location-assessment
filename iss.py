#!/usr/bin/env python

import urllib
import turtle
import time

__author__ = 'peter mayor'


def turtleStart(lat, lon, time):
    '''plot indy dot, write passover time, plot iss location from lat,lon'''
    indy_lat = 40
    indy_lon = -87
    turtle.screen = turtle.Screen()
    turtle.screen.bgpic("map.gif")
    turtle.screen.register_shape("iss.gif")
    turtle.shape('iss.gif')
    turtle.setup(720, 360)
    turtle.setworldcoordinates(-180, -90, 180, 90)

    turtle.penup()
    turtle.goto(indy_lon, indy_lat)
    turtle.dot(10, 'yellow')

    turtle.write(time, font=("Arial", 16, "bold"))

    turtle.goto(lon, lat)
    turtle.done()


def get_astronauts():
    '''get astronaut data, print it, and create astronauts.json file'''
    url = 'http://api.open-notify.org/astros.json'
    filename = 'astronauts.json'
    urllib.urlretrieve(url, filename=filename)
    with open(filename, 'rw') as f:
        file_object = eval(f.read())
        for key, value in file_object.iteritems():
            print key, value


def get_iss_location():
    '''get iss current location and return lat, lon'''
    url = 'http://api.open-notify.org/iss-now.json'
    filename = 'iss-now.json'
    urllib.urlretrieve(url, filename=filename)
    with open(filename, 'rw') as f:
        file_object = eval(f.read())
        for key, value in file_object.iteritems():
            if key == 'iss_position':
                iss_lat = float(value['latitude'])
                iss_long = float(value['longitude'])
                return iss_lat, iss_long
            else:
                pass


def get_indy_passover_time(iss_lat, iss_lon):
    '''return indy passover time'''
    url = 'http://api.open-notify.org/iss-pass.json?lat=' +\
        str(iss_lat)+'&lon='+str(iss_lon)
    filename = 'iss-pass.json'
    urllib.urlretrieve(url, filename=filename)
    with open(filename, 'rw') as f:
        file_object = eval(f.read())
        for key, value in file_object.iteritems():
            print key, value
            if key == 'response':
                for item in value:
                    print item
                    return time.ctime(item['risetime'])
            else:
                pass


def main():
    '''get iss data and plot on map'''
    get_astronauts()
    iss_lat, iss_lon = get_iss_location()
    time = get_indy_passover_time(iss_lat, iss_lon)

    turtleStart(iss_lat, iss_lon, time)


if __name__ == '__main__':
    main()
