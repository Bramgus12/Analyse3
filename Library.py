import json
# import csv
# import book
# import customer


class Library:
    def __init__(self):
        # user_input = input("Enter Command: ")
        # if user_input == "loan":
        #     book_title = input("Enter Booktitle: ")
        #     book_search = book.Book.searchbook()
        #     self.loan()
        # elif user_input == "search book":
        #     pass
        # elif user_input == "search customer"
        #     pass
        # else:
        #     return print("error command unkown")
        pass

    def loan(self, book_title):
        with open('books.json', 'r') as json_file:
            data = json.load(json_file)
        availabilty = {"available": False}
        for d in data:
            data_string = str(d)
            lowercased_object = data_string.lower()
            lowercased_input = book_title.lower()
            splitted_input = lowercased_input.split()
            for values in splitted_input:
                if values in lowercased_object and d["available"] == True:
                    object_index = data.index(d)
                    d.update(availabilty)
                    print("fuck off")
                    data.pop(object_index)
                    data.append(d)
                    json_file.close()
                    newFile = open("books.json", "w")
                    backup_file = open("newBooks.json", "w")
                    newFile.write(json.dumps(data, indent=2, sort_keys=True))
                    backup_file.write(json.dumps(data, indent=2, sort_keys=True))
                else:
                    pass
                    print("yeet")


x = Library()
x.loan("Marguerite Yourcenar")
