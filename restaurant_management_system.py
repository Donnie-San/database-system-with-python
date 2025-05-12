import functools

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Action: {func.__name__} was performed.")
        return func(*args, **kwargs)
    return wrapper

class Dish:
    def __init__(self, name, price, category):
        self._name = name
        self._price = price
        self._category = category

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f"{self._name} ({self._category}) - ${self._price}"

    def __repr__(self):
        return f"Dish({self._name}, {self._price}, {self._category})"

class Customer:
    def __init__(self, name):
        self._name = name
        self._orders = []

    def place_order(self, order):
        if len(self._orders) < 5:
            self._orders.append(order)
        else:
            print("Order limit reached!")

    def __len__(self):
        return len(self._orders)

class VIPCustomer(Customer):
    def place_order(self, order):
        self._orders.append(order)

class Order:
    def __init__(self, customer):
        self._customer = customer
        self._dishes = []

    @log_action
    def add_dish(self, dish):
        self._dishes.append(dish)

    @log_action
    def remove_dish(self, dish):
        if dish in self._dishes:
            self._dishes.remove(dish)
        else:
            print(f"{dish} is not in the order!")

    def show_order(self):
        print(f"\nOrder for {self._customer._name}:")
        for dish in self._dishes:
            print(dish)

    @staticmethod
    def is_available(dish, menu):
        return dish in menu

    @classmethod
    def generate_order(cls, customer, dish_names, menu):
        order = cls(customer)
        for dish in menu:
            if dish._name in dish_names:
                order.add_dish(dish)
        return order

def main():
    menu = [
        Dish("Lasagna", 14.99, "Italian"),
        Dish("Pizza", 23.99, "Italian"),
        Dish("Sushi", 18.99, "Japanese"),
        Dish("Crumpets", 6.49, "British")
    ]

    customer1 = Customer("Donnie")
    customer2 = VIPCustomer("Jacob")

    order1 = Order.generate_order(customer1, ["Lasagna", "Sushi"], menu)
    order2 = Order.generate_order(customer2, ["Pizza", "Crumpets"], menu)

    customer1.place_order(order1)
    customer2.place_order(order2)

    order1.show_order()
    order2.show_order()

if __name__ == '__main__':
    main()