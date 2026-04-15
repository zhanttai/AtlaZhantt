class Book:
    title: str
    author: str
    pages: int
    is_read: bool

    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        is_read: bool = False,
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def __repr__(self):
        read_status: str = "✅ Прочитана" if self.is_read else "❌ Не прочитана"
        return f"{self.title} - {self.author} | {self.pages} | {read_status}"


def save_books(books: list[Book]) -> None:
    with open(file="./Урок 6/library.txt", mode="w") as file:
        for book in books:
            file.write(f"{book.title}:{book.author}:{book.pages}:{book.is_read}\n")


def load_books() -> list:
    books = []
    with open(file="./Урок 6/library.txt", mode="r") as file:
        for line in file:
            title, author, pages, is_read = line.split(":")
            book = Book(
                title=title,
                author=author,
                pages=int(pages),
                is_read=is_read == "True",
            )
            books.append(book)

    return books


# Пример создания объекта
book = Book("Дюна", "Фрэнк Герберт", 412)


class EBook(Book):
    file_size: float
    file_type: str

    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        file_size: float,
        file_type: str,
        is_read: bool = False,
    ):
        super().__init__(title, author, pages, is_read)
        self.file_size = file_size
        self.file_type = file_type

    def __repr__(self):
        return f"{super().__repr__()} | {self.file_size} MB | {self.file_type}"


class AudioBook(Book):
    duration_hours: float

    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        duration_hours: float,
        is_read: bool = False,
    ):
        super().__init__(title, author, pages, is_read)
        self.duration_hours = duration_hours
    def __repr__(self):
        return f"{super().__repr__()} | {self.duration_hours}"


AudioBook = AudioBook("Дюна", "Челик", 500, 10, True)
AudioBook.mark_as_read()
print(AudioBook)

catalog = [
    Book("Властелин колец", "Толкин", 1200),
    EBook("Дюна", "Фрэнк Герберт", 412, 15.3, str),
    AudioBook("Дюна", "Челик", 500, 10, True), \
]

print (catalog)
