class Books:
    def __init__(self,  author, title, publisher, year, pages):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.is_published_after_2010()

    def is_published_after_2010(self):
        if self.year > 2010:
            return print(self)

    def __str__(self):
        return f'{self.author} | {self.title} | {self.publisher} | {self.year} | {self.pages} pages'


b1 = Books('J. K. Rowling', 'Harry Potter and the Philosopher`s Stone', 'Mahaon', 2004, 400)
b2 = Books('T. H. Shevchenko', 'Kobzar', 'Ababahalamaga', 1995, 160)
b3 = Books('E. L. James', 'Fifty Shades of Grey', 'Ababahalamaga', 2011, 514)
b4 = Books('E. L. James', 'Fifty Shades Darker', 'Ababahalamaga', 2011, 544)
b5 = Books('E. L. James', 'Fifty Shades Freed', 'Ababahalamaga', 2012, 592)
b6 = Books(' J. R. R. Tolkien', 'The Fellowship of the Ring', 'George Allen & Unwin', 1954, 423)
