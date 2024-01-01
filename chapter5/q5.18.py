"""
output will be like:
start silly
5
start funny
10
start goofy
11
end goofy
end funny
start goofy
4
end goofy
end silly
"""


def silly(x):
    print('start silly')
    print(x)
    funny(2 * x)
    goofy(x - 1)
    print('end silly')


def funny(y):
    print('start funny')
    print(y)
    goofy(y + 1)
    print('end funny')


def goofy(z):
    print('start goofy')
    print(z)
    print('end goofy')


silly(5)
