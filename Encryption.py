import sys

# Definitions for usable characters and their numeric values
alpha = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
symbol = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '10'}

# List used to reference for numbers
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Declaring the encrypt
encrypt = []

print('Please enter the data string you would like to be encrypted\n *Use letters, numbers or standard symbols only*')

data = input()

# Encryption functions, currently just adding a flat value of 139 to the numeric value for each character
def alphaEncrypt(let):
    value = int(alpha.get(let)) + 139
    return value

def numEncrypt(num):
    value = int(num) + 139
    return value

def symEncrypt(sym):
    value = int(symbol.get(sym)) + 139
    return value

# Loop goes through and takes each character in the string, identifies it's character type, then runs the appropriate function
for value in data:
    value = value.lower()
    
    if value in alpha:
        encryptValue = alphaEncrypt(value)
        encrypt.append(encryptValue)
        
    elif value in number:
        encryptValue = numEncrypt(value)
        encrypt.append(encryptValue)
        
    elif value in symbol:
        encryptValue = symEncrypt(value)
        encrypt.append(encryptValue)
        
    else:
        print('Sorry this string contains invalid data, please enter a valid data string next time')
        sys.exit()
        
print('Your original input of ' + data + ' was encrypted to:', end = ' ')

# Formats the list into a single string for ease of reading
for i in range(len(encrypt)):
    print(encrypt[i], end = '')
