'''
Estimated time

10-15 minutes
Level of difficulty

Easy
Objectives

    improving the student's skills in operating with strings;
    encouraging the student to look for non-obvious solutions.

Scenario

Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

    asks the user for some text;
    checks whether the entered text is a palindrome, and prints result.

Note:

    assume that an empty string isn't a palindrome;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent;
    there are more than a few correct solutions - try to find more than one.

Test your code using the data we've provided.
Test data

Sample input:
Ten animals I slam in a net

It's a palindrome

Sample input:
Eleven animals I slam in a net

It's not a palindrome
'''

def is_palindrome_v1(strng):
    n = len(strng)
    is_palindrome = True
    for i in range(n):
        if strng[i] != strng[n-1-i]:
            is_palindrome = False
    return is_palindrome

def is_palindrome_v2(strng):
    is_palindrome = False
    # check if the word is equal to its reversed
    if strng.lower() == strng[::-1].lower():
        is_palindrome = True
    return is_palindrome

try:
    strng = input("Give me a string: ")
    strng = strng.replace(" ", "").upper()
    print(is_palindrome_v1(strng))
    print(is_palindrome_v2(strng))
except BaseException as e :
    print("Note: ", e)
