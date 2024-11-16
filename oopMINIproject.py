
class Book():

  def __init__(self): 
    self.books = []
    self.checked_books = []
    

  def add_new_book(self):
    book_title = input("Add title: ")
    
    if not any(book['Book Title'] == book_title for book in self.books):
      author = input("Add Author: ")
      genre = input("Add genre: ")
      publication_date = input("Add publication date: ")
      self.books.append({"Author": author, "Book Title": book_title, "Genre": genre, "Publication Date": publication_date, "Available": True})
      print(f"{book_title} written by {author} has been officially cataloged!")
    else:
      print("This title already exists within the Southwest Library System!")

  def search_book(self):
    database_title = input("Find title: ").lower()
    for book in self.books:
      if database_title == book['Book Title'].lower():
        print(f"In database: {book}")
        return book
      else:
        print("Entry not in database")

  def display_books(self):
    if not self.books:
      print("No book recorded in library database.")
    else:
      for book in self.books:
        print(book)
  
  def checkout(self):
    if self.available:
      self.available = False
      return True
    else:
      return False
  
  def return_book(self):
    self.available = True

class User():
  def __init__(self):
    self.users = []
    self.checked_books = []
    self.available = True
  #---------------------unsure
  def checked_book(self, book):
    if book.checkout(): #checkout() function is in class Book()
      self.checked_book.append(book) #self.checked [].append(parameter)
      print(f"{self.users} checked out {book.add_new_book.book_title}") #STUCK
  
  def return_book(self, book):
    self.available = True
    if book in self.checked_book:
      self.checked_book.remove(book)
      book.available = True
      print(f"{self.users} has returned {book.add_new_book.book_title}")
#------------------------------unsure
  def add_new_user(self):
    library_user = input("Add a new user: ")
    library_ID = input("Attach a unique ID (sample: A12345): ")
    if not any(user['Library Identification'] == library_ID for user in self.users):
      self.users.append({"Library Identification": library_ID, "Library User": library_user})
      print(f"Library user {library_user} has been added to library system database")
    else:
      print("Library user is already in the database")

  def view_user_details(self):
    specific_user_details = input("Find user: ").lower()
    for user in self.users:
      if specific_user_details == user['Library User'].lower():
        print(f"Library User's Information: {user}")
        return user
      else:
        print("User not in database")
        return None

  def display_all_users(self):
    if not self.users:
      print("No users recorded")
    else:
      for user in self.users:
        print(user)

class Author:
  def __init__(self):
    self.authors = []

  def add_new_author(self):
    author_entry = input("Add an author to the database: ").lower()
    author_bio_entry = input("Write a brief biography: ")
    if not any(author['Authors Name'] == author_entry for author in self.authors):
      self.authors.append({"Authors Name": author_entry, "Biography": author_bio_entry})
      print(f"{author_entry} has been added to the library")
    else:
      print("Author is already in the database")
  
  def view_author_details(self):
    specific_author_details = input("Find an author: ")
    for author in self.authors:
      if specific_author_details == author['Authors Name']:
        print(f"Information for Author is below:\n {author}")
        return author
      else:
        print("Author not in database.")
        return None

  def display_all_authors(self):
    if not self.authors:
      print("No Author's recorded")
    else:
      for author in self.authors:
        print(author)

def main():
  py_library_system = Book()
  py_user_system = User()
  py_author_info_system = Author()

  while True:
    print("\n1. Book Operations \n2. User Operations \n3. Author Operations \n4. Quit")
    user_input = input("Enter a number: ").lower()
    if user_input.lower() == "4":
      break
    if user_input == '1':
      print("\n1. Add a new book \n2. Search for a book \n3. Display all books")
      sub_selection = input("Enter selection: ")
      if sub_selection == '1':
        py_library_system.add_new_book()
      elif sub_selection == '2':
        py_library_system.search_book()
      elif sub_selection == '3':
        py_library_system.display_books()

    elif user_input == '2':
      print("\n1. Add a new user \n2. View user details \n3. Display all users \n4. Borrow Book///Return Book")
      sub_selection = input("Enter a new selection: ")
      if sub_selection == '1':
        py_user_system.add_new_user()
      elif sub_selection == '2':
        py_user_system.view_user_details()
      elif sub_selection == '3':
        py_user_system.display_all_users()

      elif sub_selection == '4':
        user_input = input("Do you want to borrow or return a book?").lower()
        #UNSURE------------------------------------>
        if user_input == "borrow":
          input_name = input("Type name: ")
          input_title = input("Type book title: ")
          library_user = book.view_user_details(input_name)
          book = book.search_book(input_title)
          if library_user and book:
            library_user.checkout(book)

        elif user_input == "return":
          input_name = input("Type name: ")
          input_title = input("Type book title: ")
          library_user = book.view_user_details(input_name)
          book = book.search_book(input_title)
          if library_user and book:
            library_user.return_book(book)
        #UNSURE------------------------------------->

    elif user_input == '3':
      print("\n1. Add a new author \n2. View author details \n3. Display all authors")
      sub_selection = input("Enter a selection: ")
      if sub_selection == '1':
        py_author_info_system.add_new_author()
      elif sub_selection == '2':
        py_author_info_system.view_author_details()
      elif sub_selection == '3':
        py_author_info_system.display_all_authors()

if __name__ == "__main__":
  main()