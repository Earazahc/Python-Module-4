#!/usr/bin/env python3
"""
Module Documentation Here
"""
from __future__ import print_function


def car_doors(left_dash, right_dash, child_lock, master_lock, left_inside,
              left_outside, right_inside, right_outside, gear):
    """
    Function recieves several input values to simulate
    the current state of a van. The values are checked
    to see if a door is trying to open and has the
    requirements to be unlocked.
    Args:
        states: A list with positions coresponding to the states
                of different system checks
            states[0]: Left Dashboard switch (0 or 1)
            states[1]: Right Dashboard switch (0 or 1)
            states[2]: Child Lock (0 or 1)
            states[3]: Master Lock (0 or 1)
            states[4]: Left Inside Handle (0 or 1)
            states[5]: Left Outside Handle (0 or 1)
            states[6]: Right Inside Handle (0 or 1)
            states[7]: Right Outside Handle (0 or 1)
        gear: Gear Shift Position (P, N, D, 1, 2, 3, or R)
    """
    states = [int(left_dash), int(right_dash), int(child_lock),
              int(master_lock), int(left_inside), int(left_outside),
              int(right_inside), int(right_outside)]


    print("Left dashboard switch (0 or 1): {}".format(left_dash))
    print("Right dashboard switch (0 or 1): {}".format(right_dash))
    print("Child lock switch (0 or 1): {}".format(child_lock))
    print("Master unlock switch (0 or 1): {}".format(master_lock))
    print("Left inside handle (0 or 1): {}".format(left_inside))
    print("Left outside handle (0 or 1): {}".format(left_outside))
    print("Right inside handle (0 or 1): {}".format(right_inside))
    print("Right outside handle (0 or 1): {}".format(right_outside))
    print("Gear shift position (P, N, D, 1, 2 ,3, or R): {}".format(gear))
    #test gear is valid

    if gear not in ("P", "N", "D", "1", "2", "3", "R"):
        print("Invalid Record: Both doors stay closed")
        return


    openleft = 0
    openright = 0

    # Test left door
    if states[3] and (gear == 'P') and states[0]:
        openleft = 1
    elif states[3] and (gear == 'P') and states[5]:
        openleft = 1
    elif states[3] and (gear == 'P') and states[4] and not states[2]:
        openleft = 1

    # Test right door
    if states[3] and (gear == 'P') and states[1]:
        openright = 1
    elif states[3] and (gear == 'P') and states[7]:
        openright = 1
    elif states[3] and (gear == 'P') and states[6] and not states[2]:
        openright = 1

    # Test gear
    if gear != "P":
        print("Both doors stay closed")
        return

    if openleft and openright:
        print("Both doors open")
        return
    elif openleft:
        print("Left door opens")
        return
    elif openright:
        print("Right door opens")
        return
    else:
        print("Both doors stay closed")
        return


def main():
    """
    Test your module
    """
    #switches = [1, 0, 1, 1, 0, 0, 1, 0]
    #shift = "P"
    car_doors(1, 0, 1, 1, 0, 0, 1, 0, "P")


if __name__ == "__main__":
    main()
    exit(0)
