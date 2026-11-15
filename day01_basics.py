print("hello word")
order_price = 250
delivery_fee = 15
discount = 30

total = order_price + delivery_fee - discount
print(total)

if total > 200:
    print("You have to pay for delivery")
elif total < 200:
        print("You don't have to pay for delivery")
else:
    print("Standerd delivery fee applies")



order_prices=[100,1, 1, 50, 400]
for order in order_prices:
    total = total + order
    print("total order: ",total)


while total < 1000:
    total = total + 100
    print("total order: ",total , " less than 1000")


order_prices = [100, 250, 80, 300, 150]
total_price= 0
for order_price in order_prices:
    if order_price > 150:
        total_price= total_price + order_price
print("total price: ", total_price)


for i in range(10):
    print(i)