# Open input file and read first line.
input = open("2025/Day2/input.txt")
line = input.readline()
# Holds the sum of the IDs.
sum = 0

# Make the input line into a list with ID ranges.
rangeList = line.split(",")

# For loop to go through all ID ranges.
for i in rangeList:
    # Split the minimum and maximum values of the range.
    idRange = i.split("-")
    # For loop to go through every ID in the range.
    for id in range(int(idRange[0]), int(idRange[1]) + 1):
        idString = str(id)
        # Check if the length is even.
        if len(idString) % 2 == 0:
            # Check if the first half is equal to the second half of the ID.
            if idString[0:int(len(idString)/2)] == idString[int(len(idString)/2):len(idString)]:
                # Add ID to the sum.
                sum += id 
print(sum)
