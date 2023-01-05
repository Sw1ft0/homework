import datetime


class Ticket:
    def __init__(self, number: int, price: float, event_name: str, event_date: datetime.date,
                 purchase_date: datetime.date):
        self.number = number
        self.price = price
        self.event_name = event_name
        self.event_date = event_date
        self.purchase_date = purchase_date

    def get_price(self) -> float:
        return self.price

    def __str__(self) -> str:
        return f"Ticket {self.number} for {self.event_name}" \
               f"on {self.event_date.strftime('%Y-%m-%d')}: {self.price}." \
               f" Purchase date: {self.purchase_date.strftime('%Y-%m-%d')}"


class RegularTicket(Ticket):
    def __init__(self, number: int, price: float, event_name: str, event_date: datetime.date,
                 purchase_date: datetime.date):
        super().__init__(number, price, event_name, event_date, purchase_date)


class AdvanceTicket(Ticket):
    def __init__(self, number: int, price: float, event_name: str, event_date: datetime.date,
                 purchase_date: datetime.date):
        super().__init__(number, price * 0.6, event_name, event_date, purchase_date)


class LateTicket(Ticket):
    def __init__(self, number: int, price: float, event_name: str, event_date: datetime.date,
                 purchase_date: datetime.date):
        super().__init__(number, price + price * 0.1, event_name, event_date, purchase_date)


class StudentTicket(Ticket):
    def __init__(self, number: int, price: float, event_name: str, event_date: datetime.date,
                 purchase_date: datetime.date):
        super().__init__(number, price * 0.5, event_name, event_date, purchase_date)


def buy_ticket(number: int, price: float, event_name: str, event_date: datetime.date,
               purchase_date: datetime.date = None) -> Ticket:
    if purchase_date:
        days_until_event = (event_date - purchase_date).days
        if days_until_event >= 60:
            return AdvanceTicket(number, price, event_name, event_date, purchase_date)
        elif days_until_event < 10:
            return LateTicket(number, price, event_name, event_date, purchase_date)
    if number == 4:
        return StudentTicket(number, price, event_name, event_date, purchase_date)
    return RegularTicket(number, price, event_name, event_date, purchase_date)


my_ticket = buy_ticket(1, 100.0, "Google Conference", datetime.date(2023, 3, 7), datetime.date.today())
print(my_ticket)

print('Student ticket price: ', my_ticket.get_price())
