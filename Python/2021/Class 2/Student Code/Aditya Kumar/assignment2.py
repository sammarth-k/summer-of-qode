numOfChocolates = int(input("How many chocolates do you want: "))
if numOfChocolates <= 10:
    print("We have enough chocolates for you :D")
    bill = numOfChocolates * 15
    print(f'Your total bill will be {bill} rupees.')
elif numOfChocolates > 10:
    print("We don't have enough chocolates for you D:")
else: print("I don't understand")
