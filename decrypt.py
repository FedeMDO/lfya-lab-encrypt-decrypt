encrypted = []
desencrypted = []

# encrypt function
def decrypt(char):
    x = ord(char)  # unicode int value of char
    print(x)

    decryptedChar =  (((48 * x) + 45) % 95) + 32
    print(decryptedChar)
    
    return chr(decryptedChar)


# read all file lines
with open('output.txt') as f:
    encrypted = f.readlines()

print(encrypted)

# encrypt
for line in encrypted:
    newLine = ''
    for char in line:
        newLine = newLine + decrypt(char)
    desencrypted.append(newLine)

print(desencrypted)

# save the encrypted content
with open('test.txt', 'w') as f:
    for line in desencrypted:
        f.write(line + '\n')