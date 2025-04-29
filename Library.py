library = []

def show_menu():
    print("\n--- Personal Library ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Exit")

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    book = {"title": title, "author": author}
    library.append(book)
    print("Book added!")

def show_books():
    if not library:
        print("No books in library.")
    for book in library:
        print(f"{book['title']} by {book['author']}")

while True:
    show_menu()
    choice = input("Choose (1-3): ")
    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
        