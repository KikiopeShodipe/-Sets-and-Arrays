# 1. Create a set with integer elements
integer_set = {1, 2, 3, 4, 5}
print("Set with integer elemens:", integer_set)
# 2. Creat a set with mixed data type elements
mixed_set = {1, "hello", 3.14, True}
print("Set with mixed data types:", mixed_set)
# 3. Create another set with elements - 1, 2, 3, 4, 3, 2
# Duplicate elements are removed automatically in sets
duplicate_set = {1, 2, 3, 4, 3, 2}
print("Set with duplicate elements removed:", duplicate_set)
# 4. Create a set from a list with elements - [1, 2, 3, 2]
list_to_set = set([1, 2, 3, 2])
print("Set created from list:", list_to_set)
# 5. Print the set after removing the first elements from this set - [0, 1, 3, 4, 5]
# Note: Sets are unordered, so we need to convert to list to remove "first" element
original_list = [0, 1, 3, 4, 5]
temp_set = set(original_list)
temp_list = list(temp_set)
temp_list.pop(0)  # remove the first element
new_set = set(temp_list)
print("Set after removing the first element:",new_set)