#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci = []
    if length == 0:
        fibonacci = []
    elif length == 1:
        fibonacci = [0]
    elif length == 2:
        fibonacci = [0, 1]
    elif length > 2:
        fibonacci = [0, 1]
        i = 2
        while i in range(length):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            i += 1

    print(fibonacci)
