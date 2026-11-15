from day01_basics import total

orders = [
    {"id": 101, "status": "delivered", "total": 150, "city": "Riyadh"},
    {"id": 102, "status": "pending", "total": 80, "city": "Jeddah"},
    {"id": 103, "status": "delivered", "total": 200, "city": "Riyadh"},
    {"id": 104, "status": "cancelled", "total": 120, "city": "Dammam"},
    {"id": 105, "status": "delivered", "total": 50, "city": "Jeddah"},
]

def validate_order(order):
    required_fields = ["id", "status", "total", "city"]
    if not isinstance(order,dict):
        raise ValueError("Order must be a dictionary")

    for field in required_fields:
        if field not in order:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(order["status"], str):
        raise ValueError("Status must be a string")

    total =orders["total"]

    if(
        isinstance(total,bool)
        or not isinstance(total, (int, float))
        or total < 0
    ):
        raise ValueError(f"Invalid total for order {order['id']}")


def calculate_orders(orders,status="delivered"):
    return [
        order
        for order in orders
        if order["status"]==status
        ]
delivered=calculate_orders(orders)
print(delivered)

def calculate_revenue(orders):
    totals=[order["total"] for order in orders]
    return sum(totals)


print(calculate_revenue(delivered))


orders = [
    {"id": 1, "total": 100}
]

new_orders = orders.copy()

new_orders.append({"id": 2, "total": 200})

class DeliveryOrder:
    def __init__(self, status: str):
        self.status = status

    @property
    def is_delivered(self) -> bool:
        return self.status == "delivered"


order = DeliveryOrder("delivered")

print(order.is_delivered)