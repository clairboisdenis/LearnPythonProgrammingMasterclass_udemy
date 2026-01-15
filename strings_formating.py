for i in range (1, 13):
    print(i)

for j in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2} ".format(j, j ** 2, j ** 3))

for k in range(1, 14):
    print("N° {0:3} squared = {1:6} and cubed = {2:4}".format(k, k ** 2, k ** 3))

for l in range(1, 14):
    print("N° {0:<3} squared = {1:<6} and cubed = {2:<8}".format(l, l ** 2, l ** 3))

for m in range(1, 14):
    print("N° {0:<3} squared = {1:<6} and cubed = {2:^8}".format(m, m ** 2, m ** 3))

print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:^72.50f}".format(22/7))
print("Pi is approximately {0:12}".format(22/7))

for m in range(1, 14):
    print("N° {0:<3} squared = {1:<6} and cubed = {2:^8}".format(m, m ** 2, m ** 3))


