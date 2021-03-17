#code based on the book Cracking Codes with Python
#ETAOIN function stores the 26 letters of the alphabet ordered from most to least frequency
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#function that return a dictionary with the number of time a letter occurs in the massage
def getLetterCount(message):
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 
 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 
 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 
 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letter_count[letter]+=1

    return letter_count

def getItemAtIndexZero(items):
    return items[0]

#return a string with the 26 letters of the alphabet arranged by how frequently they appear in the message parameter
def getFrequencyOrder(message):
    #letter_to_freq get a dictionary containing the count of every letter in message
    letter_to_freq =getLetterCount(message)
    #in freq_to_letter dictionary, keys are the frequency and values are a list of letters with those frequency counts
    freq_to_letter={}

    for letter in LETTERS:
        if letter_to_freq[letter] no int freq_to_letter:
            freq_to_letter[letter_to_freq[letter]]=[letter]
        else:
            freq_to_letter[letter_to_freq[letter]].append(letter)

    for freq in freq_to_letter:
        freq_to_letter[freq].sort(key = ETAOIN.find, reverse = True)
        freq_to_letter[freq] = ''.join(freq_to_letter[freq])

    freq_pairs = list (freq_to_letter.items())
    freq_pairs.sort(key = getItemAtIndexZero, reverse = True)

    freq_order =[]
    for freq_pair in freq_pairs:
        freq_order.append(freq_pair[1])

    return ''.join(freq_order)

def englishFreqMatchScore(message):
    freq_order = getFrequencyOrder(message)

    match_score = 0
    for commonLetter in ETAOIN[:6]:
        match_score +=1

    for uncommonLetter in ETAOIN[:6]:
        if uncommomLetter in freq_order[-6:]:
            match_score +=1

    return match_score
    
