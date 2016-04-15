""" Homework cont.
Create a small library inventory app that would be able to store information on books. For each book we need to know: Author, Title, number of copies in the library and for each copy we need to know it's status,
is it lent or is it available. The application should be able to hold the inventory, add or delete books from the inventory,
add or delete copies of a specific book and perform basic querys like returning all the books by an author or all the books that contain a certain word.

Improve the library app to take full use of object orientation. Also, now books can be lent to actual people :)
You should be able to determine what books each person has and for every book you should be able to determine exactly to whom it is lent.
"""


import os


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
        os.system('pause')

    def Delete(self, item):
        try:
            del self.items[item]
            print "Succesfully deleted book!"
        except:
            print "Could not find book"
        os.system('pause')

    def Print(self, query):
        print "==BOOKS=="
        for item in self.items.values():
            if query in item.author:
                print item.book
        os.system('pause')

    def Find(self, query):
        print "==LENT TO=="
        for item in self.items.values():
            if query in item.book:
                for keys, values in item.uid.items():
                    if  values !=0:
                        print values
        os.system('pause')

library = Library()
choice = 1
while choice != 0:
    os.system('cls')
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
