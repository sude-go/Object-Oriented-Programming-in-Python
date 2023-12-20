"""
Write a code fragment that processes a list items and prints out all values
that occur more than once on the list. Take care to only print out each such value
once. For example, given the list
items = ['apple', 'grape', 'kiwi', 'kiwi', 'pear',
'grape', 'kiwi', 'strawberry']
your program should print
grape
kiwi
(or kiwi, grape; either order will suffice).
"""

items = ['apple', 'grape', 'kiwi', 'kiwi', 'pear', 'grape', 'kiwi', 'strawberry']
more_than_once = []

for item in items:
    if items.count(item) > 1:
        if item not in more_than_once:
            more_than_once.append(item)
print(more_than_once)
