class Book:
    book_matherial = 'paper'
    def __init__(self, name, year, author):
        self.__name = name
        self._year = year
        self.author = author

    @property
    def get_name(self):
        return self.__name

    def get_year(self):
        return self._year

    def get_author(self):
        return self.author

    def set_name(self, new_name):
        self.__name = new_name

    def set_year(self, new_year):
        self._year = new_year

    def set_author(self, new_author):
        self.author = new_author


class ChildBook(Book):
    def __init__(self, name, year, author, cover):
        super().__init__(name, year, author)
        self.cover = cover

    def reading_time(self, minutes):
        return (f'I can read this book {minutes} min')


kolobok = ChildBook('kolobok', 1950, 'world', 'hard')
print(kolobok.get_name)
kolobok.set_name('granny')
print(kolobok.get_name)
print(kolobok.reading_time(10))

zolushka = ChildBook('Zolushka', 2020, 'charl perro', 'small edition')
print(zolushka.get_name, zolushka.cover)
print(kolobok.__dict__)
print(zolushka.__dict__)