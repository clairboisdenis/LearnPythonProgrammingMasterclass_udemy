data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

stop = None

# Process the lowest value

for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# process the highest value

start = None

for index in range(len(data) -1, -1, -1):
    #print(index)
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
print(data[start])
del data[start:]
print(data)
