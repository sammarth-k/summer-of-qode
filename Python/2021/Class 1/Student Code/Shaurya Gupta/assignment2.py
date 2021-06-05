# 2 tea shops sell tea at the price of 15 and 30 rupees per cup. Input the number of cups a person buys from the first shop, then input the number of cups a person buys from the second shop and tell the customer the total bill.
priceOfFirstShop = 15
priceOfSecondShop = 30
items_bought_from_first_shop = int(input("How many tea cups will you buy from the first shop?: "))
items_bought_from_second_shop = int(input("How many tea cups will you buy from the second shop?: "))
bill = (items_bought_from_first_shop * 15) +  (items_bought_from_second_shop * 30)
print("Your bill is: ", bill)
