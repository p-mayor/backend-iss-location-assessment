#!/usr/bin/env python

import urllib

__author__ = 'peter mayor'


def main():
    print('hi')
    # if not os.path.exists(str(dest_dir)):
    #     os.mkdir(dest_dir)
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
            print key, value


if __name__ == '__main__':
    main()
