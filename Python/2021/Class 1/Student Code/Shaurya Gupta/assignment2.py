# 2 tea shops sell tea at the price of 15 and 30 rupees per cup. Input the number of cups a person buys from the first shop, then input the number of cups a person buys from the second shop and tell the customer the total bill.
price_first_shop = 15
price_second_shop = 30

items_first_shop = int(input("How many tea cups will you buy from the first shop?: "))
items_second_shop = int(input("How many tea cups will you buy from the second shop?: "))

if items_first_shop > 100 or items_second_shop > 100:
    print("that's too much tea, don't you think")
elif items_second_shop <0 or items_second_shop < 0:
    print("no")
    items_second_shop =1
    items_first_shop = 2

bill = (items_first_shop * price_first_shop) +  (items_second_shop * price_second_shop)

print("......................................................\n" "Your bill is: ", bill)
