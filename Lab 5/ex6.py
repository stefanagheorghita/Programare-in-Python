class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def display_info(self):
        status = "available" if not self.checked_out else "checked out"
        message = f"Title: {self.title} | Status: {status}"
        return message


class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title)
        self.author = author
        self.genre = genre

    def display_info(self):
        return super().display_info() + f"\nAuthor: {self.author}" + f"\nGenre: {self.genre}"


class DVD(LibraryItem):
    def __init__(self, title, type, director):
        super().__init__(title)
        self.director = director
        self.type = type

    def display_info(self):
        return super().display_info() + f"\nDirector: {self.director}" + f"\nType: {self.type}"


class Magazine(LibraryItem):
    def __init__(self, title, topic):
        super().__init__(title)
        self.topic = topic

    def display_info(self):
        return super().display_info() + f"\nTopic: {self.topic}"


book = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
dvd = DVD("The Godfather", "Drama Film", "Francis Ford Coppola")
magazine = Magazine("National Geographic", "Science")
print(book.display_info())
print(dvd.display_info())
print(magazine.display_info())
print(book.check_out())
print(book.check_out())
print(book.return_item())
print(dvd.check_out())
print(dvd.return_item())
print(dvd.return_item())
print(magazine.check_out())
