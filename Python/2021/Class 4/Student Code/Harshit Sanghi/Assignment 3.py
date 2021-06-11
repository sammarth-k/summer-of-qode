import random
numbers = [0, 1, 1, 2, 2, 3, 8, 5, 8, 14, 21, 14, 34,]
nums = []
i = 0
while i < 5:
    x = random.sample(numbers, 1)
    nums.append(x)
    i += 1
print(f"The list with possible duplicates is {nums}")
for num in nums:
    if nums.count(num) > 1:
        print(f"The number {num} has {nums.count(num)-1} duplicate/duplicates.")
        nums.remove(num)
print(f"The list of numbers without duplicates is {nums}.")
