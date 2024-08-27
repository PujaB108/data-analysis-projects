# # Create the adding_practice list with the following entry: 273.15
# The code below returns the output [273.15]

adding_practice = [273.15]
print(adding_practice)

# # # Use the append method to add the number 42 and the string "hello" to the list. Add these new items one at a time.  Print the list after each step to confirm the changes.
# # The code below returns the output [273.15, 42]

adding_practice.append(42)
print(adding_practice)

# The code below returns the output [273.15, 42, 'hello']

adding_practice.append("hello")
print(adding_practice)

# # Use list concatenation to add these three items to the list all at once: [False, -4.6, '87'].
# The code below returns the output [False, -4.6, '87']

new_list = [False, -4.6, '87']
print(new_list)

# The code below returns the output [273.15, 42, 'hello', False, -4.6, '87']

print(adding_practice + new_list)

# # Use the cargo_hold list for the next set of exercises.
cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']

# # Use bracket notation to replace 'slinky' in the list with 'space tether'. Print the list to confirm the change.
# The code below returns the output ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'space tether', 'security blanket']
cargo_hold[-2] = 'space tether'
print(cargo_hold)

# # Remove the last item from the list with pop. Print the element removed and the updated list.
# # The code below returns the output ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'space tether']

last_removed_item = cargo_hold.pop()
print(last_removed_item)
print(cargo_hold)

# # Remove the first item from the list with pop. Print the element removed and the updated list.
# # The code below returns the output ['space suits', 'parrot', 'instruction manual', 'meal packs', 'space tether']

first_removed_item = cargo_hold.pop(0)
print(first_removed_item)
print(cargo_hold)

# # append and insert require arguments inside the (). Add the items 1138 and ‘20 meters’ to the the list - the number at the start and the string at the end. Print the updated list to confirm the changes.
# # # The code below returns the output [1138, 'space suits', 'parrot', 'instruction manual', 'meal packs', 'space tether']

cargo_hold.insert(0, 1138)
print(cargo_hold)

# The code below returns the output [1138, 'space suits', 'parrot', 'instruction manual', 'meal packs', 'space tether', '20 meters']

cargo_hold.append('20 meters')
print(cargo_hold)

# Use the remove method to take the parrot out of cargo_hold, then print the updated list.
# The code below returns the output [1138, 'space suits', 'instruction manual', 'meal packs', 'space tether', '20 meters']

cargo_hold.remove('parrot')
print(cargo_hold)

# Use .format() to print the final list and its length. "The list ___ contains ___ items."
# The code below returns the output - The list [1138, 'space suits', 'instruction manual', 'meal packs', 'space tether', '20 meters'] has 6 items.

print("The list {} has {} items.".format(cargo_hold, len(cargo_hold)))