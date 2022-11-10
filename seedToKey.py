import os

SEED = ['wait', 'doctor', 'evil', 'please', 'wait', 'learn', 'first', 'about', 'awesome', 'midnight', 'party', 'mix']

# Get the 0-2047 BIP-39 standard wordlist 
def getWordList():
    cwd = os.getcwd()
    with open(cwd + "/wordlist/eng.txt", "r") as f:
        wordlist = [w.strip() for w in f.readlines()]
    
    return wordlist

# Get the concatened bits by convverting the indexnumber of the words from wordlist to binary
def getBinaryFromWordlist():
    binary = ''
    wordlist = getWordList()

    for i in range(len(SEED)):
        index = wordlist.index(SEED[i])
        binary = binary + str(bin(index)[2:].zfill(8))
    
    return binary

# Convert the resultant binary into hex by removing the last appended character
def binaryToHex(binary):
    result = str(hex(int(binary, 2))[:-1])

    return result


def getPrivateKey():
    binary = getBinaryFromWordlist()
    result = binaryToHex(binary)


    print(result)


getPrivateKey()