#!/usr/bin/env python3
"""
Module Documentation Here
"""
from __future__ import print_function
from urllib.request import urlopen
from barcode import print_barcode


def test_barcode():
    """
    Opens up the web file
    Grabs the print_barcode function from module 3
    and prints the barcode for a valid zipcode
    and a wrning if zip is invalid
    :Params: nothing
    :Returns: nothing

    """
    url_test = urlopen('http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt')
    url_line = [line.decode('utf-8').strip('\n') for line in url_test]
    for item in url_line:
        print('Enter a zipcode: ' + item)
        print_barcode(item)
        print('\n')


def main():
    """
    Test your module
    """
    test_barcode()


if __name__ == "__main__":
    main()
    exit(0)
