
#A certain shop has 10 chocolates. Input the number of chocolates required 
#by the user and return true if those many chocolates are available (false otherwise). 
# If available, tell the total price (each chocolate costs 15 rupees).
var1= True
var2= False
chocolates = int(input("enter the number chocolates you want to buy:"))
if chocolates <= 10:
    print(var1)
    bill = chocolates*15
    print( bill, "is your bill")

else: 
    print(var2)




