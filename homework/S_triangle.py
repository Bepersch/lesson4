import math


def sqt(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            return "Square of triangle: " + str(math.sqrt((p * (p - a) * (p - b) * (p - c))))
        else:
            return "A triangle with such sides does not exist"
    else:
        return "INVALID VALUE!"
