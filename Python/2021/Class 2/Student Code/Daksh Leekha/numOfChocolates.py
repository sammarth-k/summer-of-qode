chocolates = 10
to_buy = int(input("How many chocolates would you like to buy?"))

if to_buy <= chocolates:
    print(f"We have exactly {chocolates} to buy! You are buying {to_buy} of them!")
elif to_buy < 0:
    print("You cannot buy negative number of chocolates!")
elif to_buy == 0:
    print("Why are you here if you don't want to buy chocolates? SHOOOOOOO!")
