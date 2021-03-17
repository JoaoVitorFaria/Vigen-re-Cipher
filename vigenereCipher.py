#code based on the book Cracking codes with Python
#Vigenère Cipher basically takes a character from the original message and find its index at the alphabet,
#then get the letter that is in the same position  at the key, get its index in alphabetical order, and sum both to find the ciphertext letter
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    my_message = '''Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.'''
    my_key = 'ASIMOV'
    my_mode = 'encrypt'#it can be setted to 'decrypt'

    if my_mode == 'encrypt':
        translated = encryptMessage(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decryptMessage(my_key, my_message)

    print("%sed message:"%(my_mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clip board.')

#the wrapper functions
def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = []
    #this variable keeps track of which subkey to use
    key_index = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated.append(symbol)
            
    return ''.join(translated)

if __name__ == '__main__':
    main()
