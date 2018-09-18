import argparse
from S_circle import sqc
from S_triangle import sqt
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--figure', required=True, type=str, help="circle or triangle")
    parser.add_argument('--a', type=float, help="1st side of triangle")
    parser.add_argument('--b', type=float, help="2nd side of triangle")
    parser.add_argument('--c', type=float, help="3rd side of triangle")
    parser.add_argument('--r', type=float, help="Radius of circle")
    result = parser.parse_args()
    if result.figure == 'circle':
        print(sqc(result.r))
    elif result.figure == 'triangle':
        print(sqt(result.a, result.b, result.c))
    else:
        print("INVALID VALUE!")
