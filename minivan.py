#!/usr/bin/env python3
"""
Module Documentation Here
"""
from __future__ import print_function


def car_doors(states, gear):
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
    Return:
        openleft: Open Left Door (0 or 1)
        openright: Open Right Door (0 or 1)
    """
    openleft = 0
    openright = 0

    if states[3] and (gear == 'P') and states[0]:
        openleft = 1
    elif states[3] and (gear == 'P') and states[5]:
        openleft = 1
    elif states[3] and (gear == 'P') and states[4] and not states[2]:
        openleft = 1
    if states[3] and (gear == 'P') and states[1]:
        openright = 1
    elif states[3] and (gear == 'P') and states[7]:
        openright = 1
    elif states[3] and (gear == 'P') and states[6] and not states[2]:
        openright = 1


    return openleft, openright

def main():
    """
    Test your module
    """
    switches = [1, 0, 1, 1, 0, 0, 1, 0]
    shift = 'P'
    left, right = car_doors(switches, shift)
    print(left)
    print(right)


if __name__ == "__main__":
    main()
    exit(0)
