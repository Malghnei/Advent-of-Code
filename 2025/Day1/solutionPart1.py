# Open input file and read a line.
input = open("2025/Day1/input.txt")
line = input.readline()
# Position of the dial & the # of times the position is set to 0.
pos = 50
counter = 0

# While loop to go through all the lines in the input file.
while line:
    # Get the number from the line.
    num = int(line[1:len(line)])

    # Move dial position based on direction given.
    match line[0]:
        case 'L': # Moves to the left (Negative)
            pos = (pos + num * -1) % 100
        case 'R': # Moves to the right (Positive)
            pos = (pos + num) % 100

    # Adds to the counter if the position is 0.
    if (pos == 0): counter += 1
        
    # Reads the next line of the file.
    line = input.readline()

# Print the answer to the puzzle.
print(counter)

    


