computer_parts = ["computer",
                  "monitor",
                  "keybaord",
                  "mouse",
                  "mouse mat",
                  "usb port"]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print(computer_parts[:])

print(computer_parts[:3])

print(computer_parts[-1])

computer_parts[3] = "trackball"

print(computer_parts)
computer_parts.append(["mouse", "usbc port", "NIC"])
print(computer_parts)
computer_parts.remove(["mouse", "usbc port", "NIC"])
print(computer_parts)

computer_parts[3] = "mouse"
print(computer_parts[3:])

#different slide =  different effect
computer_parts[3:] = "trackball"
print(computer_parts)

computer_parts[3:] = ["trackball", "usb port", "NIC"]
print(computer_parts)







