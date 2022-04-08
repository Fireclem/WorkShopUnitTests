#!/usr/bin/env python3

def sum(a, b):
    return a + b

def div(a, b):
    if b == 0:
        return "ERROR"
    else:
        return a / b

def calc(a, b, x, c):
    res = a * a * x + b * x + c
    return res

def concat(dest, src):
        return dest + src

def convertToInt(str):
    nb = int(str)
    return nb

def convertToFloat(toFloat):
    nb = float(toFloat)
    return nb

def convertToStr(nb):
    string = str(nb)
    return string

def createTab(elem1, elem2, elem3, elem4):
    tab = [elem1, elem2, elem3, elem4]
    return tab

print(createTab("salut", "coucou", 2, "mechant"))
print(convertToStr(22))
print("22")
print(22)
print(convertToFloat(22))
print(concat("coucou", " c'est moi!"))