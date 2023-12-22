class List:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self._data = list(initial_data)

    def replace(self, old, new):
        for i in range(len(self._data)):
            if self._data[i] == old:
                self._data[i] = new


my_list = List([1, 2, 3, 2, 4, 2, 5])
print("Original List:", my_list._data)

while True:
    old_value = int(input("Enter the old value you want to change: "))
    if old_value not in my_list._data:
        print(f"{old_value} is not in the list. Please enter a valid old value.")
    else:
        while True:
            new_value = int(input("Enter the new value you want to change: "))
            if new_value == old_value:
                print(f"{new_value} is the same as {old_value}. Please enter a different new value.")
            else:
                break

        my_list.replace(old_value, new_value)
        break

print(f"After replacing {old_value} with {new_value}:", my_list._data)
