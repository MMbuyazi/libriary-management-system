import pandas as pd


books_df = pd.DataFrame(columns=["book_id", "title", "author", "status"])
members_df = pd.DataFrame(columns=["member_id", "name", "borrowed_books"])


book_id = input("Enter book ID: ")
title = input("Enter book title: ")
author = input("Enter author name: ")
status = input("Enter book status: ")
books_df = books_df.append({"book_id": book_id, "title": title, "author": author, "status": status}, ignore_index=True)
print(f"Book '{title}' added successfully.")

member_id = input("Enter member ID: ")
name = input("Enter member name: ")
members_df = members_df.append({"member_id": member_id, "name": name, "borrowed_books": []}, ignore_index=True)
print(f"Member '{name}' added successfully.")


print("Books:")
print(books_df)

print("\nMembers:")
print(members_df)
