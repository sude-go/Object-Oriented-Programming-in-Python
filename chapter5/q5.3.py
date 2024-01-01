nums = []
num = int(input("Enter a number: "))
nums.append(num)
while num != 0:
    print(num)
    num = int(input("Enter a number: "))
    nums.append(num)
nums.remove(0)
print(nums)
average = sum(nums) / len(nums)
print(average)
