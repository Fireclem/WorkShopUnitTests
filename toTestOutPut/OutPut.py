#!/usr/bin/env python3

def print(any):
    print(any)

def printCalc(nb, nb2, nb3):
    res = nb + nb2 / nb3
    print(res)

def printTab(ostr):
    list_ostr = list(ostr)
    tab = []
    nstr = []
    for i in range(ostr):
        if list_ostr[i] == ' ':
            tab.append(nstr)
            nstr.clear
        else:
            nstr += list_ostr[i]
    print(tab)