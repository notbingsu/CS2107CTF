import hashlib
#import hashedtext.txt file
file = open('hashedtext.txt', 'r')

# create dictionary of all char hashes
hashes = {}
for i in range(32,127):
    hashes[hashlib.sha1(chr(i).encode()).hexdigest()] = chr(i)

# show hashes
# print(hashes)

#translate hashed text to plain text
for line in file:
    print(hashes[line.strip()], end='')
