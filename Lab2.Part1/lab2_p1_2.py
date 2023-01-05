from typing import List


class Pizza:
    def __init__(self, name: str, price: float, ingredients: List[str]):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self) -> str:
        return f"{self.name} (${self.price})"


class PizzaOrder:
    def __init__(self, pizza: Pizza, extra_ingredients: List[str]):
        self.pizza = pizza
        self.extra_ingredients = extra_ingredients
        self.total_price = pizza.price + len(extra_ingredients) * 0.5

    def __str__(self) -> str:
        extra_ingredient_string = ", ".join(self.extra_ingredients)
        return f"{self.pizza}: +${len(self.extra_ingredients) * 0.5} " \
               f"for extra ingredients ({extra_ingredient_string}). Total: ${self.total_price}"


def get_pizza_of_the_day(day_of_week: str) -> Pizza:
    if day_of_week == "Monday":
        return Pizza("Margherita", 10.0, ["tomato sauce", "mozzarella"])
    elif day_of_week == "Tuesday":
        return Pizza("Pepperoni", 12.0, ["tomato sauce", "mozzarella", "pepperoni"])
    elif day_of_week == "Wednesday":
        return Pizza("Vegetarian", 11.0, ["tomato sauce", "mozzarella", "mushrooms", "bell peppers"])
    elif day_of_week == "Thursday":
        return Pizza("Meat Lovers", 13.0, ["tomato sauce", "mozzarella", "pepperoni", "ham", "bacon"])
    elif day_of_week == "Friday":
        return Pizza("Seafood", 15.0, ["tomato sauce", "mozzarella", "shrimp", "squid", "scallops"])
    elif day_of_week == "Saturday":
        return Pizza("BBQ Chicken", 14.0, ["BBQ sauce", "mozzarella", "chicken", "onion"])
    elif day_of_week == "Sunday":
        return Pizza("Hawaiian", 12.0, ["tomato sauce", "mozzarella", "ham", "pineapple"])


def create_order(day_of_week: str, extra_ingredients: List[str]) -> PizzaOrder:
    pizza = get_pizza_of_the_day(day_of_week)
    return PizzaOrder(pizza, extra_ingredients)


order = create_order("Monday", ["cheese", "olives"])
print(order)

order = create_order("Saturday", ["onions", "jalapenos", "tomatoes"])
print(order)

