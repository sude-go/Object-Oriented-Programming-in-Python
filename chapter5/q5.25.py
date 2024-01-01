def pair_sum(data, goal):
    seen = []

    for num in data:
        c = goal - num
        if c in seen:
            return True
        seen.append(num)
    return False


data_list = [5, 12, 3, 8, 12, 11, 2, 6]

print("pair sum data , 14: ", pair_sum(data_list, 14))
print("pair sum data , 24: ", pair_sum(data_list, 24))
print("pair sum data , 4: ", pair_sum(data_list, 4))
