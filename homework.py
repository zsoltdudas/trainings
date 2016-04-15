class Books(object):
    def __init__(self, uid, author, book, number):
        self.uid = uid
        self.author = author
        self.book = book
        self.number = number

class Library(object):
    def __init__(self):
        self.items = {}

    def Add(self, item):
        self.items[item.book] = item
        item.uid = {}
        i = 1
        while i <= item.number:
            lent = input('Is lent: ')
            if "yes" not in lent:
                item.uid[i] = 0
            else:
                person = input("To whom: ")
                item.uid[i] = person
            i = i+1

    def Delete(self, item):
        del self.item

    def Print(self, query):
        for item in self.items.values():
            if query in item.author:
                print item.book
                print item.uid

    def Find(self, query):
        for item in self.items.values():
            if query in item.book:
                for keys, values in item.uid.items():
                    if  values !=0:
                        print values

library = Library()
choice = 1
while choice != 0:
    print "1: Add Book, 2: Delete Book, 3: Search book by author 4: Where is my book 0:Exit"
    choice = input("whacha gonna do: ")
    if choice == 1:
        author = input("Author: ")
        author = author.capitalize()
        book = input("Book: ")
        book = book.capitalize()
        number = input("Number: ")
        uid = hash(author+book)
        uid = str(uid)
        library.Add(Books(uid,author,book,number))
    elif choice == 2:
        book = input("Book: ")
        book = book.capitalize()
        library.Delete(book)
    elif choice == 3:
        query = input("Search for what: ")
        query = query.capitalize()
        library.Print(query)
    elif choice == 4:
        query = input("Which book: ")
        query = query.capitalize()
        library.Find(query)
    elif choice == 0:
        exit()
    else:
        continue
