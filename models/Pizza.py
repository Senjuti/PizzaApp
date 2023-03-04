toppings_map = {
    'bacon': 3,
    'chicken': 2,
    'onion': 1,
    'pepper': 1,
    'pepperoni': 2,
    'mushroom': 1
}

size_map = {
    'S': 5,
    'M': 10,
    'L': 15,
    'XL': 20
}

BASE_PRICE = 5


class Pizza:
    def __init__(self, size: str):
        self.size = size_map.get(size)
        self.price = self._calculate_price()

    def __repr__(self) -> str:
        return f'<Pizza:size={self.size},price={self.price}>'

    def _calculate_price(self) -> int:
        return BASE_PRICE + self.size
