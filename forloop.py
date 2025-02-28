students = {
    "male":["Tom","Charlie","Harry","Frank"],
    "female":["Kavita","Sakshi","Pratiksha","Mahi","Bhairavi"]
    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
