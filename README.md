# Caesar Cipher Decoder
 decrypts all sorts of caesar ciphers

 algorithm::

 the program starts by taking shift value as 1 and shifts all letters in the encoded sentence by the next letter. then it counts how many of those words exist in the dictionart(words.txt file acts as the reference).

 now it takes shift value as 2 and repeats the above steps. once all 26 shift values have been taked into consideration,the shift value with maximum amount of words matching with the dictionary is taken as best shift value. 

 the decoded sentence obtained by shifting by 'best shift value' is then displayed
