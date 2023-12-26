class BinaryNumber:
    def __init__(self, binary_str):
        if not all(bit in '01' for bit in binary_str):
            raise ValueError("Invalid binary string")

        self.binary_str = binary_str

    def __add__(self, other):
        max_len = max(len(self.binary_str), len(other.binary_str))
        bin_sum = bin(int(self.binary_str, 2) + int(other.binary_str, 2))[2:].zfill(max_len)
        return BinaryNumber(bin_sum)

    def __sub__(self, other):
        max_len = max(len(self.binary_str), len(other.binary_str))
        bin_diff = bin(int(self.binary_str, 2) - int(other.binary_str, 2))[2:].zfill(max_len)
        return BinaryNumber(bin_diff)

    def __lt__(self, other):
        return int(self.binary_str, 2) < int(other.binary_str, 2)

    def __gt__(self, other):
        return int(self.binary_str, 2) > int(other.binary_str, 2)

    def __eq__(self, other):
        return self.binary_str == other.binary_str

    def __str__(self):
        return self.binary_str

    def __int__(self):
        return int(self.binary_str, 2)


binary_num1 = BinaryNumber('1101')
binary_num2 = BinaryNumber('1010')

print(binary_num1 + binary_num2)
print(binary_num1 - binary_num2)
print(binary_num1 < binary_num2)
print(binary_num1 > binary_num2)
print(binary_num1 == binary_num2)
print(str(binary_num1))
print(int(binary_num1))
