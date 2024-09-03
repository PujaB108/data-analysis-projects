# Part 1 A -- Make a Line
# This function returns a string of length size (5)

def make_line(size):
    line = ""
    for i in range(size):
        line = line + "#"
    return line

print(make_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
# This function creates a square of size (5) using the  'make_line' function.

def make_line(size):
    line = ""
    for i in range(size):
        line = line + "#"
    return line

def make_square(size):
   square = ""
   for i in range(size):
      square = square + make_line(size) + "\n"
   return square

print(make_square(5))

# Part 1 C -- Make a Rectangle
# This function creates a rectangle of size (width [3], height[5]) x using the  'make_line' function.

def make_line(size):
    line = ""
    for i in range(size):
        line = line + "#"
    return line

def make_rectangle(width, height):
   rectangle = ""
   for i in range(height):
      rectangle = rectangle + make_line(width) + "\n"
   return rectangle

print(make_rectangle(5,3))

# Part 2 A -- Make a Stairs
# This function creates the staircase pattern with the given height, using the make_line function

def make_line(size):
    line = ""
    for i in range(size):
        line = line + "#"
    return line

def make_downward_stairs(height):
   stairs = ""
   for i in range(height):
      stairs = stairs + make_line(i+1) + "\n"
   return stairs

print(make_downward_stairs(5))

# Part 2 B -- Make Space-Line 
# This function returns a line with exactly 3 spaces, followed by 5 hashes, followed again by 3 more spaces.

def make_space_line(num_spaces, num_chars):
    spaces = ' ' * num_spaces
    hashes = '#' * num_chars
    return spaces + hashes + spaces

print(make_space_line(3,5))

# Part 2 C -- Make Isosceles Triangle
# The function returns an isosceles triangle of a given height.

def make_space_line(num_spaces, num_chars):
    spaces = ' ' * num_spaces
    hashes = '#' * num_chars
    return spaces + hashes + spaces

def make_isosceles_triangle(height):
   triangle = ""
   for i in range(height):
      spaces = height -i -1
      hashes = 2 * i + 1
      triangle = triangle + make_space_line(spaces, hashes) + "\n"
   return triangle

print(make_isosceles_triangle(5))

# Part 3 -- Make a Diamond
# The function returns a diamond where the triangle formed by the top portion has the given height (5)

def make_diamond(height):
    diamond = ""
    for i in range(height):
        diamond = diamond + ' ' * (height - i - 1) + '#' * (2 * i + 1) + '\n'
    for i in range(height - 2, -1, -1):
        diamond = diamond + ' ' * (height - i - 1) + '#' * (2 * i + 1) + '\n'
    return diamond

print(make_diamond(5))

      