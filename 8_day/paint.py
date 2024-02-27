import math

def print_area(h, w, c):
    area = float(h) * float(w)
    num_paint = math.ceil(area / c)
    print("You will need {} number of cans of paints".format(num_paint))

height = input("What is the height of the building? ")
width = input("What is the width of the building? ")
coverage = 5

print_area(h = height, w = width, c = coverage)