import hashlib
import binascii
import os

K128 = "0x0123456789abcdef0123456789abcdef"

# Initialization
# Checks if the length of the entropy is following BIP 39 standard and converts the hexadecimal string into binary 
def checkEntropyAndConvert(entropy):
    data = entropy.strip() # Cleaning of data for spaces and indents
    data = binascii.unhexlify(data[2:]) # Return the binary data represented by the hexadecimal string. Note that we first remove 0x from hexadecimal string

    if len(data) not in [16, 20, 24, 28, 32]:
        raise ValueError("The length of the entropy should be [16, 20, 24, 28, 32] bits. The current length is (%d)." % len(data))
    
    return data

# Step 1, 2, 3, 4, 5
# Generates checksum by taking the first ENT/32 bits and then appends it to the end of inital entropy which in our
# case is the privateKey. Concatenated bits are split into groups of 11 bits, each encoding a number from 0-2047
def generateCheckSum(data):
    h = hashlib.sha256(data).hexdigest() # Get the SHA3-256 hash
    b = bin(int(binascii.hexlify(data),16))[2:].zfill(len(data)*8) + bin(int(h,16))[2:].zfill(256)[: len(data)* 8//32]

    return b

# Get the 0-2047 BIP-39 standard wordlist 
def getWordList():
    cwd = os.getcwd()
    with open(cwd + "/eng.txt", "r") as f:
        wordlist = [w.strip() for w in f.readlines()]
    
    return wordlist


# Step 6
# Loop through the bits and map the bits to the wordlist. The encoding number serves as the index
def mapToWordList(wordlist, b):
    seed = []
    for i in range(len(b)//11):
        indx = int(b[11*i:11*(i+1)], 2)
        seed.append(wordlist[indx])
    
    return seed



def getMnemonicPhrase():
    data = checkEntropyAndConvert(K128)
    b = generateCheckSum(data)
    seed = mapToWordList(getWordList(), b)

    print(seed)

getMnemonicPhrase()
