# 1. Empty Tuple
empty_tuple = ()
print("Empty Tuple:")
print(empty_tuple)  
print("\n")

# 2. Slicing a Tuple
sample_tuple = (10, 20, 30, 40, 50)
sliced_tuple = sample_tuple[1:4]
print("Sliced Tuple (from index 1 to 3):")
print(sliced_tuple)  
print("\n")

# 3. Nested Tuple
nested_tuple = (1, 2, (3, 4, 5), (6, 7))
nested_element = nested_tuple[2][1]  
print("Nested Tuple:")
print(nested_tuple)  
print("Accessed nested element (nested_tuple[2][1]):")
print(nested_element)  
print("\n")

# 4. Finding Maximum and Minimum in a Tuple
num_tuple = (15, 20, 10, 30, 25)
max_value = max(num_tuple)
min_value = min(num_tuple)

print("Tuple to find max and min values:")
print(num_tuple)  
print(f"Maximum Value: {max_value}")  
print(f"Minimum Value: {min_value}")  
