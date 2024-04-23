import json


with open('1Easy\e2_keylogger\e2data.json') as f:
    data = json.load(f)

keypresses = []
for packet in data:
    keypresses.append(packet['_source']['layers']['usb.capdata'])

# dictionary of keypresses
from keyd import keydict

# keypress_set = set()
for keypress in keypresses:
    #split keypress into bytes
    presses = keypress.split(':')
    # get the keypress value
    flag = False
    for press in presses:
        if keydict.get(int(press, 16)):
            if presses[0] == '02':
                print(keydict[int(press, 16)][1], end='')
            else:
                print(keydict[int(press, 16)][0], end='')
            flag = True
    

