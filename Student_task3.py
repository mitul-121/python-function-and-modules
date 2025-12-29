def create_acronym(*args):
    output = ""
    for arg in args:
        output += arg[0]
    return output

print(create_acronym("Code", "Academy", "Lithuania"))
print(create_acronym("Hyper", "Text", "Markup", "Language"))