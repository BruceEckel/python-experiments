from icecream import ic
from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == "__main__":
    ii = InventoryItem("Plumbus", 11.11, 70_000)
    ic(ii)
