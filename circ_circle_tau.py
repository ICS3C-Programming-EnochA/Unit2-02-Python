#!/usr/bin/env python3
# Created By: Enoch Amedjrovi
# 26 February 26, 2025
# These program asks the user for the radius of a circle in mm. It then calculates and displays the circumference using tau.
import constants


def main():
    # get teh radius from the uer
    radius = float(input("enter radius (mm): "))
    # calculate the circumference
    circumference = constants.TAU * radius
    # display the circumference
    print("The circumference is {}mm".format(circumference))


if __name__ == "__main__":
    main()
