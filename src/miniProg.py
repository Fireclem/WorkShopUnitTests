#!usr/bin/env python3

import sys

def find_friends(friends, y, n):
    person = friends[y][n]
    friend_list = [person]
    for i in range(0, len(friends)):
        if (person == friends[i][0] and person != friends[i][1]):
            friend_list.append(friends[i][1])
        elif (person != friends[i][0] and person == friends[i][1]):
            friend_list.append(friends[i][0])
    return friend_list

def check_double(friends2, person):
    if not friends2:
        return 0
    for i in range(0, len(friends2)):
        if person == friends2[i][0]:
            return 1
    return 0

def insert_alpha(friends2, tmp):
    i = 0
    while i < len(friends2) and tmp[0] > friends2[i][0]:
        i += 1
    friends2.insert(i, tmp)

def parse_friends(list):
    friends = []
    friends2 = []
    for i in range(0, len(list)):
        if " is friends with " in list[i]:
            friends.append(list[i].split(" is friends with "))
    for y in range(0, len(friends)):
        if (check_double(friends2, friends[y][0]) == 0):
            tmp = find_friends(friends, y, 0)
            insert_alpha(friends2, tmp)
        if (check_double(friends2, friends[y][1]) == 0):
            tmp = find_friends(friends, y, 1)
            insert_alpha(friends2, tmp)
    return friends2

def create_adj(side):
    line = [0] * side
    tab = []
    for i in range(0, side):
        tab.append(list(line))
    return tab

def fill_adj(to_fill, friends):
    for i in range(0, len(friends)):
        for j in range(1, len(friends[i])):
            for k in range(0, len(friends)):
                if friends[k][0] == friends[i][j]:
                    to_fill[i][k] = 1
                    break
    return to_fill

def print_lists(friends):
    for i in range(0, len(friends)):
        print(friends[i][0])

def find_next_degrees(matrix, l, c, next_degree):
    for c2 in range(0, len(matrix)):
        if matrix[l][c2] == 1 and matrix[c2][c] == 0 and c2 != c:
            matrix[c2][c] = next_degree
    for l2 in range(0, len(matrix)):
        if matrix[l2][c] == 1 and matrix[l][l2] == 0 and l != l2:
            matrix[l][l2] = next_degree
    return matrix

def find_degrees(matrix, degree_lim):
    mem = 1
    for degree in range(1, degree_lim):
        if mem == 0:
            break
        mem = 0
        for l in range(0, len(matrix)):
            for c in range(0, len(matrix)):
                if matrix[l][c] == degree:
                    mem = 1
                    matrix = find_next_degrees(matrix, l, c, degree + 1)
    return matrix

def check_names(friends):
    check = [-1, -1]
    for i in range(0, len(friends)):
        if friends[i][0] == sys.argv[2]:
            check[0] = i
        if friends[i][0] == sys.argv[3]:
            check[1] = i
    if check[0] == -1 or check[1] == -1:
        print("Degree of separation between {} and {}: -1".format(sys.argv[2], sys.argv[3]))
        sys.exit(0)
    return check

def find_relation(matrix, case):
    mem = 1
    degree = 1
    while matrix[case[0]][case[1]] == 0:
        if mem == 0:
            break
        mem = 0
        for l in range(0, len(matrix)):
            for c in range(0, len(matrix)):
                if matrix[l][c] == degree:
                    mem = 1
                    matrix = find_next_degrees(matrix, l, c, degree + 1)
        degree += 1
    return matrix