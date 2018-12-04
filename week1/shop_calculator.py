DISOCOUNT=0.9
num=int(input("Enter number of items"))
while (num<=0):
    print("Enter a positive number")
    num=int(input("Enter number of items"))
total=0.0
for i in range(0,num):
    price=float(input("Enter price of items"))
    total+=price
    print("price= ",price,"total= ",total)
if total>100:
    toatl=DISOCOUNT*tatol
print("total price of ", num, "item is ", total)
