# 1. Empty Set
empty_set = set()
print("Empty Set:")
print(empty_set)  
print("\n")

# 2. Overlapping Set 
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Overlapping Sets:")
print(f"Set A: {set_a}")  
print(f"Set B: {set_b}")  
print("\n")

# 3. Finite Set
finite_set = {10, 20, 30, 40, 50}
print("Finite Set:")
print(finite_set)  
print("\n")

# 4. Infinite Set 
infinite_set = set(range(1, 11))  
print("Infinite Set (Limited Representation):")
print(infinite_set)  
print("\n")

# 5. Union of Two Sets 
union_set = set_a.union(set_b)
print("Union of Set A and Set B:")
print(union_set)  
print("\n")

# 6. Intersection of Two Sets
intersection_set = set_a.intersection(set_b)
print("Intersection of Set A and Set B:")
print(intersection_set)  
print("\n")

# 7. Updating a Set 
set_a.update({5, 6})
print("Set A after updating with {5, 6}:")
print(set_a) 
print("\n")
