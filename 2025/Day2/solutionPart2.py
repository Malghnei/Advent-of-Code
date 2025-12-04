# Open input file and read first line.
input = open("2025/Day2/input.txt")
line = input.readline()

# Make the input line into a list with ID ranges.
sum = 0

rangeList = line.split(",")

# For loop to go through all ID ranges.
for i in rangeList:
    # Split the minimum and maximum values of the range.
    idRange = i.split("-")
    # For loop to go through every ID in the range.
    for id in range(int(idRange[0]), int(idRange[1]) + 1):
        idString = str(id)
        length = len(idString)
        # For loop to go through every possible repeating amount, starting at 2.
        for j in range(length // 2, 0, -1):
            # Check if the length is divisible by the current repeating amount.
            if length % j == 0:
                checkID = idString[:j]
                # Check if invalid ID.
                if checkID * (length // j) == idString:
                    # Add ID to the sum.
                    sum += id
                    break
print(sum)
