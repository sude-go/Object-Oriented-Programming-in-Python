"""
Exercise 4.38: Given a list orig, possibly containing duplicate values, show how to use list
comprehension to produce a new list uniq that has all values from the original but
with duplicates omitted. Hint: look for indices at which the leftmost occurrence of a
value occurs.
"""

orig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
uniq = []
# uniq = [orig[i] for i in range(len(orig)) if orig[i] not in orig[i + 1:]]

for i in range(len(orig)):
    if orig[i] not in orig[i + 1:]:
        uniq.append(orig[i])
print(uniq)
