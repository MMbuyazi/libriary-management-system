
books = []
members = []


def display_books():
    print("Books:")
    for book in books:
        print(book)


def display_members():
    print("Members:")
    for member in members:
        print(member)


book_id = input("Enter book ID: ")
title = input("Enter book title: ")
author = input("Enter author name: ")
status = input("Enter book status: ")
book = {"book_id": book_id, "title": title, "author": author, "status": status}
books.append(book)
print(f"Book '{title}' added successfully.")

member_id = input("Enter member ID: ")
name = input("Enter member name: ")
member = {"member_id": member_id, "name": name, "borrowed_books": []}
members.append(member)
print(f"Member '{name}' added successfully.")


display_books()
display_members()
