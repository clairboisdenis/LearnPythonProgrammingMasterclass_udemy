result = True
another_result = result

print(id(result))
print(id(another_result))

print(type(result))

result = False
print(id(result))
