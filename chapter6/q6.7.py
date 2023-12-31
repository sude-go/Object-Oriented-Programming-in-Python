class List:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self._data = list(initial_data)

    def __contains__(self, value):
        return value in self._data


test_list = List([1, 2, 3, 4, 5])
value_to_check = int(input("Enter the value to check: "))
present = test_list.__contains__(value_to_check)

if present:
    print(f"The value {value_to_check} is present in the list.")
else:
    print(f"The value {value_to_check} is not present in the list.")
