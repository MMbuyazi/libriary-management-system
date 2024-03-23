class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        status = input("Enter book status: ")
        book = {"book_id": book_id, "title": title, "author": author, "status": status}
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def add_member(self):
        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")
        member = {"member_id": member_id, "name": name, "borrowed_books": []}
        self.members.append(member)
        print(f"Member '{name}' added successfully.")

    def display_books(self):
        print("Books:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("Members:")
        for member in self.members:
            print(member)



library = LibraryManagementSystem()


library.add_book()


library.add_member()



library_b = LibraryManagementSystem()


library_b.add_book()
library_b.add_member()


library_b.display_books()
library_b.display_members()
