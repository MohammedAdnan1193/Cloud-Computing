import json
from typing import List
from cart import dao
from products import Product


class Cart:
    def _init_(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @classmethod
    def load(cls, data: dict):
        """Load a Cart object from a dictionary."""
        contents = [Product(**product) for product in json.loads(data['contents'])]
        return cls(data['id'], data['username'], contents, data['cost'])


def get_cart(username: str) -> List[Product]:
    """Retrieve the cart for a user."""
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []
    
    items = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail['contents'])
        except json.JSONDecodeError:
            continue  # Skip invalid entries
        
        items.extend(contents)
    
    return [products.get_product(item_id) for item_id in items]


def add_to_cart(username: str, product_id: int):
    """Add a product to the user's cart."""
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """Remove a product from the user's cart."""
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """Delete the user's entire cart."""
    dao.delete_cart(username)