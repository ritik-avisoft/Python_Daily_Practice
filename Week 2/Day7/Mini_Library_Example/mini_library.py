# mini_library.py

class Book:
    """A physical book."""
    next_id = 1  # class variable: unique id counter for all Book instances

    def __init__(self, title, author, copies=1):
        self.id = Book.next_id
        Book.next_id += 1

        self.title = title              # instance vars
        self.author = author
        self.copies = copies

    def is_available(self):
        return self.copies > 0

    def borrow(self):
        if self.is_available():
            self.copies -= 1
            return True
        return False

    def return_copy(self):
        self.copies += 1

    def info(self):
        return f"[{self.id}] {self.title} by {self.author} — copies: {self.copies}"


class DigitalBook(Book):
    """A digital book — no physical copies, availability works differently."""
    def __init__(self, title, author, file_size_mb):
        # DigitalBook still wants an id and title/author behavior from Book.
        super().__init__(title, author, copies=0)  # call parent __init__
        self.file_size_mb = file_size_mb

    # override is_available — digital always available
    def is_available(self):
        return True

    # override borrow: no copies decrement
    def borrow(self):
        # maybe log usage; return True to indicate success
        return True

    def info(self):
        base = super().info()
        return f"{base} (digital, {self.file_size_mb}MB)"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []  # list of Book ids

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed.append(book.id)
            return True
        return False

    def return_book(self, book):
        if book.id in self.borrowed:
            book.return_copy()
            self.borrowed.remove(book.id)
            return True
        return False

    def info(self):
        return f"{self.name} has borrowed: {self.borrowed}"


class Library:
    library_count = 0  # class variable tracking number of library instances

    def __init__(self, name):
        self.name = name
        self.catalog = {}   # maps book.id -> Book instance
        self.members = {}   # maps member name -> Member
        Library.library_count += 1

    def add_book(self, book):
        self.catalog[book.id] = book

    def add_member(self, member):
        self.members[member.name] = member

    def find_available_books(self):
        return [b for b in self.catalog.values() if b.is_available()]

    def borrow(self, member_name, book_id):
        member = self.members.get(member_name)
        book = self.catalog.get(book_id)
        if not member:
            return f"No member named {member_name}"
        if not book:
            return f"No book with id {book_id}"
        if member.borrow_book(book):
            return f"{member.name} successfully borrowed {book.title}"
        return f"Cannot borrow {book.title} (not available)"

    def return_book(self, member_name, book_id):
        member = self.members.get(member_name)
        book = self.catalog.get(book_id)
        if member and book:
            if member.return_book(book):
                return f"{member_name} returned {book.title}"
            return f"{member_name} does not have {book.title}"
        return "Member or book not found"

    def catalog_info(self):
        return [b.info() for b in self.catalog.values()]


class Member:
    MEMBERSHIP_FEE = 50

    def __init__(self, name):
        self.name = name
        self.__wallet = 0                # private → encapsulation
        self.borrowed_books = []

    # Deposit money inside wallet
    def add_money(self, amount):
        self.__wallet += amount

    # Abstraction → A single method that handles internal steps
    def borrow(self, book):
        if not book.is_available():
            return f"{book.title} is not available now."

        # internal complex logic is hidden from user
        if len(self.borrowed_books) == 0:            # first borrow → membership
            if self.__wallet < Member.MEMBERSHIP_FEE:
                return "Insufficient wallet balance to activate membership."
            self.__wallet -= Member.MEMBERSHIP_FEE   # deducted internally

        book.borrow()
        self.borrowed_books.append(book.id)
        return f"{self.name} borrowed {book.title}"

    # Getter method (encapsulation)
    def get_wallet_balance(self):
        return self.__wallet


# Example usage
if __name__ == "__main__":
    lib = Library("Downtown Library")
    b1 = Book("1984", "George Orwell", copies=3)
    b2 = Book("Clean Code", "Robert C. Martin", copies=1)
    db = DigitalBook("Automate the Boring Stuff", "A. Sweigart", file_size_mb=5)

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(db)

    alice = Member("Alice")
    bob = Member("Bob")
    lib.add_member(alice)
    lib.add_member(bob)

    print(lib.catalog_info())
    print(lib.borrow("Alice", b1.id))  # Alice borrows 1984
    print(lib.borrow("Bob", b1.id))    # Bob borrows 1984
    print(lib.borrow("Bob", b1.id))    # Bob borrows 1984 (3rd copy)
    print(lib.borrow("Alice", b1.id))  # cannot borrow — no copies left
    print(lib.borrow("Alice", db.id))  # digital book — always succeeds

    print(alice.info())
    print(bob.info())

    print(lib.return_book("Bob", b1.id))
    print(lib.find_available_books())  # Now 1984 might be available again
    print("Libraries created:", Library.library_count)
