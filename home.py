list=["C","PYTHON","JAVA","JAVASCRIPT","C#"]


def available():
   print("Available Books:",list)

def add():
    book=input("Enter the book name that yoy want to add:")
    list.append(book)

def remove():
    book=input("Enter the book name that you want to remove:")
    if book in list:
        list.remove(book)
    else :
        print("The book is not available")

def issue():
    book=input("Enter the book name that you want to issue:")
    if book in list:
        print("The book is available and it can issue")
        list.remove(book)
    else:
        print("The book is not available")

def return1():
    book=input("Enter the book name than you want ot return :")
    list.append(book)
    print (list)

while True:
    print("1. SHOW AVAILABE BOOKS")
    print("2. ADD BOOK")
    print("3. ISSUE BOOK")
    print("4. RETURN BOOK")
    print("5. EXIT")
    choice=int(input("Enter your choice: "))
    if choice==1:
        available()
    elif choice==2:
        add()
    elif choice==3:
        issue()
    elif choice==4:
        return1()
    elif choice==5:
        print("thank you")
        break
    else:
        print("Invalid choice")



