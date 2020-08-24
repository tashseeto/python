class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = 1
        self.bookmark = 1

    def bookmark_page(self):
        self.bookmark = self.current_page

    def turn_page(self, forward):
        if forward:
            self.current_page += 1
        else:
            self.current_page -= 1

    def __len__(self):
        return self.num_pages
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Bookmark at page {self.bookmark}"

'''classes are like blue prints'''
'''dunda call like a function'''
'''method use dot notation'''

google_book = Book("How Google Works", "Google Founders", 200)
print(len(google_book))
print(google_book)
# print(google_book)
# print(google_book.current_page)
# google_book.turn_page(True)
# print(google_book.current_page)
# google_book.bookmark_page()
# print(google_book.bookmark)
# # google_book.turn_page(False)
# google_book.turn_page(False)
# print(google_book.current_page)


# print(google_book.title)
# print(google_book.author)
# print(google_book.num_pages)


# hitchhikers_guide = Book("Hitchhikers Guide", "D Adams", 350)
# print(hitchhikers_guide)

# print(google_book.num_pages)


# inspirational_women = Book("200 Women", "Blackwell", 200)
# print(inspirational_women)

