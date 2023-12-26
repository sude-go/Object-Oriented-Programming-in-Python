class SortedSet:
    def __init__(self):
        self._contents = []

    def add(self, value):
        if value not in self._contents:
            self._contents.append(value)
            self._contents.sort()

    def discard(self, value):
        if value in self._contents:
            self._contents.remove(value)

    def __contains__(self, value):
        return value in self._contents

    def __str__(self):
        return str(self._contents)


# Example usage:
my_sorted_set = SortedSet()

my_sorted_set.add(3)
my_sorted_set.add(1)
my_sorted_set.add(2)

print(my_sorted_set)

my_sorted_set.discard(2)

print(my_sorted_set)
