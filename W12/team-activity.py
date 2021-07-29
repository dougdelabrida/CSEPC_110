largest_number = 0
book_name = None

with open("books_and_chapters.txt") as data:
    for line in data:
        number = int(line.split(":")[1])
        book = line.split(":")[0]

        if number > largest_number:
            largest_number = number
            book_name = book


print(f"The book with more chapters is: {book_name}:{largest_number}")
