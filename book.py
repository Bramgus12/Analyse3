import json


class Book:

    def __init__(self):
        with open('books.json', 'r') as json_file:
            self.data = json.load(json_file)

    def appendbook(self, author, title, available, country, image_link, link, number_of_pages, language, year):
        dictionary = {
            "author": author,
            "available": True,
            "country": country,
            "imageLink": image_link,
            "language": language,
            "link": link + "\n",
            "pages": number_of_pages,
            "title": title,
            "year": year
        }
        new_data = self.data
        new_data.append(dictionary)

        outfile = open('newBooks.json', "w")
        outfile.write("")
        outfile.write(json.dumps(new_data, indent=4, sort_keys=True))
        outfile.close()
    
    def searchbook(self):
        with open('books.json', 'r') as json_file:
            data = json.load(json_file)
        s1 = ''
        Userinput = input("Search for a book: ")
        for d in data:
            data_string = str(d)
            lowercased_object = data_string.lower()
            lowercased_input = Userinput.lower()
            splitted_input = lowercased_input.split()
            for values in splitted_input:
                if values in lowercased_object:
                    s = d["author"] + ", " + str(d["available"]) + ", " + d["country"] + ", " + d["imageLink"] + ", " + d["language"] + ", " + d["link"] + ", " + str(d["pages"]) + ", " + d["title"] + " and " + str(d["year"]) + "\n" + "----------------------------------------------------------------------------" + "\n"
                    if s in s1:
                        pass
                    else:
                        s1 = s1 + s
        print(s1)


x = Book()
x.searchbook()
