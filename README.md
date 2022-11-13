# BIP39_Seed_Converter

Learn to manually create 12 worded BIP39 seed phrases using an initial entropy without using any third party libraries in Python. Also contains code to convert seed phrase into private key.

Following are the steps taken to convert entropy into seed phrase:

* Create a long enough random numbers.
* A checksum is appended to this random number.
* Resultant number is then divided into chunks.
* Each chunk has a length of 11 bits and each chunk is mapped to a English word from the dictionary of 2¹¹ ~ 2048 words.
