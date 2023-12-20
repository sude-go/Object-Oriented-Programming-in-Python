"""
Hint: to properly line up the columns, you may rely upon the rjust method to right
justify strings. For example, the expression str(value).rjust(3) produces a string of
three characters with necessary leading spaces. For an n × n table, the maximum
number of characters needed for one entry will be len(str(n*n)).
"""


def generate_multiplication_table(n):
    max_width = len(str(n * n))

    header_row = " " * (max_width + 1) + "|"
    for i in range(1, n + 1):
        header_row += str(i).rjust(max_width)
    print(header_row)

    separator_line = "-" * (max_width + 1) + "+"
    separator_line += "-" * (max_width * n)
    print(separator_line)

    for i in range(1, n + 1):
        row = str(i).rjust(max_width) + "|"
        for j in range(1, n + 1):
            entry = (i * j)
            row += str(entry).rjust(max_width)
        print(row)


size = int(input("Enter the size of table: "))
generate_multiplication_table(size)
