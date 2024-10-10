class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock


class Order:
    def __init__(self, order_id, user, products):
        self.order_id = order_id
        self.user = user
        self.products = products
        self.status = "pending"


class Payment:
    def __init__(self, order, amount, payment_method):
        self.order = order
        self.amount = amount
        self.payment_method = payment_method
