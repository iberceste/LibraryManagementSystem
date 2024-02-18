from tkinter import *
from tkinter import messagebox
from library import Library

lib = Library()


class Window:
    MAINBG = "bg.png"


    def __init__(self, library):
        self.library = library

        self.window = Tk()
        self.window.title("Library Management System")
        self.MainCanvas()

    def MainCanvas(self):
        self.canvas = Canvas(self.window, width=self.window.winfo_screenwidth(), height=self.window.winfo_screenheight())
        self.canvas.pack(fill=BOTH, expand=YES)  # Canvas ana pencerenin tamamını doldurur
        self.MainBg = PhotoImage(file=self.MAINBG)
        self.canvas.create_image(0, 0, anchor=NW, image=self.MainBg, tags="bg")
        self.canvas.tag_lower("bg")  # Resmi en arka planda tutar


    def ListBooksUi(self, list_books):
        self.list_button = Button(self.window, text="List Book", command=self.libr)
        self.list_button.grid(row=0, column=0)

    def AddBooksUi(self):
        pass

    def RemoveBooksUi(self):
        pass

    def Run(self):
        self.window.mainloop()
    def SearchBooksUi(self):
        pass








