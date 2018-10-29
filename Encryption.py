import sys, random

# Definitions for usable characters and their numeric values
alpha = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}
alpha2 = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '10': 'k', '11': 'l', '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's', '19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z'}
symbol = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
symbol2 = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}

# List used to reference for numbers
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Declaring the encrypt list
encryptString = []

print('Please enter the data string you would like to be encrypted\n *Use letters, numbers or standard symbols only*')

data = input()

# Encryption function
def encryption(character):
    category = random.randint(1, 3)
    if category == 1:
        randNum = random.randint(1, 25)
        randLet = alpha2.get(str(randNum))
        
        if character in alpha:
            distance = abs(int(alpha.get(character)) - randNum)
        elif character in symbol:
            distance = abs(int(symbol.get(character)) - randNum)
        elif character in number:
            distance = abs(int(character) - randNum)
        
        if distance < 10:
            category = random.randint(1, 2)
            if category == 1:
                encryptData = randLet + str(distance)
                return encryptData
                                      
            elif category == 2:
                randSym = symbol2.get(str(distance))
                encryptData = randLet + randSym
                return encryptData
            else:
                print('Error: Category value ' + category)
        else:
            randLet2 = alpha2.get(str(distance))
            encryptData = randLet + randLet2
            return encryptData
    
    elif category == 2:
        randNum = random.randint(0, 9)
        
        if character in alpha:
            distance = abs(int(alpha.get(character)) - randNum)
        elif character in symbol:
            distance = abs(int(symbol.get(character)) - randNum)
        elif character in number:
            distance = abs(int(character) - randNum)
            
        if distance < 10:
            category = random.randint(1, 2)
            if category == 1:
                encryptData = str(randNum) + str(distance)
                return encryptData
                                      
            elif category == 2:
                randSym = symbol2.get(str(distance))
                encryptData = str(randNum) + randSym
                return encryptData
            else:
                print('Error: Category value ' + category)
        else:
            randLet = alpha2.get(str(distance))
            encryptData = str(randNum) + randLet
            return encryptData
    
    elif category == 3:
        randNum = random.randint(0, 9)
        randSym = symbol2.get(str(randNum))

        if character in alpha:
            distance = abs(int(alpha.get(character)) - randNum)
        elif character in symbol:
            distance = abs(int(symbol.get(character)) - randNum)
        elif character in number:
            distance = abs(int(character) - randNum)
            
        if distance < 10:
            category = random.randint(1, 2)
            if category == 1:
                encryptData = randSym + str(distance)
                return encryptData
                                      
            elif category == 2:
                randSym2 = symbol2.get(str(distance))
                encryptData = randSym + randSym2
                return encryptData
            else:
                print('Error: Category value ' + category)
        else:
            randLet = alpha2.get(str(distance))
            encryptData = randSym + randLet
            return encryptData
    
    else:
        print('Error: Category value ' + category)
        


# Loop takes each character through the encrypt function
for character in data:
    character = character.lower()
    
    if character == ' ':
        encryptString.append(' ')
    else:
        encryptData = encryption(character)
        encryptString.append(encryptData)
      
print('Your original input of ' + data + ' was encrypted to:', end = ' ')

# Formats the list into a single string for ease of reading
for i in range(len(encryptString)):
    print(encryptString[i], end = '')
