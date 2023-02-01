class Library:
  
  def __init__(self,list,name):
    self.listofbooks = list
    self.name = name
    self.lendbook = {}

  def display(self):
    print()
    for book in self.listofbooks:
      print(book)

  def lendBook(self,bookname,user):
    self.lendbook.update({bookname:user})
    self.listofbooks.remove(bookname)

  def addBook(self,bookn):
    self.listofbooks.append(bookn)

  def returnBook(self):
    self.listofbooks.append(bookname)
    self.lendbook.pop(bookname)

lib = Library(["focus","rich dad poor dad","think and grow","how to communicate"],"GVKV")
while True:
    user_choice = int(input("""\nWELCOME TO LIBRARY\nchoose any option from following\n1: display the books\n2: lendbook\n3: addbook\n4: returnbook\nEnter 1,2,3,4\t: """))
    if user_choice == 1:
      lib.display()

    elif user_choice == 2:
      bookname = input("Which book you want: ")
      if bookname not in lib.lendbook:
        user = input("Enter your name:  ")
        lib.lendBook(bookname,user)

    elif user_choice == 3:
      bookn = input("Enter the name of book you want to add:  ")
      lib.addBook(bookn)

    elif user_choice == 4:
      bookname = input("Enter the name of book you returning:  ")
      if bookname in lib.lendbook:
        user = input("Enter who lend the book: ")
        if user in lib.lendbook.values():
          lib.returnBook()
        else:
          print("Wrong username")
      else:
        print("This book is not lended")

    choice = input("\nYou want to continue\nEnter y or n: ")
    if choice == "y":
      continue
    elif choice == "n":
      break
    