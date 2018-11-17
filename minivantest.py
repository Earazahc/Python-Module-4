#!/usr/bin/env python3
"""
Module Documentation Here
"""
from __future__ import print_function
from urllib.request import urlopen
from minivan import car_doors


def test_doors():
    """
    Opens up the web file
    Grabs the car_doors function from module 1
    and tells whether the car door is open or not
    :Params: nothing
    :Returns: nothing
    """
    url_test = urlopen('http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv')
    url_list = [line.decode('utf-8').strip('\n') for line in url_test]
    #delete the top line of file which is title of columns
    url_list.remove('H1, LD, RD, CL, ML, LI, LO, RI, RO, GS')

    num = 1

    for item in url_list:
        print("Reading Record {}:".format(num))
        #split up each of the items in the list
        item_list = item.split(", ")
        #delete the first value which is a row identifier
        item_list.remove("R1")
        car_doors(*item_list)
        print()
        num = num + 1


def main():
    """
    Test your module
    """
    test_doors()


if __name__ == "__main__":
    main()
    exit(0)
