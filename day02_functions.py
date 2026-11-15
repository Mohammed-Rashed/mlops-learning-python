# locations = (24.9, 67.1, 12.5, 45.3, 78.9)
#
# print("locations: ", locations[0])
#
# statuses = ["pending", "delivered", "pending"]
#
# unique_statuses = set(statuses)
#
# print(len(unique_statuses))
#
#
# def calculate_tax(price, tax_rate=0.15):
#     tax = price * tax_rate
#     return tax
#
# #
# # def validate_order(total):
# #     if total < 0:
# #         raise ValueError("Order cannot be negative")
# #     else:
# #         return total
# #
# # try:
# #     result = validate_order(-100)
# #     print(result)
# #
# # except ValueError as error:
# #     print("Error:", error)
#
# orders = [
#     {"id": 101, "status": "delivered", "total": 150, "city": "Riyadh"},
#     {"id": 102, "status": "pending", "total": 80, "city": "Jeddah"},
#     {"id": 103, "status": "delivered", "total": 200, "city": "Riyadh"},
#     {"id": 104, "status": "cancelled", "total": 120, "city": "Dammam"},
#     {"id": 105, "status": "delivered", "total": 50, "city": "Jeddah"},
# ]
#
# def filter_orders_by_status(orders,status):
#     return [
#         order
#         for order in orders
#         if order["status"] == status
#     ]
#
# delivered=filter_orders_by_status(orders, "delivered")
# print("delivered orders: ", delivered)




def validate_total(total):
    if total < 0:
        raise ValueError("Total cannot be negative")

    return total
try:
    result = validate_total(-100)
    print(result)
except ValueError as error:
    print("Error:", error)
