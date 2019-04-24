import json
Userinput = input("Search for a book: ")
with open('books.json', 'r') as json_file:
    data = json.load(json_file)
    s1 = ''
    for d in data:
        dataString = str(d)
        lowercasedObject = dataString.lower()
        lowercasedInput = Userinput.lower()
        splittedInput = lowercasedInput.split()
        for values in splittedInput:
            if values in lowercasedObject:
                s = d["author"]+  ", " + d["country"]+  ", " + d["imageLink"]+  ", " + d["language"]+  ", " + d["link"]+  ", " + str(d["pages"])+  ", " + d["title"]+  " and "+ str(d["year"]) + "\n" + "8=======================================================================D~~~~~~" + "\n"
                if s in s1:
                    print("")
                else:
                    s1 = s1 + s
    print(s1)
    print()