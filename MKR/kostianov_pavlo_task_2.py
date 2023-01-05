class Date:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, day: int):
        if 1 <= day <= 31:
            self.__day = day
        else:
            raise ValueError("Invalid day")

    @month.setter
    def month(self, month: int):
        if 1 <= month <= 12:
            self.__month = month
        else:
            raise ValueError("Invalid month")

    @year.setter
    def year(self, year: int):
        self.__year = year

    def __repr__(self):
        return f"{self.__day} {self.month_name()} {self.__year} year"
    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def month_name(self):
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        return months[self.__month - 1]


date = Date(23, 2, 2022)
print(date)
print(repr(date))