# Open the input file and read a line.
file = open("2025/Day3/input.txt")
line = file.readline()

# Variables to record the maximun and sum values.
max = 0
sum = 0

# While loop to go through every line in the input file.
while line:
    line = line.strip()
    # First for loop for the first digit.
    for i in range(0, len(line)):
        first = int(line[i])
        # Second for loop for the second digit.
        for j in range(i + 1, len(line)):
            second = int(line[j])
            # Compare to the max value if there is any.
            if (first * 10 + second) > max:
                max = first * 10 + second
    # Increment the maximum value found in the line to the sum.
    sum += max
    max = 0 # Reset maximum value.
    line = file.readline()

print(sum)
    
