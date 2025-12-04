import math
# Open input file and read a line.
input = open("2025/Day1/input.txt")
line = input.readline()
# Position of the dial & the # of times the position is set to 0.
pos = 50
counter = 0

# Function that processes the number of times 0 is passed.
def checkDuringRot(pos, num, dir):
    passes = 0

    match dir:
        case -1:
            while ((pos + num * -1) < 0):
                passes += 1
                num -= 100
        case 1:
            while ((pos + num) > 100):
                passes += 1
                num -= 100

    
    return passes


# Main Program
if __name__ == "__main__":
    # While loop to go through all the lines in the input file.
    while line:
        # Get the number from the line.
        num = int(line[1:len(line)])

        # Move dial position based on direction given.
        match line[0]:
            case 'L': # Moves to the left (Negative).
                counter += checkDuringRot(pos, num, -1)
                pos = (pos + num * -1) % 100
            case 'R': # Moves to the right (Positive).
                counter += checkDuringRot(pos, num, 1)
                pos = (pos + num) % 100
                
        # Adds to the counter if the position is 0.
        if (pos == 0): counter += 1
            
        # Reads the next line of the file.
        line = input.readline()

    # Print the answer to the puzzle.
    print(counter)
    


