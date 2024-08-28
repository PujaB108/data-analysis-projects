proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
# Below code is run to check if the words in each string in proto_list1 are separated by commas.

if ',' in proto_list1:
    print("Yes, words in each string are seperated by commas in the proto_list1")
else:
    print("No, words in each string are not seperated by commas in the proto_list1")

# Below code is run to check if the words in each string in proto_list2 are separated by semicolons.

if ';' in proto_list2:
    print("Yes, words in each string are seperated by semicolons in the proto_list2")
else:
    print("No, words in each string are not seperated by semicolons in the proto_list2")

# Below code is run to check if the words in each string in proto_list3 are separated by spaces.

if '' in proto_list3:
    print("Yes, words in each string are seperated by spaces in the proto_list3")
else:
    print("No, words in each string are not seperated by spaces in the proto_list3")

# Below code is run to check if the words in each string in proto_list4 are separated by commas.

if ',' in proto_list4:
    print("Yes, words in each string are seperated by commas in the proto_list4")
else:
    print("No, words in each string are not seperated by spaces in the proto_list4")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

proto_list1 = "3,6,9,12"

# Below code splits the string and returns the output ['3','6','9','12']

array = proto_list1.split(",")
print(array)

# Below code reverses the entries and returns the output ['12','9','6','3']

reversed = array[::-1]
print(reversed)

# Below code joins the array into a new comma separated string and returns the output 12,9,6,3

new_string = ','.join(reversed)
print(new_string)


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

proto_list2 = "A;C;M;E"

# Below code splits the string and returns the output ['A','C','M','E']

array = proto_list2.split(";")
print(array)

# Below code alphabetize the entries and returns the output ['A','C','E','M']

array = ['A','C','M','E']
array.sort()
print(array)

# Below code joins the array into a new comma separated string and returns the output A,C,E,M

new_string = ','.join(array)
print(new_string)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

proto_list3 = "space delimited string"

# Below code splits the string and returns the output ['space','delimited','string']

array = proto_list3.split(' ')
print(array)

# Below code alphabetize the entries and returns the output ['delimited','space','string']

array = ['space','delimited','string']
array.sort()
print(array)

# Below code joins the array into a new comma separated string and returns the output delimited space string

new_string = ' '.join(array)
print(new_string)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.

proto_list4 = "Comma-spaces, might, require, typing, caution"

# Below code splits the string and returns the output ['Comma-spaces', ' might', ' require', ' typing', ' caution']

array = proto_list4.split(",")
print(array)

# Below code reverses the entries and returns the output [ caution', ' typing', ' require', ' might', 'Comma-spaces']

reversed = array[::-1]
print(reversed)

# Below code joins the array into a new comma separated string and returns the output caution, typing, require, might,Comma-spaces

new_string = ','.join(reversed)
print(new_string)

# Below code removes the extra spaces in the final string

final_string = new_string.strip()
print(final_string)



