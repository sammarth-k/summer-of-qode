price = int(input("How many chocolates do you want"))
chocolates =  10

if(price>chocolates):
  print(price,"chocolates are not available")
else:
  print(price,"chocolates are available")
  cost = 15
  print(int(cost*price),"is the price of the chocolates")
