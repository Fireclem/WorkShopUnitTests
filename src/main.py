#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
##
## File description:
## main
##

from miniProg import *
from sys import argv
from sys import exit

def error_handling(list):
    arg = []
    try:
        f = open(list, "r")
        arg = f.read().split('\n')
        f.close()
    except:
        sys.exit(84)
    try:
        for i in range (0, len(arg)):
            str(arg[i])
    except:
        sys.exit(84)
    return arg

def main():
    list = error_handling(sys.argv[1])
    if len(sys.argv) == 3:
        try:
            test = int(sys.argv[2])
            if test < 1:
                sys.exit(84)
        except:
            sys.exit(84)
    friends = parse_friends(list)
    adj_m = fill_adj(create_adj(len(friends)), friends)
    if len(argv) == 3:
        print_lists(friends)
        final_matrix = find_degrees(adj_m, int(argv[2]))
        print('')
        for i in range(0, len(final_matrix)):
            print(str(final_matrix[i]).strip('[]').replace(',', ''), sep = '\n')
    else:
        case = check_names(friends)
        final_matrix = find_relation(adj_m, case)
        if final_matrix[case[0]][case[1]] == 0 and argv[2] != argv[3]:
            final_matrix[case[0]][case[1]] = -1
        print("Degree of separation between {} and {}: {}".format(argv[2], argv[3], final_matrix[case[0]][case[1]]))
    exit(0)

main()