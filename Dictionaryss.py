# 1. Dictionary with Key-Value Pairs
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 2. Accessing Items in a Dictionary
print("Accessing values using keys:")
print(f"Name: {my_dict['name']}") 
print(f"Age: {my_dict['age']}")   
print(f"City: {my_dict['city']}") 
print("\n")

# 3. Adding Items to a Dictionary
my_dict["email"] = "alice@example.com"
print("After adding new item:")
print(my_dict)  
print("\n")

# 4. Empty Dictionary
empty_dict = {}
print("Empty dictionary:")
print(empty_dict)  
print("\n")

# 5. Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}
print("Dictionary comprehension to create squared numbers:")
print(squared_dict) 
print("\n")

# 6. Using .items() Method
print("Using .items() to iterate over dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
print("\n")

# 7. Checking if a Key Exists
if "name" in my_dict:
    print("Key 'name' found in dictionary.")
else:
    print("Key 'name' not found.")
print("\n")

# 8. Updating Values
my_dict["age"] = 26
print("After updating the value of 'age':")
print(my_dict)  
print("\n")

# 9. Removing Items from Dictionary
# Using del
del my_dict["city"]
print("After removing 'city' using del:")
print(my_dict) 
print("\n")

# Using pop() to remove 'age'
removed_value = my_dict.pop("age")
print(f"Removed value of 'age': {removed_value}")
print("After removing 'age' using pop():")
print(my_dict) 
print("\n")

# 10. Nested Dictionary
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 25
    },
    "person2": {
        "name": "Bob",
        "age": 30
    }
}

print("Nested dictionary:")
print(nested_dict)
print("Accessing nested dictionary items:")
print(f"Person1's name: {nested_dict['person1']['name']}")
print(f"Person2's age: {nested_dict['person2']['age']}")
