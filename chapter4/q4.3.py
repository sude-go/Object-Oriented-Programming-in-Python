"""
Given an original list of integers intList create a list strList that
contains the associated string representations of those integers.
"""

intList = [4004, 8080, 6502, 8086, 68000, 80486]
strList = []

for i in intList:
    strList.append(str(i))

print(strList)

