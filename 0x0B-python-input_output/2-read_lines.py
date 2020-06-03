#!/usr/bin/python3
"""Module for read_lines method"""


def read_lines(filename="", nb_lines=0):
    """
    Method that reads n lines of a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as my_file_0:
        lineNum = 0
        while True:
            line = my_file_0.readline()
            if not line:
                print("")
                break
            print(line, end="")
            lineNum += 1
            if (lineNum == nb_lines):
                break
