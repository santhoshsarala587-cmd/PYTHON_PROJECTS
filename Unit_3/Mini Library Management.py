

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by User {self.borrowed_by}"
        return f"{self.book_id}. {self.title} by {self.author} [{status}]"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.user_id}. {self.name}"


books = [
    Book(1, "Python Basics", "John"),
    Book(2, "AI Fundamentals", "Smith"),
    Book(3, "Data Structures", "David"),
    Book(4, "Machine Learning", "Andrew"),
    Book(5, "Deep Learning", "Ian")
]

users = [
    User(1, "Siva"),
    User(2, "Santhosh"),
    User(3, "Arun"),
    User(4, "Vishal"),
    User(5, "Pradesh"),
    User(6, "Vinson")
]


def show_books():
    print("\n--- Books ---")
    for book in books:
        print(book)


def show_users():
    print("\n--- Users ---")
    for user in users:
        print(user)


def show_borrowed():
    print("\n--- Borrowed Books ---")
    for book in books:
        if not book.is_available:
            print(f"{book.title} | Borrowed by User {book.borrowed_by}")


def borrow_book(user, book):
    if book.is_available:
        book.is_available = False
        book.borrowed_by = user.user_id
        user.borrowed_books.append(book)
        print(f" Book '{book.title}' borrowed by {user.name}")
    else:
        print(" Book not available!")


def return_book(user, book):
    if book in user.borrowed_books:
        book.is_available = True
        book.borrowed_by = None
        user.borrowed_books.remove(book)
        print(f" Book '{book.title}' returned by {user.name}")
    else:
        print(" This book was not borrowed by this user!")


def find_user(uid):
    for u in users:
        if u.user_id == uid:
            return u
    return None


def find_book(bid):
    for b in books:
        if b.book_id == bid:
            return b
    return None


def menu():
    print("\n===== Library Menu =====")
    print("1. Show Books")
    print("2. Show Users")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Borrowed Books")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            show_books()
        elif choice == "2":
            show_users()
        elif choice == "3":
            uid = int(input("Enter User ID: "))
            bid = int(input("Enter Book ID: "))
            user = find_user(uid)
            book = find_book(bid)
            if user and book:
                borrow_book(user, book)
            else:
                print(" Invalid user or book!")
        elif choice == "4":
            uid = int(input("Enter User ID: "))
            bid = int(input("Enter Book ID: "))
            user = find_user(uid)
            book = find_book(bid)
            if user and book:
                return_book(user, book)
            else:
                print(" Invalid user or book!")
        elif choice == "5":
            show_borrowed()
        elif choice == "6":
            print("Exiting. Thank you!")
            break
        else:
            print(" Invalid choice!")


if __name__ == "__main__":
    main()