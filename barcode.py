#!/usr/bin/env python3
"""
Module Documentation Here
"""
from __future__ import print_function


def print_digit(dig):
    """
    Prints the digit to bard code.
    :params: d:zip code passed in from printBarCode
    :Returns: ............
    """

    sum_d = 0
    dig = int(dig) #this is the zip code as an int

    #Add up all the digits

    while dig:
        sum_d += dig % 10
        dig //= 10

    #Sum a multiple of 10
    check = 10 - (sum_d % 10)

    if check == 10:
        check = 0

    if check == 1:
        check = "00011"
    elif check == 2:
        check = "00101"
    elif check == 3:
        check = "00110"
    elif check == 4:
        check = "01001"
    elif check == 5:
        check = "01010"
    elif check == 6:
        check = "01100"
    elif check == 7:
        check = "10001"
    elif check == 8:
        check = "10010"
    elif check == 9:
        check = "10100"
    elif check == 0:
        check = "11000"

    return check


def print_barcode(zip_c):
    """
    Validates the input
    Parses the numbers
    Calls printDigit to print the zip code numbers
    as well as the checkDigit
    :Params: zip:zip code passed in from module 4
    :Returns: Nothing
    """

    if not zip_c.isdigit():
        print("Error!!! Zipcode is not a number")
        return
    if len(zip_c) != 5:
        print("Error!!! Zipcode needs to be 5 digits")
        return

    zip_code = zip_c
    change = ""

    #call the printDigit function
    check = print_digit(zip)

    #loop through the zip_code
    for num in zip_code:
        if num == "1":
            change += "00011"
        elif num == "2":
            change += "00101"
        elif num == "3":
            change += "00110"
        elif num == "4":
            change += "01001"
        elif num == "5":
            change += "01010"
        elif num == "6":
            change += "01100"
        elif num == "7":
            change += "10001"
        elif num == "8":
            change += "10010"
        elif num == "9":
            change += "10100"
        elif num == "0":
            change += "11000"


    change += check

    #Print the bar code

    print("|", end="")
    for integer in change:
        if integer == "0":
            print(":", end="")
        if integer == "1":
            print("|", end="")
    print("|")


def main():
    """
    Test your module
    """
    print_barcode("542")


if __name__ == "__main__":
    main()
    exit(0)
