'''
Problem statement:
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

    asks the user for one line of text to encrypt;
    asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
    prints out the encoded text.
'''

'''##########################################################################'''

''' Caesar cipher - encrypt the message with a shift key
there's an algm behind this approach'''
def caesar_cipher_encrypter(text, num):
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        # Calculate R, the rank of char in the alphabet
        # Calculate R2 = (R+shift) Module 26
        # Write the letter with rank R2 in the alphabet
        char = char.upper()
        code = ord(char) + num
        # find the code of the first letter
        first = ord('A')
        # make correction
        code -= first
        code %= 26
        # append the encoded character to message
        cipher += chr(first + code)
    return cipher

''' preserve casing - the casing of the letter is preserved in a
list, 1 indicates an upper case, 0 indicates a lower case,
2 indicates a non-alphabetical character '''
def preserve_casing(text):
    casing = []
    for i in range(len(text)):
        if text[i].islower():
            casing.insert(i, 0)
        elif text[i].isupper():
            casing.insert(i, 1)
        else:
            casing.insert(i, 2)
    return casing

''' restore casing - based on the casing indicator given to it,
it adjusts the casing of the text based and returns it'''
def restore_casing(text, indicator):
    text_list = []
    for i in range(len(text)):
        if indicator[i] == 0:
            text_list.insert(i, text[i].lower())
        elif indicator[i] == 1:
            text_list.insert(i, text[i].upper())
        else:
            text_list.insert(i, text[i])
    adjusted_text = ''.join(text_list)
    return adjusted_text

okay = False
message = ''
while(not okay):
    try:
        if not message:
            message = input("Enter message to encrypt: ")
        shift = int(input("Enter shift from the range 1..25 inclusive: "))
        assert shift <= 25 and shift >=1
        okay = not okay
        casing = preserve_casing(message)
        cipher = caesar_cipher_encrypter(message, shift)
        cipher = restore_casing(cipher, casing)
        print("Cipher: ", cipher)
    except AssertionError:
        print("Shift is not in range")
    except ValueError:
        print("Shift is not a number")
    except Exception as e:
        print(e)
        print("Base exception")
