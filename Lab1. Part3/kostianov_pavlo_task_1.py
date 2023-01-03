class Books:
    books = []

    def __init__(self,  author, title, publisher, year, pages):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.pages = pages

    def __str__(self):
        if self.year >= 2010:
            return f'{self.author} {self.title} {self.publisher} {self.year} {self.pages}'


b1 = Books('J. K. Rowling', 'Harry Potter', 'Mahaon', 2004, 400)
b2 = Books('T. G. Shevchenko', 'Kobzar', 'Ababahalamaga', 1995, 160)
b3 = Books('J. K. Rowling', 'Harry Potter', 'Mahaon', 2012, 400)
b4 = Books('J. K. Rowling', 'Harry Potter', 'Mahaon', 2004, 400)
b5 = Books('J. K. Rowling', 'Harry Potter', 'Mahaon', 2004, 400)
b6 = Books('J. K. Rowling', 'Harry Potter', 'Mahaon', 2004, 400)

Books.__str__(b3)
