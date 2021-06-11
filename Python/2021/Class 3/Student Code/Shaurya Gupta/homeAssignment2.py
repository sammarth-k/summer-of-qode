count = 0
nameArray = []
while count < 5:
    name = input("Enter your name: ")

    nameArray.append(name)
    count += 1


for i in range(0,5):
    print(nameArray[i])
