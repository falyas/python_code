'''
Estimated time

10-15 minutes
Level of difficulty

Easy
Objectives

    improving the student's skills in operating with strings;
    converting strings into lists, and vice versa.

Scenario

An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

    asks the user for two separate texts;
    checks whether, the entered texts are anagrams and prints the result.

Note:

    assume that two empty strings are not anagrams;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent

Test your code using the data we've provided.
'''


try:
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # this is what we're going to do with both strings:
    # - remove spaces
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    # - change all letters to upper case
    str1 = str1.upper()
    str2 = str2.upper()
    # - convert string into list
    str1 = list(str1)
    str2 = list(str2)
    # - sort the list
    str1.sort()
    str2.sort()
    # - join list's elements into string
    print(str1)
    str1 = "".join(str1)
    str2 = "".join(str2)
    # and finally, compare both strings
    # Anagrams must have the same letters used the same amount of time
    if str1 == str2:
        print("Anagrams")
    else:
        print("Not anagrams")
# Let's do it!
except BaseException as e :
    print("Note: ", e)
