"""
Lists support a method to count the number of times that a speciﬁed value
appears in a list. Show that you can compute such a count without relying upon that
method. Speciﬁcally, assume that you have a list collection and a target value. You
are to compute the number of times that the value appears in the given collection.
"""

collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
target = 1

count = 0
for item in collection:
    if item == target:
        count += 1

print(count)

