def create_email(first_name, last_name, domain="codeacademy.lt"):
    first_name = first_name.lower().replace(" ", "")
    last_name = last_name.lower().replace(" ", "")
    return f"{first_name}.{last_name}@{domain}"

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(create_email(first_name, last_name))