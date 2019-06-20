#!/usr/bin/env python

import urllib

__author__ = 'peter mayor'

import turtle
import time


def turtleStart(x, y):
    turtle.screen = turtle.Screen()
    turtle.screen.bgpic("map.gif")
    turtle.screen.register_shape("iss.gif")
    turtle.shape('iss.gif')
    turtle.screen.update()

    turtle.penup()
    turtle.goto(-40*4, 87)
    turtle.dot(10, 'yellow')

    turtle.goto(x*4, y)

    turtle.end_fill()

    turtle.done()


def main():

    url_1 = 'http://api.open-notify.org/astros.json'
    filename_1 = 'astronauts.json'
    urllib.urlretrieve(url_1, filename=filename_1)
    with open(filename_1, 'rw') as f:
        file_object = eval(f.read())
        for key, value in file_object.iteritems():
            print key, value

    url_2 = 'http://api.open-notify.org/iss-now.json'
    filename_2 = 'iss-now.json'
    urllib.urlretrieve(url_2, filename=filename_2)
    with open(filename_2, 'rw') as f:
        file_object = eval(f.read())
        for key, value in file_object.iteritems():
            if key == 'iss_position':
                iss_lat = float(value['latitude'])
                iss_long = float(value['longitude'])
            else:
                pass
            print key, value

    url_3 = 'http://api.open-notify.org/iss-pass.json?lat=' +\
        str(iss_lat)+'&lon='+str(iss_long)
    filename_3 = 'iss-pass.json'
    urllib.urlretrieve(url_3, filename=filename_3)
    with open(filename_3, 'rw') as f:
        file_object = eval(f.read())
        for key, value in file_object.iteritems():
            print key, value
            if key == 'response':
                print value
                for item in value:

                    print item
                    print time.ctime(item['risetime'])
            else:
                pass

    turtleStart(iss_lat, iss_long)


if __name__ == '__main__':
    main()
