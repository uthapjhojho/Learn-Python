import sys


#n = "{0:b}".format(input())
n = input()
print (len(max(bin(int(n))[2:].split('0'))))
#list function :
#len    : return length of the object
#max    : return maximum value of the list/array
#int    : convert from string to integer
#bin    : convert from integer to binary, [2:] --> disobey 2 first char
#split  : split('0') break the value if encounter '0' char
