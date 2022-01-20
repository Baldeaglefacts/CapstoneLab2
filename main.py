class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if self.books.__contains__(title):
            print('Book already found!')
        else:
            self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'


def main():
    pratchett = Author('Terry Pratchett')
    pratchett.publish('Small Gods')
    pratchett.publish('Small Gods')
    print(pratchett)


main()
