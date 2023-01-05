class Product:
    def __init__(self,
                 title: str = "Surprise",
                 price: float = 0.0,
                 description: str = "Some stuff"):
        if price < 0.0:
            raise ValueError('price must not be negative')

        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f'Product: \"{self.title}\", ' \
                f'{self.description}, ' \
                f'{self.price} UAH, '


class Customer:

    def __init__(self,
                 name: str,
                 surname: str,
                 email: str):
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return f'Customer: {self.name} {self.surname}, email: {self.email}'


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.products = dict()

    def add_product(self, product: Product, amount: int):
        if not isinstance(product, Product):
            raise TypeError('There is no such products')
        if not isinstance(amount, int):
            raise TypeError('Amount of products must be an integer number')
        if amount <= 0:
            raise ValueError('Amount of products must be positive')
        whole_amount = amount + self.products.get(product, 0)
        self.products[product] = whole_amount

    def summary(self):
        return sum(product.price * self.products[product] for product in self.products)

    def __str__(self):
        result = 'Your order is: '
        for product in self.products:
            result += f'{self.products[product]}x ' \
                      f'{product.title}; '
        return result


me = Customer("Pavlo", "Kostianov", "pasha.k460@gmail.com")
ps5 = Product("SONY Play Station 5", 600, "A home video game console developed by Sony Interactive Entertainment")
nintendo_switch = Product("NINTENDO Switch", 300, "A hybrid video game console developed by Nintendo")

my_order = Order(me)
my_order.add_product(nintendo_switch, 3)
my_order.add_product(ps5, 1)
print(my_order)
print("Summary -> ", my_order.summary())
