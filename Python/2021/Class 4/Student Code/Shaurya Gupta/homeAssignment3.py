import random

# creating a random array of alphabets


List = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]
random_list = []
count = 0
while count < random.randrange(15, 30):
    count += 1
    random_list.append(List[random.randint(0, len(List) - 1)])
print(random_list, "is the random array")


# getting 5 random numbers


count = 0
final_numbers = []
while count < 5:
    count+=1
    random_num = random.randint(0, len(random_list) -1)
    final_numbers.append(random_list[random_num])

#getting the duplicates


duplicates = []
print(final_numbers, "are 5 random numbers from the array")
for i in random_list:

    if random_list.count(i) >1:
        duplicates.append(i)
print(duplicates, "are the duplicates")
