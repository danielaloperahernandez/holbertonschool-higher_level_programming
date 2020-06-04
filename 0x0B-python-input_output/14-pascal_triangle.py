#!/usr/bin/python3
def pascal_triangle(n):
    list_pascal = [[1], [1, 1]]

    for row in range(1, n-1):
        line = [1]
        for elem in range(0, len(list_pascal[row])-1):
            line.extend([list_pascal[row][elem] + list_pascal[row][elem+1]])
        line += [1]
        list_pascal.append(line)
    return list_pascal
