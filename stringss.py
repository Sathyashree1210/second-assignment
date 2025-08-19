# 1. Multiline String (Using triple quotes)
multiline_string = """
Hello, this is a multiline string.
You can write multiple lines like this.
Each new line starts with a newline character.
"""
print("Multiline String:")
print(multiline_string) 
print("\n")

# 2. Heterogeneous String (Strings with different data types)
name = "Alice"
age = 25
height = 5.7
is_student = True

heterogeneous_string = name + " is " + str(age) + " years old, " + str(height) + " feet tall, and is a student: " + str(is_student)
print("Heterogeneous String (String + other data types):")
print(heterogeneous_string)
print("\n")

# 3. String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name 
print("String Concatenation:")
print(full_name)  

# You can also use f-string for concatenation
age = 30
sentence = f"Hello, my name is {first_name} {last_name} and I am {age} years old."
print("Using f-string for Concatenation:")
print(sentence)
print("\n")
