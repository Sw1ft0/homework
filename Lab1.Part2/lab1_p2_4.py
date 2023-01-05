import os


class FileReader:

    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Incorrect type of file name")
        if not os.path.exists(title):
            raise Exception("File with that name does not exist")
        self.__title = title

    def symbols(self):
        quantity = 0

        with open(self.__title, 'r') as safe:
            for line in safe:
                quantity = quantity + len(line)

        return quantity

    def words(self):
        quantity = 0

        with open(self.__title, 'r') as safe:
            for line in safe:
                line = line.strip(os.linesep)
                words_list = line.split()
                quantity += len(words_list)

        return quantity

    def sentences(self):
        quantity = 0

        with open(self.__title, 'r') as safe:
            for line in safe:
                quantity += line.count('.')

        return quantity

    def __str__(self):
        return f"File name: {self.__title}"


title = 'lab_tasks.txt'
file = FileReader(title)
print(file)
print('Quantity of symbols -> ', file.symbols())
print('Quantity of words -> ', file.words())
print('Quantity of sentences -> ', file.sentences())
