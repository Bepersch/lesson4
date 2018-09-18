import random


def rand(N):
    if N > 0:
        _count = 0
        for i in range(N):
            if int(random.random() * 100) % 2 == 0:
                _count += 1
        return str(_count / N * 100) + "%"
    else:
        return "INVALID VALUE!"
