while True:
  age1 = input("Enter your age: ")
  
  def is_float(age1):
    try:
      age1 = float(age1)

      if age1 > 100:
        print("You have already crossed the age of 100!")
      elif age1 <= 0:
        print("You are not born yet!")
      elif age1 == 100:
        print("You are 100 years old!")
      else:
        yearsLeft = float(100 - age1)
        print(f"You have {yearsLeft} years left till you turn 100 years old!")

    except ValueError:
      print("Please enter a valid number!")

  is_float(age1)