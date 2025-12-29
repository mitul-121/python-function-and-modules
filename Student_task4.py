def parse_full_name(full_name):
    print(full_name)
    dictionary = {"title" : "None", "first_name" : "", "middle_name" : "", "last_name" : "", "suffix" : "None"}
    titles = ["Dr.", "Mr.", "Ms.", "Mrs.", "Prof."]
    suffixes = ["Jr.", "Sr.", "III", "IV"]
    full_name = full_name.split(" ")

    if full_name[0] not in titles:
        dictionary["title"] = "None"
        dictionary["first_name"] = full_name[0]
        if len(full_name) < 3:
            if full_name[1] in suffixes:
                dictionary["suffix"] = full_name[1]
            else:
                dictionary["last_name"] = full_name[1]
        elif len(full_name) < 4:
            if full_name[2] in suffixes:
                dictionary["suffix"] = full_name[2]
                dictionary["last_name"] = full_name[1]
            else:
                dictionary["last_name"] = full_name[2]
                dictionary["middle_name"] = full_name[1]
        elif len(full_name) < 5:
            if full_name[3] in suffixes:
                dictionary["suffix"] = full_name[3]
                dictionary["last_name"] = full_name[2]
                dictionary["middle_name"] = full_name[1]
            else:
                dictionary["last_name"] = full_name[3]
                dictionary["middle_name"] = full_name[2]
                dictionary["middle_name"].append(full_name[1])
    else:
        dictionary["title"] = full_name[0]
        dictionary["first_name"] = full_name[1]
        if len(full_name) < 4:
            if full_name[2] in suffixes:
                dictionary["suffix"] = full_name[2]
            else:
                dictionary["last_name"] = full_name[2]
        elif len(full_name) < 5:
            if full_name[3] in suffixes:
                dictionary["suffix"] = full_name[3]
                dictionary["last_name"] = full_name[2]
            else:
                dictionary["last_name"] = full_name[3]
                dictionary["middle_name"] = full_name[2]
        elif len(full_name) < 6:
            if full_name[4] in suffixes:
                dictionary["suffix"] = full_name[4]
                dictionary["last_name"] = full_name[3]
                dictionary["middle_name"] = full_name[2]
            else:
                dictionary["last_name"] = full_name[4]
                dictionary["middle_name"] = full_name[3]
                dictionary["middle_name"].append(full_name[2])
    return  dictionary

def format_name_formal(name_dict):
    name_dict["last_name"] = name_dict["last_name"].upper() + ","
    if name_dict["suffix"] == "None":
        print(" ".join(s for s in [name_dict["last_name"],name_dict["first_name"],name_dict["middle_name"]] if s))
    else:
        print(" ".join(s for s in [name_dict["last_name"], name_dict["first_name"], name_dict["middle_name"], name_dict["suffix"]] if s))

print(parse_full_name("Dr. John Paul Smith Jr."))
format_name_formal(parse_full_name("Dr. John Paul Smith Jr."))
print("*"*20)
print(parse_full_name("John Paul Smith Jr."))
format_name_formal(parse_full_name("John Paul Smith Jr."))
print("*"*20)
print(parse_full_name("John Paul Smith"))
format_name_formal(parse_full_name("John Paul Smith"))
print("*"*20)
print(parse_full_name("John Smith"))
format_name_formal(parse_full_name("John Smith"))
print("*"*20)
print(parse_full_name("Dr. John Jr."))
format_name_formal(parse_full_name("Dr. John Jr."))
print("*"*20)
print(parse_full_name("Dr. John Smith Jr."))
format_name_formal(parse_full_name("Dr. John Smith Jr."))
print("*"*20)



