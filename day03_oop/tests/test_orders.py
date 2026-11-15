
import pytest

from delivery.order import DeliveryOrder
from delivery.service import summarize_orders


def test_order_is_delivered():
    order = DeliveryOrder(101, 120.0,"delivered")
    order.mark_delivered()

    assert order.is_delivered is True


def test_order_summary():
    orders = [
        DeliveryOrder(101, 100.0, "delivered"),
        DeliveryOrder(102, 200.0, "delivered"),
        DeliveryOrder(103, 50.0, "cancelled")
    ]

    result = summarize_orders(orders)

    assert result["total_orders"] == 3
    assert result["delivered_orders"] == 2
    assert result["delivered_revenue"] == 300.0
    assert result["average_delivered_order"] == 150.0


def test_negative_amount():
    with pytest.raises(ValueError):
        DeliveryOrder(104, -50.0)


def test_cancelled_order_cannot_be_delivered():
    order = DeliveryOrder(105, 75.0, "cancelled")

    with pytest.raises(ValueError):
        order.mark_delivered()
