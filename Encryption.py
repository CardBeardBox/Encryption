import random

# Definitions for usable characters and their numeric values, used as references by encryption function
alpha = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}
alphaKey = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '10': 'k', '11': 'l', '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's', '19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z'}
symbol = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
symbolKey = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}

# List used to reference for numbers
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Declaring the variable to be used for displaying the encrypted data
encryptedString = []

# Encryption function 1    
def encFunc_1(character, encKey):
    alphaValue = 0
        
    if character in alpha:
        alphaValue = int(alpha.get(character))
        encChar = int(alpha.get(character)) + encKey
        encChar %= 25
        encryptData = alphaKey.get(str(encChar))
        return encryptData
    
    elif character in symbol:
        encChar = int(symbol.get(character)) + encKey
        encChar %= 10
        encryptData = symbolKey.get(str(encChar))
        return encryptData
    
    elif character in number:
        encChar = int(character) + encKey
        encChar %= 10
        encryptData = encChar
        return encryptData

# Encryption function 2    
def encFunc_2(character, encKey):

    if character in alpha:
        encChar = int(alpha.get(character)) - (encKey * 2)
        encChar %= 25
        encryptData = alphaKey.get(str(encChar))
        return encryptData.upper()
    elif character in symbol:
        encChar = int(symbol.get(character)) + encKey
        encChar %= 10
        encryptData = symbolKey.get(str(encChar))
        return encryptData
    elif character in number:
        encChar = int(character) + encKey
        encChar %= 10
        encryptData = encChar
        return encryptData

# Ask for user input     
print('Please enter the data string you would like to be encrypted\n')
data = input()

# Loop to make sure correct data params are met
while len(data) < 6:
    print('Sorry the input data string is too short, try again with atleast 6 characters\n')
    print('Please enter the data string you would like to be encrypted\n')
    data = input()

# Loop takes each character through the encrypt functions
for character in data:
    character = character.lower()
    encKey = len(data) - 5
    encFunc = random.randint(1, 4)
    
    if character == ' ':
        encryptedString.append(' ')
        
    elif encFunc < 4:
        encryptedChar = encFunc_1(character, encKey)
        encryptedString.append(encryptedChar)
        
    elif encFunc == 4:
        encryptedChar = encFunc_2(character, encKey)
        encryptedString.append(encryptedChar)

# Displays result after converting to a single string for ease of reading      
print('Your original input of ' + data + ' was encrypted to:', end = ' ')
for i in range(len(encryptedString)):
    print(encryptedString[i], end = '')
