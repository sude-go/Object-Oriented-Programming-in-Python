"""
The range function is only able to produce a list of integers. Given ﬂoating-
point values start, stop, and step, show how to create a list of ﬂoating-point values,
starting at start, taking steps of size step, going up to but not including or passing
stop. For example with start = 3.1, stop = 4.6, and step = 0.3, the result should be
the list [3.1, 3.4, 3.7, 4.0, 4.3].
"""


def generate_float_range(start, stop, step):
    result = []
    current_value = start

    while current_value < stop:
        result.append(current_value)
        current_value += step

    return result


result_list = generate_float_range(3.1, 4.6, 0.3)
print(result_list)
