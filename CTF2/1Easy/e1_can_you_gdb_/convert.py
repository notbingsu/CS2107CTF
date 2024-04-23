import string
str = "0x59b318bec4e35ba7"
print(bytes.fromhex(str[2:]).decode('utf-8'))