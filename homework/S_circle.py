import math


def sqc(r):
    if r > 0:
        return "Square of circle: " + str(math.pi * r ** 2)
    else:
        return "INVALID VALUE!"
