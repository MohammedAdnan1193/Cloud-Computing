# Cloud-Computing
IN THE CART FILE:
The changes were made to improve correctness, security, and clarity in the code. First, the constructor _init_ was fixed to __init__ for proper object initialization. The load method was updated to a @classmethod to enable the creation of Cart objects directly from dictionaries. To handle contents safely, eval was replaced with json.loads, eliminating the security risk of executing arbitrary code. The typing.List annotation was used for type hints, ensuring better code readability and static type checking.

Additionally, error handling was introduced in get_cart to gracefully skip invalid JSON entries. The contents list was transformed into a list of Product objects using a cleaner and more Pythonic list comprehension. These changes ensure the code is more secure, robust, and maintainable while adhering to best practices.


IN THE BROWSE FILE:
The changes primarily focus on improving correctness, clarity, and safety in the code. First, I fixed the constructor by changing _init_ to __init__, ensuring the Product class initializes properly. The load method was updated to a @classmethod so it can create Product instances directly from a dictionary, improving usability. Additionally, I handled cases where dao.get_product might return None by returning None gracefully, updating the type hint to Optional[Product] to reflect this behavior.

To make the code safer and cleaner, I replaced data['qty'] with data.get('qty', 0) to avoid crashes when the key is missing. I also simplified list_products by using a list comprehension to reduce verbosity. These changes ensure better error handling, more robust default values, and cleaner code structure without altering functionality.
