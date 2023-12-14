from typing import List


class Book:
    def __init__(self,title,author=None,year=None) -> None:
        self.title = title
        self.author = author
        self.year = year


    def display(self):
        if self.author is None:
            self.author = ""
            print("%-30s %-20s %5s" % (self.title,self.author,self.year))
        elif self.year is None:
            print("%-30s %-20s" % (self.title,self.author))
        else:
            print("%-30s %-20s %5s" % (self.title,self.author,self.year))


class Library(Book):
    def __init__(self,book_name) -> None:
        self.name = book_name
        self.book_list = {}


    def get_book_name(self):
        return self.name


    def get_book_data(self,name_book):
        if name_book in self.book_list:
            return self.book_list[name_book]
        else:
            print("Opps")


    def list(self):
        print(f"%-30s %-20s %5s" % ("Name","Author","Year"))   
        for book in self.book_list:
            print("%-30s %-20s %5s"  % (book, self.book_list[book][0], self.book_list[book][1]))


    def filter(self):
        filtered_books = []
        user_input = input("Choose the parameter filter: 'title' or 'author' or 'year':\n>")
        if user_input == "title":
            print('Filtered list:')
            title_input = input("Enter the title:")
            filtered_books = list(filter(lambda k:k.title ==title_input,self.book_list))
            print(list(map(str,filtered_books)))
        elif user_input == "author":
            print('Filtered list:')
            author_input = input("Enter the author:")
            filtered_books = list(filter(lambda k:k.author==author_input,self.book_list))
            print(list(map(str,filtered_books)))
        elif user_input == "year":
            print('Filtered list:')
            year_input = input("Enter the year:")
            filtered_books = list(filter(lambda k:k.year==year_input,self.book_list))
            print(list(map(str,filtered_books)))


    def add_book(self,title:str,author:str,year:str):
            self.book_list[title] = [author,year]
    
    
    def remove_book(self,title:str):
        if title in self.book_list:
            del self.book_list[title]
        else:
            print("Sorry,we can't find the book")    
    


library = Library("My Home Library")
library.add_book('Чистый код', 'Дядя Боб',2017)
library.add_book('Идеальный программист', 'Дядя Боб', 2018)
print(library.name)
library.list()

