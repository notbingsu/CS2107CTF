def shift(c,key):
    return c+key
    
def enc(ac):
    # aabb = ""
    # for c in text:
    #     ac = ord(c)
    if ac > 33 and ac <= 96:
        if ac >= 65:
            if ac >= 73:
                if ac >= 91:
                    ac = shift(ac,-6)
    
                    return ac
                ac = shift(ac,32)

                return ac
            ac = shift(ac,-25)

            return ac
        
        if ac < 65:
            if ac < 58:
                if ac < 48:
                    ac = shift(ac,57)
    
                    return ac
                if ac >= 55:
                    ac = shift(ac,68)
    
                    return ac
                ac = shift(ac,10)

                return ac
            ac = shift(ac,-10)

            return ac
        return ac
    
    if ac >= 117 and ac < 126:
        if ac >= 123:
            ac = shift(ac,-68)

            return ac
        ac = shift(ac,-83)
        return ac
    
    if ac > 33 and ac <= 116:
        ac = shift(ac,-32)
        return ac
    
    if ac == 33:
        ac = 126
        return ac
    if ac == 126:
        ac = 33
    return ac

#main
if __name__ == "__main__":
    #create dictionary of character mapping
    d = {}
    for i in range(33,127):
        d[chr(enc(i))] = chr(i)
    #print the dictionary
    print(d)
    #get flag from salad.txt
    flag = open("salad.txt", "r").readline().strip()
    #initialize empty string
    decrypted = ""
    #iterate through the flag
    for c in flag:
        #decrypt the character
        decrypted += d[c]
    #print the decrypted flag
    print(decrypted)