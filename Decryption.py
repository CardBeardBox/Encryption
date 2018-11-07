# Definitions for usable characters and their numeric values, used as references by encryption function
alpha = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}
alphaKey = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '10': 'k', '11': 'l', '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's', '19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z'}
symbol = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
symbolKey = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}

# List used to reference for numbers
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Declaring the variable to be used for displaying the decrypted data
decryptedString = []

# Decryption function 1    
def decFunc_1(character, decKey):
    alphaValue = 0
        
    if character in alpha:
        decChar = int(alpha.get(character)) - decKey
        decChar %= 25
        decryptData = alphaKey.get(str(decChar))
        return decryptData
        
    elif character in symbol:
        decChar = int(symbol.get(character)) - decKey
        decChar %= 10
        decryptData = symbolKey.get(str(decChar))
        return decryptData
    
    elif character in number:
        decChar = int(character) - decKey
        decChar %= 10
        decryptData = decChar
        return decryptData
        

# Decryption function 2    
def decFunc_2(character, decKey):
    character = character.lower()
    
    if character in alpha:
        decChar = int(alpha.get(character)) + (decKey * 2)
        decChar %= 25
        decryptData = alphaKey.get(str(decChar))
        return decryptData
    
    elif character in symbol:
        decChar = int(symbol.get(character)) + (decKey * 2)
        decChar %= 10
        decryptData = symbolKey.get(str(decChar))
        return decryptData
    
    elif character in number:
        decChar = int(character) + (encKey * 2)
        decChar = int(character) - decKey
        decryptData %= 10
        return decryptData

# Ask for user input     
print('Please enter the data string you would like to be decrypted\n')
data = input()

# Loop to make sure correct data params are met
while len(data) < 6:
    print('Sorry the input data string is too short, try again with atleast 6 characters\n')
    print('Please enter the data string you would like to be decrypted\n')
    data = input()

# Loop takes each character through the decrypt functions
for character in data:
    decKey = len(data) - 5
    
    if character == ' ':
        decryptedString.append(' ')
        
    elif character.isupper():
        decryptedChar = decFunc_2(character, decKey)
        decryptedString.append(decryptedChar)
        
    else:
        decryptedChar = decFunc_1(character, decKey)
        decryptedString.append(decryptedChar)

# Displays result after converting to a single string for ease of reading      
print('Your original input of ' + data + ' was decrypted to:', end = ' ')
for i in range(len(decryptedString)):
    print(decryptedString[i], end = '')
