#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from math import sqrt


def infinite_sum(x, check, num):
    eps = 10 ** -7
    a = 1
    summa = 1
    i = 1
    prev = 0
    while abs(summa - prev) > eps:
        prev = summa
        numerator = 1
        denominator = 1
        for j in range(1, i + 1):
            if 2 * j - 3 > 0:
                numerator *= 2 * j - 3
            denominator *= 2 * j
        temp = (numerator / denominator) * x**i
        if (-1) ** (i + 1) > 0:
            summa += temp
        else:
            summa -= temp
        i += 1
    print(f"Calculated sum: {num} is: {summa}")
    print(f"Verification sum: sqrt(1+({x})) = {check}")


if __name__ == '__main__':
    checksum1 = sqrt(1 - 0.8)
    thread1 = Thread(target=infinite_sum, args=(-0.8, checksum1, 1))
    thread1.start()
    checksum2 = sqrt(1 - 0.4)
    thread2 = Thread(target=infinite_sum, args=(-0.4, checksum2, 2))
    thread2.start()
    checksum3 = sqrt(1 - 0.5)
    thread2 = Thread(target=infinite_sum, args=(-0.5, checksum3, 3))
    thread2.start()
