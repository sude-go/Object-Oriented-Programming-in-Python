class List:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self._data = list(initial_data)

    def count(self, value):
        return self._data.count(value)


test_list = List([1, 2, 3, 2, 4, 2, 5])
value_to_count = int(input("Enter the value to count: "))
count_result = test_list.count(value_to_count)
if count_result == 0:
    print(f"The value {value_to_count} is not present in the predefined list.")
else:
    print(f"The count of {value_to_count} in the predefined list is: {count_result}")
