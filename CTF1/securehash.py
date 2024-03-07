attempts = 3

def secure_hash():
    password_input = input('Enter password: ')
    expected_string = "e|278Fx7|!VeX7_!V!|@8SR"
    magic = [
        int('0x1fa9787f52d6819dac3e51c96c9850ac9a68a000' ,0),
        int('0x551e7b2ade66a9cd21538d24f8232eb9e3c6a00',0),
        int('0x685130edf575c5fd89b4ea52d8ce440fb75d40',0),
        int('0x4d2b06845e7f210fd15f3697fe234c69919a0',0),
        int('0x267227d769f1422427c2f550f7852c59bfec',0),
        int('0xd9fd323c23dd5a26579cb53a8a42996b38',0),
        int('0x388a9fbf545b3b1a5e4b80376e94de767',0),
        int('0xadef7b085371d7244d43d0011e7c6d5',0),
        int('0x18cbc26aefc3b3b1ef4588ce4acc6b',0),
        int('0x296e5ed6f99d55e5efb08eb856e9',0),
        int('0x314ef6584d10a8c5226f105685',0),
        int('0x2798a7a450463592994fc72f',0),
        int('0x133caaa3da819c1ca0087d',0),
        int('0x445974d799d8bcf9c3b',0)
    ]
    magic2 = int('0x2971713e56d0006e6a0b48126ca34000')
    calculated_string = ''
    result = 0
    nresult = 0
    for char in password_input:
        result = 0
        one_char = -ord(char)
        for j in range(len(magic)):
            result *= one_char
            result += magic[len(magic) - 1 - j]
        nresult = result % magic2
        result = -result // magic2
        result += (888 - result) * (result > 127)
        result += (888 - result) * (nresult != 0)
        result += (888 - result) * (result < 33)
        calculated_string += chr(result)
    
    if calculated_string == expected_string:
        print('Yay you got the password. Submit the password as the flag :D')
    else:
        global attempts
        attempts -= 1
        if attempts == 0:
            print('Too many attempts (≧ڡ≦*). Go try other challenges.')
        else:
            print(f'Try harder. You have {attempts} attempts left.')

def encode(char):
    magic = [
        int('0x1fa9787f52d6819dac3e51c96c9850ac9a68a000' ,0),
        int('0x551e7b2ade66a9cd21538d24f8232eb9e3c6a00',0),
        int('0x685130edf575c5fd89b4ea52d8ce440fb75d40',0),
        int('0x4d2b06845e7f210fd15f3697fe234c69919a0',0),
        int('0x267227d769f1422427c2f550f7852c59bfec',0),
        int('0xd9fd323c23dd5a26579cb53a8a42996b38',0),
        int('0x388a9fbf545b3b1a5e4b80376e94de767',0),
        int('0xadef7b085371d7244d43d0011e7c6d5',0),
        int('0x18cbc26aefc3b3b1ef4588ce4acc6b',0),
        int('0x296e5ed6f99d55e5efb08eb856e9',0),
        int('0x314ef6584d10a8c5226f105685',0),
        int('0x2798a7a450463592994fc72f',0),
        int('0x133caaa3da819c1ca0087d',0),
        int('0x445974d799d8bcf9c3b',0)
    ]
    magic2 = int('0x2971713e56d0006e6a0b48126ca34000',0)
    result = 0
    nresult = 0
    one_char = -ord(char)
    for j in range(len(magic)):
        result *= one_char
        result += magic[len(magic) - 1 - j]
    nresult = result % magic2
    result = -result // magic2
    result += (888 - result) * (result > 127)
    result += (888 - result) * (nresult != 0)
    result += (888 - result) * (result < 33)
    return chr(result)

# create dictionary of char mappings in ascii range using encode function
char_map = {encode(chr(i)):chr(i) for i in range(33,127)}
print(char_map)
expected_string = "e|278Fx7|!VeX7_!V!|@8SR"
calculated_string = ''.join([char_map[char] for char in expected_string])
print(calculated_string)