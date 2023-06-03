import string
### HELPER CODE ###

def load_words(): # Returns: a list of valid words. Words are strings of lowercase letters.
    #print("Loading word list from file...")
    f = open("words.txt", 'r')
    wordlist = []
    for line in f:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist
loadedwords = load_words()
#print(load_words())
#print(loadedwords,"done")

def is_word(word_list, word): #Determines if word is a valid word from wordlist by removing symbols and lowercase
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list
def get_story_string():    #Returns: a story in encrypted text.
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story
#print(get_story_string())
message_text = get_story_string()
#message_text = "bn uif cftu"
### END HELPER CODE ###
WORDLIST_FILENAME = 'words.txt'
class Message(object):
    def __init__(self, text):
        #print("yo")
        #self.message_text (string, determined by input text)
        self.message_text = text
        #self.valid_words (list, determined using helper function load_words)
        self.valid_words = loadedwords
    def get_message_text(self): #Used to safely access self.message_text outside of the class
        return self.message_text
    def get_valid_words(self): #Returns: a COPY of self.valid_words
        return self.valid_words
    def build_shift_dict(self,shift): #Returns: a dictionary mapping a letter (string) to  another letter (string).
        lowercaseletters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        uppercaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letterdict = {}
        for i in range(0,26,1):
            letterdict[lowercaseletters[i]] = lowercaseletters[i + shift]
        for i in range(0,26,1):
            letterdict[uppercaseletters[i]] = uppercaseletters[i + shift]
        #shift (integer): the amount by which to shift every letter of the alphabet. 0 <= shift < 26
        return letterdict
    def apply_shift(self, shift): #Returns: the message text with every character shifted down the alphabet by shift
        msgaftercode = []
        letterdict = Message.build_shift_dict(self,shift)
        for i in range(0, len(message_text), 1):
            if message_text[i] in letterdict:
                encodedletter = letterdict[message_text[i]]
                msgaftercode.append(encodedletter)
            else:
                msgaftercode.append(message_text[i])
        strmsgaftercode = ''.join(msgaftercode)
        #Creates a new string that is self.message_text shifted down the alphabet by input shift
        return strmsgaftercode

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        #PlaintextMessage object inherits from Message and has five attributes:
        self.message_text = text
        self.valid_words = load_words()
        self.shift = shift
        letterdict = Message.build_shift_dict(self.message_text, self.shift)
        self.encryption_dict = letterdict
        self.message_text_encrypted = Message.apply_shift(self.message_text, self.shift)
    def get_shift(self):
        return self.shift
    def get_encryption_dict(self): #Returns: a COPY of self.encryption_dict
        encryption_dict_copy = self.encryption_dict.copy()
        return encryption_dict_copy
    def get_message_text_encrypted(self): #Used to safely access self.message_text_encrypted outside of the class
        return self.message_text_encrypted
    def change_shift(self, shift): #Changes self.shift of the PlaintextMessage and updates other attributes determined by shift.
        #self.shift =
        #cant undestand what this method is meant to do
        #Returns: nothing
        #return
        pass

class CiphertextMessage(Message):
    def __init__(self, text):
        #a CiphertextMessage object has two attributes:
        self.message_text = text
        #print(self.message_text)
        self.valid_words = load_words()
        #print(self.valid_words)
    def decrypt_message(self):
        rightwords = loadedwords
        bestshift =0
        validwordsafterbestshift = 0
        #print(Message.apply_shift(self, 8))
        for shift in range(0,26,1):
            strmsgaftercodewithoutlist = Message.apply_shift(self, shift)
            strmsgaftercode = strmsgaftercodewithoutlist.split()
            validwordsaftershift = 0
            for word in strmsgaftercode:
                for word2 in rightwords:
                    if word == word2:
                        validwordsaftershift += 1
            #print(shift, validwordsaftershift)
            if validwordsaftershift >= validwordsafterbestshift:
                bestshift = shift
                validwordsafterbestshift = validwordsaftershift
                #print(shift,validwordsaftershift,validwordsafterbestshift)

        #We will define "best" as the shift that creates the maximum number of real words when we use apply_shift(shift)
        #If s is the original shift value used to encrypt the message, then 26 - s to be the best shift value for decrypting it.
        bestsolved = Message.apply_shift(self, bestshift)
        #print(bestsolved)
        #Returns: a tuple of the best shift value used to decrypt the message and the decrypted message text using that shift value
        print(bestshift)
        return bestsolved
print(CiphertextMessage.decrypt_message("bn uif cftu"))





#Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('hello', 2)
#print('Expected Output: jgnnq')
#print('Actual Output:', plaintext.get_message_text_encrypted())

#    Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage('jgnnq')
#print('Expected Output:', (24, 'hello'))
#print('Actual Output:', ciphertext.decrypt_message())


'''
lowercaseletters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
uppercaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterdict = {}
for i in range(0,26,1):
    letterdict[lowercaseletters[i]] = lowercaseletters[i + 5]
for i in range(0,26,1):
    letterdict[uppercaseletters[i]] = uppercaseletters[i + 5]

message_text = get_story_string()
print(message_text)

msgaftercode = []
for i in range(0,len(message_text),1):
    if message_text[i] in letterdict:
        encodedletter = letterdict[message_text[i]]
        msgaftercode.append(encodedletter)
    else :
        msgaftercode.append(message_text[i])
strmsgaftercode = ''.join(msgaftercode)
print(strmsgaftercode)
'''