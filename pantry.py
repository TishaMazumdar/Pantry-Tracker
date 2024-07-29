class Pantry:
    def __init__(self, item_name, quantity, category, expiry_date) -> None:
        self.item_name = item_name
        self.quantity = quantity
        self.category = category
        self.expiry_date = expiry_date

    def __repr__(self) -> str:
        return f"{self.item_name}, {self.quantity}, {self.category}, {self.expiry_date}"