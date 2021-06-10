x=10
y=15
wanted = int(input("enter number: "))
if (wanted>x):
  print("sorry we only have ten chocolates")
else:
  print ("Available, calculating bill... ")
  Total = (wanted*15)
  print ("Your bill is", (Total), "rupees")