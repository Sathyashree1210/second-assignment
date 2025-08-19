# 1. Homogeneous List 
homogeneous_list = [10, 20, 30, 40, 50]
print("Homogeneous List:")
print(homogeneous_list)  
print("\n")

# 2. Heterogeneous List 
heterogeneous_list = ["Alice", 25, 5.7, True]
print("Heterogeneous List:")
print(heterogeneous_list) 
print("\n")

# 3. Singleton List 
singleton_list = [100]
print("Singleton List:")
print(singleton_list)  
print("\n")

# 4. Empty List
empty_list = []
print("Empty List:")
print(empty_list)  
print("\n")

# 5. Indexing a List 
print("Accessing elements by index:")
print(f"First element: {homogeneous_list[0]}")  
print(f"Last element: {homogeneous_list[-1]}")  
print("\n")

# 6. Insert an Element at a Specific Index
homogeneous_list.insert(2, 35)  
print("List after inserting 35 at index 2:")
print(homogeneous_list)  
print("\n")

# 7. Append an Element at the End of the List
homogeneous_list.append(60)  
print("List after appending 60:")
print(homogeneous_list)  
print("\n")

# 8. Extend a List by Adding Elements from Another List
additional_list = [70, 80]
homogeneous_list.extend(additional_list)  
print("List after extending with [70, 80]:")
print(homogeneous_list)  
print("\n")

# 9. Pop an Element from the List 
popped_element = homogeneous_list.pop()  
print("Popped element:", popped_element)  
print("List after popping an element:")
print(homogeneous_list) 
print("\n")

# 10. Clear all Elements in the List
homogeneous_list.clear()
print("List after clearing all elements:")
print(homogeneous_list)  
print("\n")

# 11. Count Occurrences of an Element in a List
homogeneous_list = [10, 20, 30, 10, 40, 10]
count_of_10 = homogeneous_list.count(10)  
print("List to count elements:")
print(homogeneous_list)  
print(f"Count of 10 in the list: {count_of_10}")
