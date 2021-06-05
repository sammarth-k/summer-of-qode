import sys

cups1 = input("How many cups of tea did you buy from shop 1: ")
cups2 = input("How many cups of tea did you buy from shop 2: ")

try:
    int(cups1)
    int(cups2)
except ValueError:
    print("\nPlease enter a valid whole number and try again.")
    sys.exit()

cups1 = int(cups1)
cups2 = int(cups2)

bill1 = cups1 * 15
bill2 = cups2 * 30

totalBill = bill1 + bill2

if cups1 or cups2 < 0:
    print("\nThe number of cups of tea that you buy should be positive!")
else:
    print("\nYour total bill to be paid is rupees", totalBill)