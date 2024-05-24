class ShoppingCartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    # Interface to decouple the concrete iterator implementation
    def get_iterator(self):
        return ShoppingCartIterator(self.items)

class ShoppingCartIterator:
    def __init__(self, items):
        self.items = items
        self.current_index = 0

   
    def has_next(self):
        return self.current_index < len(self.items)

    def next(self):
        if self.has_next():
            item = self.items[self.current_index]
            self.current_index += 1
            return item
        else:
             raise StopIteration() # Handle the end of iteration

# Example usage
cart = ShoppingCart()
cart.add_item(ShoppingCartItem("Apple", 1.50))
cart.add_item(ShoppingCartItem("Bread", 2.25))
cart.add_item(ShoppingCartItem("Milk", 3.75))

# Iterate and print item details or calculate total price
cart_iterator = cart.get_iterator()
while cart_iterator.has_next():
 item = cart_iterator.next()
 print(f"{item.name}: ${item.price}") # Or: total_price += item.price
