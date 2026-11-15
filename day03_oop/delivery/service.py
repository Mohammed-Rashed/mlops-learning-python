from delivery.order import DeliveryOrder

def summarize_orders(
        orders:list[DeliveryOrder]
)-> dict[str,int|float]:

    delivered_orders= [
        order for order in orders
        if order.is_delivered
    ]
    total = sum(order.amount for order in delivered_orders)

    count = len(delivered_orders)

    average = total / count if count > 0 else 0.0

    highAmount=max(order.amount for order in delivered_orders)
    return {
        "total_orders":len(orders),
        "delivered_orders":len(delivered_orders),
        "delivered_revenue":total,
        "average_delivered_order": average,
        "highest_delivered_amount":highAmount
    }