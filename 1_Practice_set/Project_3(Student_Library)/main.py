# Implement a Student library System using Oops where students can borrow a book from the list of books.
# Create a separate library and student class. Your program must be menu driven.
# You are free to choose methods and attribute of your choice to implement this functionality.


class libraryCls:
    def __init__(self,listOfBooks):
        self.listOfBooks = listOfBooks

    def displayBooks(self):
        print("Books present in this library are: ")
        for books in self.listOfBooks:
            print(" *" +books)

    def borrowBook(self, bookname):
        if bookname in self.listOfBooks:
            print(f"You have been issued {bookname}. Please keep it safe and return it within 30 days.")
            self.listOfBooks.remove(bookname)
        else:
            print("Sorry, This book is either not available or  has already been isuued to someone else. Please wait until the book is returned.")

    def returnBook(self,bookname):
        self.listOfBooks.append(bookname)
        print("Thanks for adding or returning this book ! Happy Learning !")

class studentCls:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    CentralLibrary = libraryCls(["Angular", "Python", "Html", "Css", "Javascript", "C", "C++"])
    Studentzone = studentCls()
    while(True):
        welcomemsg = '''
        ==========WELCOME TO CENTRAL LIBRARY==========
        Please choose an option:
        1. Listing all the books.
        2. Request a book.
        3. Return a book.
        4. Exit the Library.
        '''
        print(welcomemsg)
        try:
            a = int(input("Enter a choice: "))
            if a == 1:
                CentralLibrary.displayBooks()
            elif a == 2:
                book = Studentzone.requestBook()
                book = book.capitalize()
                CentralLibrary.borrowBook(book)
            elif a == 3:
                book = Studentzone.returnBook()
                book = book.capitalize()
                CentralLibrary.returnBook(book)
            elif a == 4:
                print("Thanks for choosing Central Library :-)\nHave a great day :-)")
                exit()
            else:
                print("Invalid choice")
        except Exception:
            print("Invalid choice. Please enter the correct option.")

    



