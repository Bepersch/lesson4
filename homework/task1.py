import argparse
from randgen import rand
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', required=True, type=int, help="Count of numbers")
    result = parser.parse_args()
    print(rand(result.N))
