from library import Library
lib = Library()



system = True


while system:
    print("*** MENU ***" + "\n" + "1. Add Book" + "\n" + "2 - Delete Book" + "\n" + "3 - List Books" "\n" + "4 Quit(q)")
    enter = (input("Enter your choice (1-4):  ")).lower()
    if enter == "1":
        lib.AddBook()

    elif enter == "2":
        lib.RemoveBook()

    elif enter == "3":
        lib.ListBooks()

    elif enter == "4" or enter == "q":
        system = False

    else:
        print(f"{enter} not valid. Please  enter a correct valid")





