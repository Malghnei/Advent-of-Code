# Open the input file and read a line.
file = open("2025/Day3/input.txt")
line = file.readline()

# Variables to record the maximum and sum values.
max = 0
sum = 0

# While loop to go through every line in the input file.
while line:
    # Remove newline characters
    line = line.strip()  

    # Reset values
    maxValue = 0
    curr = 0
    end = len(line)

    # Find all 12 digits
    for i in range(11, -1, -1):
        # Find the greatest digit in the given interval
        for j in range(curr, end - i):
            if max < int(line[j]):
                max = int(line[j])
                curr = j + 1
        # Add the greatest digit to the final value
        maxValue = maxValue * 10 + max
        max = 0


    # Add final value to the total sum
    sum += maxValue
    line = file.readline()

print(sum)

