import sys, random

# Definitions for usable characters and their numeric values, used as references by encryption function
alpha = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}
alpha2 = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '10': 'k', '11': 'l', '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's', '19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z'}
symbol = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
symbol2 = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}

# List used to reference for numbers
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Declaring the variable to be used for displaying the encrypted data
encryptString = []

# Encryption functions, random number generator to pick which one to use
def encryption(character, encKey):
    encFunc = random.randint(1, 2)

# Encryption function 1    
    if encFunc == 1:
        alphaValue = 0
        
        if character in alpha:
            alphaValue = int(alpha.get(character))
            encChar = int(alpha.get(character)) + encKey - 1
        elif character in symbol:
            encChar = int(symbol.get(character)) + encKey - 1
        elif character in number:
            encChar = int(character) + encKey - 1

        encType = random.randint(1, 3)
  
        if alphaValue > 9:
            encChar = encChar % 25
            encryptData = alpha2.get(str(encChar))
            return encryptData

        elif encType == 1:
            encChar = encChar % 10
            encryptData = alpha2.get(str(encChar))
            return encryptData

        elif encType == 2:
            encChar = encChar % 10
            encryptData = symbol2.get(str(encChar))
            return encryptData
        
        elif encType == 3:
            encChar = encChar % 10
            encryptData = str(encChar)
            return encryptData
            
        else:
            print('Error: Category value ' + category)

# Encryption function 2    
    elif encFunc == 2:

        if character in alpha:
            encChar = int(alpha.get(character)) + (encKey * 2)            
        elif character in symbol:
            encChar = int(symbol.get(character)) + (encKey * 2)
        elif character in number:
            encChar = int(character) + (encKey * 2)

        encChar = encChar % 25
        encryptData = alpha2.get(str(encChar))
        return encryptData.upper()

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
    encKey = len(data) - 5
    character = character.lower()
    
    if character == ' ':
        encryptString.append(' ')
    else:
        encryptData = encryption(character, encKey)
        encryptString.append(encryptData)

# Displays result after converting to a single string for ease of reading      
print('Your original input of ' + data + ' was encrypted to:', end = ' ')
for i in range(len(encryptString)):
    print(encryptString[i], end = '')
