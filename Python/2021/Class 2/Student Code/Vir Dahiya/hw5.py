print('Welcome Manager,set up an age limit and test out if the user is allowed to ride the soller coaster! ')
minimum = int(input("What is the minimum age: "))
maximum = int(input("What is the maximum age: "))
print('Nice! Now lets test it out...')
user = int(input('Write a random age to test out our system: '))
if user>minimum and user<maximum:
  print("You are welcome to ride the roller coaster!")
elif user<minimum:
  print("Sorry you are too young to ride!")
elif user>maximum:
  print("You are too old to ride!")


