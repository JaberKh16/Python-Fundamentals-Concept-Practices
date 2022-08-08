
class Library:
    
    def __init__(self, list_of_books) -> None:
        self.available_books = list_of_books
    
    # to display all the available books
    def display_available_books(self):
        for books in self.available_books:
            print(f'Available Books are : {books}')
    
    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print(f'You have now borrowd the book {requested_book}')
            self.available_books.remove(requested_book)
        
        # elif book_count is 2 and requested_book in self.available_books:
        #     print(f'You have now borrowd the {book_count} books name {requested_book}')
        #     self.available_books.remove(requested_book) 
        
        else:
            print('Sorry , the book is not available in book list') 
            
    def add_book(self, returned_book):
        # if no_of_book is 1:
        #     self.available_books.append(returned_book)
        # elif no_of_book is 2:
        self.available_books.append(returned_book)
        
    
class Customer:
    
    def request_books(self):
        #borrow_book_count = 0
        #print('Enter the how many book you wanna borrow, limitation is 2')
        #book_want = int(input())
        #if book_want is 1:
        print('Enter the name of the book you would like to borrow:')
        self.book = input() # though book name is string
            #borrow_book_count += 1
        return self.book
        # elif book_want is 2:
        #     print('Enter the name of the books you would like to borrow:')
        #     # though book name is string
        #     self.books = input().split(',')
        #     borrow_book_count += book_want 
        #     return self.books, borrow_book_count
        
        
    def return_book(self):
        #book_returned = int(input('Enter the no. of books wanna returned: '))
        #if book_returned is 1:
        print('Enter the name of the book which you are returning:')
        self.book = input()
        return self.book
        # elif book_returned is 2:
        #     print('Enter the name of the book which you are returning:')
        #     self.books = input().split(',')
        #     return self.books
            

book_list = ['Time Management', 'Grow Enrich', 'C++ Paradigm', 'For One More Day']
library  = Library(book_list)
customer = Customer()

while True:
    print('Enter 1 to display the available books')
    print('Enter 2 to request for a book or books')
    print('Enter 3 to return a book or books')
    print('Enter 4 to exit')
    
    user_choice = int(input('Enter the choice: '))
    
    if user_choice == 1:
        library.display_available_books()
    
    elif user_choice == 2:
        requested_book = customer.request_books()
        library.lend_book(requested_book)
    
    elif user_choice == 3:
        returned_book = customer.return_book()
        library.add_book(returned_book)
    
    elif user_choice == 4:
        print('Exiting...')
        exit()