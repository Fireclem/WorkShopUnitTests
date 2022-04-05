#!/usr/bin/env python3

def sum(a, b):
    return a + b

def div(a, b):
    if b == 0:
        return "ERROR"
    else:
        return a / b

def concat(dest, src):
    if int(dest):
        return dest + src
    else:
        return dest

def convertToInt(str):
    nb = int(str)
    return nb

def convertToFloat(toFloat):
    nb = float(toFloat)
    return nb