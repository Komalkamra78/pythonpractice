from re import I


class Library:
    library = "SaintMarry"

    def __init__(self, ListOfBooks):
        self.books = ListOfBooks

    def DisplayAvailableBooks(self):
        print(f"the books present in this library {self.library} are: ")
        for book in self.books:
             print("\t" + "*" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print("book is Available! ")
            print(f"you have been issued {bookName}. please keep it safe and return it within 10 days!")
            self.books.remove(bookName)
            return True
        else:
            print("sorry! this book is either not available or has already been issued to someone else. Please wait untill the book is available! ")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book! Hope you enjoyed reading it!")


class Student:

    def requestBook(self):
        self.book = input("enter the name of the book you want to borrow: ")
        return self.book 

    def returnBook(self):
        self.book = input("enter the name of the book you want to return: ")
        return self.book 


if __name__ == "__main__":
    centralLibrary = Library(["algorithm", "django", "clrs", "python notes", "c++ notes"])
    student = Student()
    #centralLibrary.DisplayAvailableBooks()

    while(True):
        welcomeMsg='''
        
        ====Welcome to Central Library saint marry====
        please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. exit the library
    
        '''
        print(welcomeMsg)
        
        a = int(input("enter a choice: "))
        if a == 1:
            centralLibrary.DisplayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
        # print(welcomeMsg)

        

