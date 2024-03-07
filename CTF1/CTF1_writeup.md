# CTF Assignment 1 Write Up

_Lu Bingyuan, A0259353X_

## Easy Challenges

### Sanity Check

Flag is written at the bottom of CTF Assignment Instructions document  
Flag is `CS2107{nice_job_read_til_here!}`

### XOR Secure

The encryption process is as follows:

- Encode the plaintext to bytes
- Convert 4 keys from hex arrays to byte arrays
- XOR the byte array of plaintext with the byte array of the keys
- Convert the XORed byte array to hex string

Therefore to decrypt the message using XOR self inverse property

- Convert the hex string to byte array
- XOR the byte array with the byte array of the keys
- Convert the XORed byte array to string

The flag is then
Refer to the python script `xor_secure.py` for the implementation.

### Caesar with Capital C

Given the encryption algorithm of the caesar cipher,

- upper case and lower case characters are incremented by the static key, then mod 26 before converting to character by adding to the ascii value of 'A' or 'a' respectively
- digits are incremented by the static key, then mod 10 before converting to character by adding to the ascii value of '0'

Therefore to decrypt the message,

- upper case and lower case characters are decremented by the static key, if value is negative, add 26 before converting to character by adding to the ascii value of 'A' or 'a' respectively
- digits are decremented by the static key, if value is negative, add 10 before converting to character by adding to the ascii value of '0'

Any non-alphanumeric characters are left unchanged.
The flag is then
Refer to the C++ script `caesardecrypt.cpp` for the implementation.

### Hash_browns

Given a ciphertext in the format of lines of 40 hex characters (and the hint suggesting SHA1 hashing), on can deduce that every line of hex characters is the digest of one message, which in this case are plaintext characters.  
By using python hashlib, one can hash all plaintext characters to their SHA1 digest and compare with the given ciphertext. Each character can be retrieved subsequently.
