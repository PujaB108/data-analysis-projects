# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
# Below code returns the output [Strings_are_]

new_text = text[0 : 12]
print(new_text)

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
# Below code returns the output [_characters.]

text = 'Strings_are_sequences_of_characters.'
new_text = text[-12:]
print(new_text)

# 3. Print a slice of the middle 12 characters from 'text'.
# Below code returns the output that there are 36 characters in the string. 

text = 'Strings_are_sequences_of_characters.'
print(len(text))

# To print middle 12 characters, the start_index will be 12 and end_index will be 24
# Below code returns the output [sequences_of]

text = 'Strings_are_sequences_of_characters.'
new_text = text[12 : 24]
print(new_text)


# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
# Method 1
word = 'tomato'

for word in 'tomato':
    print(word)

# Method 2
word = 'tomato'

for index in range(len(word)):
    print (word[index])

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
# Below codes in Method 1 and 2 returns the output [otamot]
# Method 1
word = 'tomato'
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print(reversed_word)

# Method 2
word = 'tomato'
reversed_word = ""

for index in word:
    reversed_word = index + reversed_word
print(reversed_word)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
# Below code returns the desired output 'tomato | otamot'
word = 'tomato'
reversed_word = ""

for index in word:
    reversed_word = index + reversed_word
print(word, '|', reversed_word)