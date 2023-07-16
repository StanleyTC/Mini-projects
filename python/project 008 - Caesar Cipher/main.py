def encrypt(text, shift, alphabet):
    newvalue = []
    for i in range(0, len(text)):
        if text[i] in alphabet:
            a = alphabet.index(text[i])
            newvalue.append(alphabet[a+shift])
    print(newvalue)


def decrypt(text, shif, alphabet):
    newvalue = []
    for i in range(0, len(text)):
        if text[i] in alphabet:
            a = alphabet.index(text[i])
            newvalue.append(alphabet[a-shift])
    print(newvalue)


print("""
 ██████  █████  ███████ ███████  █████  ██████       ██████ ██ ██████  ██   ██ ███████ ██████  
██      ██   ██ ██      ██      ██   ██ ██   ██     ██      ██ ██   ██ ██   ██ ██      ██   ██ 
██      ███████ █████   ███████ ███████ ██████      ██      ██ ██████  ███████ █████   ██████  
██      ██   ██ ██           ██ ██   ██ ██   ██     ██      ██ ██      ██   ██ ██      ██   ██ 
 ██████ ██   ██ ███████ ███████ ██   ██ ██   ██      ██████ ██ ██      ██   ██ ███████ ██   ██ 
                                                                                               
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

value = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input('Type your message: \n').lower()
shift = int(input('Type the shift number: \n'))


if value == 'encode':
    encrypt(text, shift, alphabet)
    ...
elif value == 'decode':
    decrypt(text, shift, alphabet)
else:
    print('Sorry, invalid value')