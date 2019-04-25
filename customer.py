import csv
import json


class Customer:
    def __init__(self):
        pass

    def append_data(self):
        csv_file = open("FakeNameSet20.csv", "r")
        json_file = open("customers.json", "w")
        fieldnames = ("Number", "Gender", "NameSet", "GivenName", "Surname", "StreetAddress", "ZipCode", "City", "EmailAddress","Username", "TelephoneNumber")
        reader = csv.DictReader(csv_file, fieldnames)
        out = json.dumps([row for row in reader], indent=4, sort_keys=True)
        json_file.write(out)
        json_file.close()
        csv_file.close()

    def add_customer(self, gender, name_set, given_name, surname, street_address, zip_code, city, email_address, username, telephone_number, number=0,):
        with open("customer.json", 'r') as json_file:
            customer_data = json.load(json_file)
        customer_dictionary = {
            "Number": number,
            "Gender": gender,
            "NameSet": name_set,
            "GivenName": given_name,
            "Surname": surname,
            "StreetAddress": street_address,
            "ZipCode": zip_code,
            "City": city,
            "EmailAddress": email_address,
            "Username": username,
            "TelephoneNumber": telephone_number,
        }
        json_file.close()
        new_data = customer_data.append(customer_dictionary)
        outfile = open('customer', "w")
        outfile.write("")
        outfile.write(json.dumps(new_data, indent=4, sort_keys=True))
        outfile.close()


    def search_customer(self):
        with open('customers.json', 'r') as json_file:
            data = json.load(json_file)
        s1 = ''
        user_input = input("Search for customer: ")
        for d in data:
            data_string = str(d)
            lowercased_object = data_string.lower()
            lowercased_input = user_input.lower()
            splitted_input = lowercased_input.split()
            for values in splitted_input:
                if values in lowercased_object:
                    s = d["Gender"] + "," + d["Number"] + "," + d["NameSet"] + "," + d["GivenName"] + "," + d["Surname"] + "," + d["StreetAddress"] + "," + d["ZipCode"] + "," + d["City"] + "," + d["EmailAddress"] + "," + d["Username"] + "," + d["TelephoneNumber"] + "\n" + "------------------------------------------------------------------------------------" + "\n"
                    if s in s1:
                        pass
                    else:
                        s1 = s1 + s
        print(s1)


x = Customer()
x.append_data()
x.search_customer()
