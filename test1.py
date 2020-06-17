#!/usr/bin/env python3
print("Hello World")
for x in range(10):
    print(x)

filename =str(input('Enter file: '))
handle = open(filename, 'r')
for line in handle:
	print(line)

