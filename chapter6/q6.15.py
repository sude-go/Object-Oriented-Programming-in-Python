class Set:
    def __init__(self):
        self._contents = []

    def add(self, value):
        if value not in self._contents:
            self._contents.append(value)

    def discard(self, value):
        if value in self._contents:
            self._contents.remove(value)

    def __contains__(self, value):
        return value in self._contents


my_set = Set()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print(1 in my_set)
print(4 in my_set)

my_set.discard(2)

print(2 in my_set)
