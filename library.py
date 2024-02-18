class Library:
    def __init__(self):
        self.file = open("books.txt", "a+", )
        self.year = None
        self.page = None

    def ListBooks(self):
        self.file.seek(0)
        self.list = self.file.readlines()

        if not self.list:
            print("The book list is empty.")
            return

        for book in self.list[0::]:
            print(book.strip())

    def AddBook(self):
        self.title = input("Enter title: ")
        self.author = input("Enter author: ")
        try:
            self.year = int(input("Enter year: "))
            self. page = int(input("Enter pages: "))
        except ValueError:
            print("Error: Please enter a valid numeric value for Year and Pages")


        self.add_book = self.file.write(self.title + "," + self.author + "," + str(self.year) + "," + str(self.page) + "\n")

    def RemoveBook(self):
        self.remove_title = input("Book title: ")
        self.remove_author = input("Author name:")
        self.file.seek(0)
        self.remove_book = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for book in self.remove_book:
            if self.remove_title and self.remove_author not in book:
                self.file.write(book)



    def __del__(self):
        self.file.close()


