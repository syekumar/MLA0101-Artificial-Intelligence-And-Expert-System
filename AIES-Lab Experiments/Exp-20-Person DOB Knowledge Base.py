# Person DOB Knowledge Base

dob = {
    "Rahul": "15-08-2002",
    "Anita": "20-01-2003",
    "Kiran": "10-12-2001",
    "Priya": "05-06-2004"
}

name = input("Enter person's name: ")

if name in dob:
    print("Name :", name)
    print("Date of Birth :", dob[name])
else:
    print("Person not found in the Knowledge Base")
