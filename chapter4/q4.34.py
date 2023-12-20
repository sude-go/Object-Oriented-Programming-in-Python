"""
Use list comprehension to create the list of values
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512].
"""

power_of_two_list = [2**i for i in range(10)]
print(power_of_two_list)
