
lines = []
encrypted = []

# encrypt function
def encrypt(char):
    x = ord(char) - 32 # unicode int value of char, no matters 
    print(x)

    encryptedChar = ((2 * x ) + 5) % 95
    print(encryptedChar)
    
    return chr(encryptedChar)


# read all file lines
with open('input.txt') as f:
    lines = f.readlines()

print(lines)

# encrypt
for line in lines:
    newLine = ''
    for char in line:
        newLine = newLine + encrypt(char)
    encrypted.append(newLine)

print(encrypted)

# save the encrypted content
with open('output.txt', 'w') as f:
    for line in encrypted:
        f.write(line)