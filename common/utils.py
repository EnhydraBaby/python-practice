#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
#求一元二次方程解
def quadratic(a, b, c):
    delta = pow(b,2) - 4 * a * c
    base = 2 * a
    if delta < 0 :
        return
    elif delta == 0 :
        return -b / base, -b / base
    if delta > 0 :
        deltaSqrt = math.sqrt(delta)
        x1 = (-b + deltaSqrt) / base
        x2 = (-b - deltaSqrt) / base
        return x1, x2

