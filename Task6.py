input1 = ["pineapple", "apple", "orange", "watermelon"]
target_value = "orange1"
target_value1 = "orange"

def index_of_target(strings, target):
    for index, item in enumerate(strings):
        if item == target:
            return index
    return -1

print(index_of_target(input1, target_value))
print(index_of_target(input1, target_value1))