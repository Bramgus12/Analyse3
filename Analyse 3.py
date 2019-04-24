import json
Userinput = input("Search for a book: ")
with open('books.json', 'r') as json_file:
    data = json.load(json_file)
    for d in data:
        a = str(d)
        b = a.lower()
        c = Userinput.lower()
        if c in b:
            print(d)


# class Book:
#     def __init__(self):


    # def __init__(self, ISBN, Title, summary, publisher, publication_date, number_of_pages, language):
    #     self.ISBN = ISBN
    #     self.Title = Title
    #     self.summary = summary
    #     self.publisher = publisher
    #     self.publication_date = publication_date
    #     self.number_of_pages = number_of_pages
    #     self.language = language

    
    # def getISBN(self):
    #     return self.ISBN
    
    # def getTitle(self):
    #     return self.Title
    
    # def getSummary(self):
    #     return self.summary
    
    # def getPublisher(self):
    #     return self.publisher
    
    # def getPublicationDate(self):
    #     return self.publication_date
    
    # def getNumberOfPages(self):
    #     return self.number_of_pages

    # def getLanguage(self):
    #     return self.language

    # def showData(self):
    #     print(self.ISBN)
    #     print(self.Title)
    #     print(self.summary)
    #     print(self.publisher)
    #     print(self.publication_date)
    #     print(self.number_of_pages)
    #     print(self.language)
