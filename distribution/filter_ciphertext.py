from Crypto.Cipher import AES
import os

# with open("flag.txt", "r") as f:
#     flag = f.read()

BLOCK_SIZE = 16
iv = os.urandom(BLOCK_SIZE)

xor = lambda x, y: bytes(a^b for a,b in zip(x,y))

key = os.urandom(16)

def encrypt(pt):
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    blocks = [pt[i:i+BLOCK_SIZE] for i in range(0, len(pt), BLOCK_SIZE)]
    tmp = iv
    ret = b""
    
    for block in blocks:
        res = cipher.encrypt(xor(block, tmp))
        ret += res
        tmp = xor(block, res)
        
    return ret

    
def decrypt(ct):
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    blocks = [ct[i:i+BLOCK_SIZE] for i in range(0, len(ct), BLOCK_SIZE)]

    for block in blocks:
        if block in secret_enc:
            blocks.remove(block)
    
    tmp = iv
    ret = b""
    
    for block in blocks:
        res = xor(cipher.decrypt(block), tmp)
        ret += res
        tmp = xor(block, res)
    
    return ret
    
# secret = os.urandom(80)
# secret_enc = encrypt(secret)

secret_enc = "1a1ec9400b56f49a40dfff6b4f7b556ead620871ba55c9398fc121afa28dd23a21d6625e61db06779df2c443c8e4ba1785493e2b5d3f2e0c6ce7ba140c8ac980e24cb78cf14bde31d63f5df125230cf9"
secret = decrypt(secret_enc)
print(secret)

# print(f"Encrypted secret: {secret_enc.hex()}")

# print("Enter messages to decrypt (in hex): ")

# while True:
#     res = input("> ")

#     try:
#         enc = bytes.fromhex(res)

#         if (enc == secret_enc):
#             print("Nice try.")
#             continue
        
#         dec = decrypt(enc)
#         if (dec == secret):
#             print(f"Wow! Here's the flag: {flag}")
#             break

#         else:
#             print(dec.hex())
        
#     except Exception as e:
#         print(e)
#         continue

    


