import json
import book
import customer


class Library:
    def __init__(self):
        self.book_class = book.Book()
        self.customer_class = customer.Customer()
        while True:
            command = input("Enter command: ")
            if command.lower() == "make_loan":
                book_to_loan = input("Enter the Full name of the book: ")
                self.loan(book_to_loan)
            elif command.lower() == "search_book":
                search_book = input("Search for book: ")
                self.book_class.searchbook(search_book)
            elif command.lower() == "search_customer":
                search_customer = input("Search customer: ")
                self.customer_class.search_customer(search_customer)
            elif command.lower() == "append_book":
                author = input("Author: ")
                country = input("Country: ")
                image_link = input("Imagelink: ")
                language = input("Language: ")
                link = input("Link: ")
                pages = input("Number of pages: ")
                title = input("Title: ")
                year = input("Year: ")
                self.book_class.appendbook(author, title, country, image_link, link, int(pages), language, int(year))
                print("Book has been added!")
            elif command.lower() == "append_customer":
                gender = input("Gender: ")
                given_name = input("GivenName: ")
                surname = input("Surname: ")
                street_address = input("Street Address: ")
                zipcode = input("Zipcode: ")
                city = input("city")
                email_address = input("Email: ")
                username = input("Username: ")
                telephone_number = input("Telephone Number: ")
                self.customer_class.add_customer(gender, given_name, surname, street_address, zipcode, city, email_address, username, telephone_number)
                print("Customer added")
            elif command.lower() == "add_new_customer_file":
                self.customer_class.append_data()
                print("New file is now in use!")
            elif command.lower() == "backup":
                self.backup()
                print("Backup has been made!")
            elif command.lower() == "restore_backup":
                self.restore_backup()
                print("Backup has been restored!")
            elif command.lower() == "exit":
                return
            else:
                print("Error finding the command!")

    def loan(self, book_title):
        with open('books.json', 'r') as json_file:
            data = json.load(json_file)
        availability = {"available": False}
        for d in data:
            lowercased_input = book_title.lower()
            if d["title"].lower() == lowercased_input and d["available"] == True:
                object_index = data.index(d)
                d.update(availability)
                print("Loan has been made on book: " + d["title"])
                data.pop(object_index)
                data.append(d)
                json_file.close()
                newFile = open("books.json", "w")
                newFile.write(json.dumps(data, indent=2, sort_keys=True))
            else:
                pass

    def backup(self):
        with open("books.json", "r") as json_books:
            book_data = json.load(json_books)
        with open("customers.json", "r") as json_customers:
            customer_data = json.load(json_customers)

        new_data = {
            "Books": book_data,
            "Customers": customer_data
        }
        json_books.close()
        json_customers.close()
        json_file = open("Backup.json", "w")
        json_file.write(json.dumps(new_data, indent=2, sort_keys=True))

    def restore_backup(self):
        with open("Backup.json") as json_file:
            data = json.load(json_file)
        books = data["Books"]
        Customers = data["Customers"]
        json_books = open("books.json", "w")
        json_books.write(json.dumps(books, indent=2, sort_keys=True))
        json_customers = open("customers.json", "w")
        json_customers.write(json.dumps(Customers, indent=2, sort_keys=True))


x = Library()
