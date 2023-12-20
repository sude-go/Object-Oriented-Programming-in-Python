"""
0
3
"""

foods = ['eggs', 'broccoli', 'peas', 'salt', 'steak']

for k in range(len(foods) - 1):
    if len(foods[k]) < len(foods[k + 1]):
        print(k)
