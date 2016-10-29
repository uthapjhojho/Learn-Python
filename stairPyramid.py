from __future__ import print_function
import sys

class stairCase:
    n = 0

    def __init__(number):
        n = number

    def StairCase1():
        for i in range(n):
            for j in range(n-i, 0, -1):
                print ("#", end="")

            for k in range(0, i):
                print (" ", end="")

            print ('')

    def StairCase2():
        for i in range(n):
            for j in range(0, i+1):
                print ("#", end="")

            for k in range(n-1, i, -1):
                print (" ", end="")

            print ('')

    def StairCase3():
        for i in range(n):
            for j in range(n-i, 0, -1):
                print (" ", end="")

            for k in range(0, i):
                print ("#", end="")

            print ('')

    def StairCase4():
        for i in range(n):
            for j in range(0, i+1):
                print (" ", end="")

            for k in range(n-1, i, -1):
                print ("#", end="")

            print ('')

    n = input("input N : ")
    #print (sys.version)
    objStair = StairCase(n)
    objStair.StairCase1()
    objStair.StairCase2()
    objStair.StairCase3()
    objStair.StairCase4()
