# BIP39_Seed_Converter

Learn to manually create 12 worded BIP39 seed phrases using an initial entropy without using any third party libraries.

Following are the steps taken:

* Create a long enough random numbers.
* A checksum is appended to this random number.
* Resultant number is then divided into chunks.
* Each chunk has a length of 11 bits and each chunk is mapped to a English word from the dictionary of 2¹¹ ~ 2048 words.
