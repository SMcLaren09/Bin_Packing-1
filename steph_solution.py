#
# CSCI 338 Bin Packing Solution
# Authors: Stephanie McLaren
# 02/15/2016
#

def find_solution (rectangles, maxSize):
    rectangles = sorted(rectangles, reverse = True)
    placement = []
    upper_left_x = 0
    upper_left_y = 0

    for rectangle in rectangles:
        width = rectangle[0]
        coordinate = (upper_left_x, upper_left_y)
        placement.insert(0, coordinate)
        upper_left_x = upper_left_x + width

    return placement


    

