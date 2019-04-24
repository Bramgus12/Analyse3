import csv, json

csvfile = open("/home/bram/Documents/GitHub/Analyse3/Analysis3/FakeNameSet20.csv", "r")
jsonfile = open("/home/bram/Documents/GitHub/Analyse3/Analysis3/customers.json", "w")

fieldnames = ("Number","Gender","NameSet","GivenName","Surname","StreetAddress","ZipCode","City","EmailAddress","Username","TelephoneNumber")
reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps([row for row in reader], indent=4, sort_keys=True)
jsonfile.write(out)
