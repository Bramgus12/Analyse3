import json
with open('books.json', 'r') as json_file:
    data = json.load(json_file)

class Book:
    def __init__(self):
        pass

    def appendBook(self, author, Title, country, image_link, link, number_of_pages, language, year):
        Dict = {
            "author": author,
            "country": country,
            "imageLink": image_link,
            "language": language,
            "link": link + "\n",
            "pages": number_of_pages,
            "title": Title,
            "year": year
        }
        newData = data
        newData.append(Dict)

        outfile = open('newBooks.json', "w")
        outfile.write("")
        outfile.write(json.dumps(newData, indent=4, sort_keys=True))
        outfile.close()
    
    def searchBook(self):
        with open('books.json', 'r') as json_file:
            data = json.load(json_file)
        s1 = ''
        Userinput = input("Search for a book: ")
        for d in data:
            dataString = str(d)
            lowercasedObject = dataString.lower()
            lowercasedInput = Userinput.lower()
            splittedInput = lowercasedInput.split()
            for values in splittedInput:
                if values in lowercasedObject:
                    s = d["author"]+  ", " + d["country"]+  ", " + d["imageLink"]+  ", " + d["language"]+  ", " + d["link"] +  ", " + str(d["pages"])+  ", " + d["title"]+  " and "+ str(d["year"]) + "\n" + "----------------------------------------------------------------------------" + "\n"
                    if s in s1:
                        print("")
                    else:
                        s1 = s1 + s
        print(s1)


x = Book()
x.searchBook()
