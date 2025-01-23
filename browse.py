from products import dao
from typing import List, Optional


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        """Initialize a Product instance."""
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict):
        """Load a Product object from a dictionary."""
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data.get('qty', 0)
        )


def list_products() -> List[Product]:
    """Retrieve all products."""
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Optional[Product]:
    """Retrieve a product by its ID."""
    product_data = dao.get_product(product_id)
    if product_data is None:
        return None
    return Product.load(product_data)


def add_product(product: dict):
    """Add a new product."""
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Update the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative.')
    dao.update_qty(product_id, qty)
