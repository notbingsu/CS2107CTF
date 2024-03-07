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

The flag is then `CS2107{M4St3R_0f_aNc13nT_x0R_t3CHn1qu3s!!!!}`  
Refer to the python script [`xor_secure.py`](XOR_secure.py) for the implementation.

### Caesar with Capital C

Given the encryption algorithm of the caesar cipher,

- upper case and lower case characters are incremented by the static key, then mod 26 before converting to character by adding to the ascii value of 'A' or 'a' respectively
- digits are incremented by the static key, then mod 10 before converting to character by adding to the ascii value of '0'

Therefore to decrypt the message,

- upper case and lower case characters are decremented by the static key, if value is negative, add 26 before converting to character by adding to the ascii value of 'A' or 'a' respectively
- digits are decremented by the static key, if value is negative, add 10 before converting to character by adding to the ascii value of '0'

Any non-alphanumeric characters are left unchanged.
The flag is then `CS2107{345y_p345y_l3m0n_5qu33zy}`  
Refer to the C++ script [`caesardecrypt.cpp`](caesardecrypt.cpp) for the implementation.

### Hash_browns

Given a ciphertext in the format of lines of 40 hex characters (and the hint suggesting SHA1 hashing), on can deduce that every line of hex characters is the digest of one message, which in this case are plaintext characters.  
By using python hashlib, one can hash all plaintext characters to their SHA1 digest and compare with the given ciphertext. Each character can be retrieved subsequently.

The flag is then `CS2107{hash_br0wn$_cr@ck3rs}`  
Refer to the python script [`hashbreak.py`](hashbreak.py) for the implementation.

### Rivest-Shamir-Adleman

- Using the prime numbers p and q provided, one can calculate the modulus n and the totient of n using the formulae  
  $n = p \times q$ and $\phi(n) = (p-1) \times (q-1)$.
- Then, one can choose a public exponent e such that it is coprime with $\phi(n)$, and calculate the private exponent d such that $d \equiv (k \times \phi(n) + 1) / e$.
- This was done by iterating k from 1 to $\phi(n)$ and checking if $(k \times \phi(n) + 1) \mod e$ resulted in a remainder.
- Using d, one can decrypt the ciphertext using the formula $m = c^d \mod n$.
- The plaintext is then reproduced by converting the integer m to a string of characters.

The flag is then `CS2107{pl3ase_$3cure_ur_p_q_RS@}`  
Refer to the python script [`rsa.py`](rsa.py) for the implementation.

## Medium Challenges

### Salad

Since the salad python script maps every character from ASCII 33 to 126 to a corresponding character in the same range, the decryption process is to reverse the mapping. A dictionary is created to map the encrypted characters to the original characters, and the encrypted message is then decrypted by replacing each character with the corresponding character in the dictionary.

The flag is then `CS2107{m45t3r_0f_sub5ti7u7i0n_3nj0y_uR_s4l@d!!}`  
Refer to the python script [`undosalad.py`](undosalad.py) for the implementation.

### Baby_Shark

This challenge uses Wireshark to read packets from a capture given.  
Firstly, the HTTP objects from the pcapng file are extracted. I referenced Wireshark Episode #7 https://www.youtube.com/watch?v=V23d18W2-pw to extract the HTTP objects. The objects are saved in the folder `WireShark_captures`.  
The 4 parts of the flag were found in the following files:

- wallpaper.png - `CS2107{b`
- inventory_book.xlsx - `@by_sh@a`
- config.xml - `Rk_d00_d` in a component `<flag>`
- Confidential.pdf - `Oo_143192}` hidden as text with no color

The combined flag is thus `CS2107{b@by_sh@aRk_d00_dOo_143192}`  
Refer to the folder [`WireShark_captures`](WireShark_captures) for the extracted files.

## Hard Challenge(s)

### Secure Hash

Similar to previous hash challenges, I approached the problem by hashing every ASCII character to its digest. The script for this hashing was found in the `<script>` component of the webpage using inspect element and can be found as `secure_hash()` in the `secure_hash.py' file.  
Using the script, a function mapping a single character was extracted. The function was then used to hash every character. Then using this hashing and the expected hashed string, the flag can be found by comparing the hashed string with the expected hashed string.

The flag is then `CS2107{1S_4Ct1y_4_Sb0x}`  
Refer to the python script [`securehash.py`](securehash.py) for the implementation.
