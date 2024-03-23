class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author, status):
        book = {"book_id": book_id, "title": title, "author": author, "status": status}
        self.books.append(book)

    def add_member(self, member_id, name):
        member = {"member_id": member_id, "name": name, "borrowed_books": []}
        self.members.append(member)

library = LibraryManagementSystem()


library.add_book(2024001, "Python Programming", "Jacob Zuma", "Available")


library.add_member(1, "Anelisa Maleka")


print("Books:")
for book in library.books:
    print(book)
print("\nMembers:")
for member in library.members:
    print(member)


