books=[]
issued_books=[]
def add_book():
    name=input('Enter name of book:')
    books.append(name)
    print(name,'book is added.')
def show_book():
    if len(books)==0:
        print('No books available.')    
    else:
        print("Available books.")
        for b in books:
            print(books)

def issue_book():
    if len(books)==0:
        print('No book available.')
        return
    else:
        show_book()
        name=input("Book you want to issue.")
        if name in books:
            issued_books.append(name)
            books.remove(name)
            print(name,'is issued.')
        else:
            print(name,'is not available.')   
def return_book():
    name=input("Enter the book name.")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name,'book is return succesfully.')
    else:
        print(name,'is not issued or not belong to the library.')    
def library():
    while True:
        print('Menu')
        print('1.Add Books')
        print('2.Show Books')
        print('3.Issue Books')
        print('4.Return Books')
        print('5.Exit')
        choice =int(input("Enter an Choice:"))
        if choice==1:
            add_book()
        elif choice==2:
            show_book()   
        elif choice==3:
            issue_book()        
        elif choice==4:
            return_book()   
        elif choice==5:
            print('Thank You!')
            break
        else:
            print('Invalid choice.')
library()