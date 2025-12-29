Firstname = input("Enter your first name: ")
Lastname = input("Enter your last name: ")

def formate_name(firstname, lastname):
    firstname = firstname.title()
    lastname = lastname.title()
    return f"{firstname}, {lastname}"

print(formate_name(Lastname, Firstname))