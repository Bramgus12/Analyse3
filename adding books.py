import json
with open('books.json', 'r') as json_file:
    data = json.load(json_file)

class Book:
    def __init__(self, author, Title, country, image_link, link, number_of_pages, language, year):
        self.author = author
        self.Title = Title
        self.country = country
        self.image_link = image_link
        self.link = link
        self.number_of_pages = number_of_pages
        self.language = language
        self.year = year

    def appendBook(self):
        Dict = {
            "author": self.author,
            "country": self.country,
            "imageLink": self.image_link,
            "language": self.language,
            "link": self.link + "\n",
            "pages": self.number_of_pages,
            "title": self.Title,
            "year": self.year
        }
        newData = data
        newData.append(Dict)

        outfile = open('newBooks.json', "w")
        outfile.write("")
        outfile.write(json.dumps(newData, indent=4, sort_keys=True))
        outfile.close()


x = Book("test", "test", "test", "test", "test", "test", "test", "test")
x.appendBook()