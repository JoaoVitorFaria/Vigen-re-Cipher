#code based on  the book Cracking Codes with Python
#This approach consists of trying all the words in the dictionary file as keys in the vigenere cipher
import detectEnglish, vigenereCipher, pyperclip

def main():
    ciphertext= """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hacked_message = hackVigenereDictionary(ciphertext)

    if hacked_message != None:
        print("Copying hacked message to clipboard:")
        print(hacked_message)
        pyperclip.copy(hacked_message)
    else:
        print("Failed to hack encryption.")


def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    #the readlines method return a list of string, where each string is a single line from the file
    words = fo.readlines()
    fo.close()

    for word in words:
        #Remove the newline at the end
        word = word.strip()
        decrypted_text = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decrypted_text, word_percentage=40):
            print()
            print("Possible encryption break:")
            print("key" + str(word)+":"+decrypted_text[:100])
            print()
            print("Press D for done, or just press Enter to continue breaking:")
            response = input('>')

            if response.upper().startswith('D'):
                return decrpted_text

if __name__ == '__main__':
    main()
