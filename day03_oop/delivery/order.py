

class DeliveryOrder:
    ALLOWED_STATUSES = ("pending", "delivered", "cancelled")
    def __init__(
            self,
            order_id:int,
            amount:float,
            status: str = "delivered",
            discount:int=0
                 )-> None:
        if amount < 0:
            raise ValueError("amount cannot be negative")

        if status not in self.ALLOWED_STATUSES:
            raise ValueError("invalid status")

        self.order_id = order_id
        self.amount = amount
        self.status = status
        if discount>0:
            self.apply_discount(discount)


    @property
    def is_delivered(self) -> bool:
        return self.status == "delivered"

    def mark_delivered(self) -> None:
        if self.status == "cancelled":
            raise ValueError(
                "cancelled order cannot be delivered"
            )

        self.status = "delivered"

    def apply_discount(self , percentage) -> None:
        discount=self.amount/100*percentage
        amountAfterDiscount = self.amount-discount
        self.amount=amountAfterDiscount
