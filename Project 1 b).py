from tkinter import Tk, Frame, Label, Entry, Radiobutton, StringVar, TOP, BOTTOM, LEFT, RIGHT, Button, DISABLED, Scrollbar, VERTICAL, HORIZONTAL, Y, X, W, NO
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title('A Library Application')


# Functions
def Database():
    global conn, cursor
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, booktitle TEXT, author TEXT, year INTEGER, isbn TEXT)")


def Add():
    if BOOKTITLE.get() == "" or AUTHOR.get() == "" or YEAR.get() == "" or ISBN.get() == "":
        txt_result.config(text="Please enter all the fields", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO books (booktitle, author, year, isbn) VALUES (?,?,?,?)",
                       (BOOKTITLE.get(), AUTHOR.get(), YEAR.get(), ISBN.get()))
        # (booktitle, author, year, isbn)
        conn.commit()
        BOOKTITLE.set("")
        AUTHOR.set("")
        YEAR.set("")
        ISBN.set("")
        # cursor.commit()
        conn.close()
        txt_result.config(text="Created a data !", fg="green")


def Display():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM books")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert("", "end", values=(data[1], data[2], data[3], data[4]))
    cursor.close()
    conn.close()
    txt_result.config(
        text="Successfully read the data from database", fg="black")


def Exit():
    result = tkMessageBox.askquestion("Do you want to exit ?", icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


# Variable Declaration
BOOKTITLE = StringVar()
AUTHOR = StringVar()
YEAR = StringVar()
ISBN = StringVar()


# Frame
Top = Frame(root, width=900, height=50, bd=8, relief='raise', bg='blue')
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8,
             relief='raise', background='red')
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief='raise', bg='yellow')
Right.pack(side=RIGHT)


Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)

Buttons = Frame(Left, width=300, height=100, bd=8, relief='raise')
Buttons.pack(side=BOTTOM)

# Labels
txt_title = Label(Top, width=900, font=("arial", 24),
                  text=".....Library Management Application.....")
txt_title.pack()
txt_booktitle = Label(Forms, text='Booktitle:', font=("arial", 16), bd=15)
txt_booktitle.grid(row=0, sticky="e")
txt_author = Label(Forms, text='Author:', font=("arial", 16), bd=15)
txt_author.grid(row=1, sticky="e")
txt_year = Label(Forms, text='Year:', font=("arial", 16), bd=15)
txt_year.grid(row=2, sticky="e")
txt_isbn = Label(Forms, text='ISBN:', font=("arial", 16), bd=15)
txt_isbn.grid(row=3, sticky="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)


# Entry Widget
booktitle = Entry(Forms, textvariable=BOOKTITLE, width=30)
booktitle.grid(row=0, column=1)
author = Entry(Forms, textvariable=AUTHOR, width=30)
author.grid(row=1, column=1)
year = Entry(Forms, textvariable=YEAR, width=30)
year.grid(row=2, column=1)
isbn = Entry(Forms, textvariable=ISBN, width=30)
isbn.grid(row=3, column=1)


# Button Widget
btn_display = Button(Buttons, width=10, text='Display', command=Display)
btn_display.pack(side=LEFT)
btn_search = Button(Buttons, width=10, text='Search', state=DISABLED)
btn_search.pack(side=LEFT)
btn_add = Button(Buttons, width=10, text='Add', command=Add)
btn_add.pack(side=LEFT)
btn_issue = Button(Buttons, width=10, text='Issue', state=DISABLED)
btn_issue.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text='Delete', state=DISABLED)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text='Exit', command=Exit)
btn_exit.pack(side=LEFT)


# List Widget
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)

tree = ttk.Treeview(Right, height=40, columns=(
    "Booktitle", "Author", "Year", "ISBN"))

scrollbary.config(command=tree.yview)
scrollbarx.config(command=tree.xview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.pack(side=RIGHT, fill=X)
tree.heading("Booktitle", text="Booktitle", anchor=W)
tree.heading("Author", text="Author", anchor=W)
tree.heading("Year", text="Year", anchor=W)
tree.heading("ISBN", text="ISBN", anchor=W)
tree.column("#0", stretch=NO, minwidth=0, width=10)
tree.column("#1", stretch=NO, minwidth=0, width=200)
tree.column("#2", stretch=NO, minwidth=0, width=200)
tree.column("#3", stretch=NO, minwidth=0, width=95)
tree.column("#4", stretch=NO, minwidth=0, width=95)
tree.pack()


# Initialization
if __name__ == "__main__":
    root.mainloop()
