# " outlier" = valeur abérrante

data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

del data[:2]  # == del data[0:2]
print(data)

del data[-2:]
print(data)

data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

for index, value in enumerate(data):
    print(f"- index = {index} -- value : {value}")

##### ERROR

for index, value in enumerate(data):
    if (data[index] < min_valid) or (data[index] > max_valid):
        del data[index]
else:
    print(data)

# Solution 1 :
# data = list(filter(lambda x: min_valid <= x <= max_valid, data))

# solution 2 :
# data = [x for x in data if min_valid <= x <= max_valid]

#########  solution3 ###############

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







