import json
import rhinoscriptsyntax as rs

filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open JSON File", filter)

class Book:
    def __init__(self, ISBN, Title, summary, publisher, publication_date, number_of_pages, language):
        self.ISBN = ISBN
        self.Title = Title
        self.summary = summary
        self.publisher = publisher
        self.publication_date = publication_date
        self.number_of_pages = number_of_pages
        self.language = language

    
    def getISBN(self):
        return self.ISBN
    
    def getTitle(self):
        return self.Title
    
    def getSummary(self):
        return self.summary
    
    def getPublisher(self):
        return self.publisher
    
    def getPublicationDate(self):
        return self.publication_date
    
    def getNumberOfPages(self):
        return self.number_of_pages

    def getLanguage(self):
        return self.language

    def showData(self):
        print(self.ISBN)
        print(self.Title)
        print(self.summary)
        print(self.publisher)
        print(self.publication_date)
        print(self.number_of_pages)
        print(self.language)

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def getName(self):
        return self.name
    
    def getBiography(self):
        return self.biography