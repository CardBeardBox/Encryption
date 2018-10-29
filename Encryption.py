import sys

# Definitions for usable characters and their numeric values
alpha = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
alpha2 = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}
symbol = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
symbol2 = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}

# List used to reference for numbers
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Declaring the encrypt list
encrypt = []

print('Please enter the data string you would like to be encrypted\n *Use letters, numbers or standard symbols only*')

data = input()

# Encryption functions
def alphaEncrypt(let):
    value = int(alpha.get(let)) + 6
    if value > 26:
        value -= 26
        value = alpha2.get(str(value))
        return value
    else:
        value = alpha2.get(str(value))
        return value

def numEncrypt(num):
    value = int(num) + 6
    if value > 9:
        value -= 9
        return value
    else:
        return value


def symEncrypt(sym):
    value = int(symbol.get(sym)) + 6
    if value > 9:
        value -= 9
        value = symbol2.get(str(value))
        return value
    else:
        value = symbol2.get(str(value))
        return value

# Loop goes through and takes each character in the string, identifies it's character type, then runs the appropriate function
for value in data:
    absValue = value.lower()
    
    if absValue in alpha:
#Check if letter is capitalized or not, so we can make the encrypted letter capitalized as well
        if value.isupper():
            encryptValue = alphaEncrypt(absValue)
            encryptValue = encryptValue.upper()
            encrypt.append(encryptValue)
        else:
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
