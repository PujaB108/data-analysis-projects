my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.
# Below code returns the output nchCodeLau

new_string = my_string[3:] + my_string[:3]
print(new_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
# Below code returns the output - The original string is 'LaunchCode' and the modified string is 'nchCodeLau'. 

print(f"The original string is '{my_string}' and the modified string is '{new_string}'. ")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
# Get user input for the string
my_string = input("Enter a string: ")

# Get user input for the number of letters to relocate
num_letters = int(input("Enter the number of letters to remove and add to the end: "))

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
if num_letters > len(my_string):
    num_letters = 3
    error_message = "Error: The number of letters to relocate was longer than the string length, must be only 3."
else:
    error_message = ""

print(f"The original string is '{my_string}', and the modified string is '{new_string}'. {error_message}")