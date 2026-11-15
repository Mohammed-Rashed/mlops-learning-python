from delivery.order import DeliveryOrder
from delivery.service import *

order1 = DeliveryOrder(101,200.0,"delivered",10)
order2 = DeliveryOrder(102,90.0,"delivered",0)
order3 = DeliveryOrder(103,150.0,"delivered",0)

orders = [ order1,order2,order3]

summary = summarize_orders(orders)
print(summary)