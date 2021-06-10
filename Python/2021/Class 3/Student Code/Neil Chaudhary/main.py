def one():
  num = int(input("Enter a number: "))

  while (num <= 50 and num >= 0):
    num = int(input("Enter a number: "))

  print("Loop terminated")

def two():
  for i in range(0, 5):
    name = input("Enter your name: ")
    print(name)

def three():
  for i in range(1, 100):
    if (i % 4 == 0):
      print(i)
