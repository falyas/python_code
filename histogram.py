'''
Character Frequency Histogram - sorted

Level of difficulty

Medium

Objectives

    improving the student's skills in operating with files (reading)
    using data collections for counting numerous data.

Scenario - PART 1

A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

    asks the user for the input file's name;
    reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
    prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:
aBc

the expected output should look as follows:
a -> 1
b -> 1
c -> 1

Tip:

We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.

Scenario - PART 2

The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

    the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
    the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

Assuming that the input file contains just one line filled with:
cBabAa

the expected output should look as follows:
a -> 3
b -> 2
c -> 1

Tip:

Use a lambda to change the sort order.
'''
import os
import sys

data = {}

# Obtain a histogram data colloection
try:
    file_name = input("Enter a text file name: ")
    # check the extension
    file_name_parts = os.path.splitext(file_name)
    if file_name_parts[1].isspace():
        file_name = file_name + ".txt"
    if file_name_parts[1] != ".txt":
        print("This is not a text file. We can't serve you")
        sys.exit()
    stream = open(file_name, "rt", encoding="utf-8")
    content = stream.read()
    content = content.lower()
    for chr in content:
        #if the character exists, increment it's value
        #if it doesn't exist add it and give a value of 1
        if chr in data.keys():
            data[chr] += 1
        else:
            data.update({chr: 1})
    stream.close()
except IOError as ioe:
    if isinstance(ioe.errno, int):
        print("IOError number: ", ioe.errno, " ", os.strerror(ioe.errno))
    else:
        print("IOError: ", exc)
except Exception as be:
    print("Exception: ", be)

# sort the data with lambda, puts data in a list of tuples
# sorted() sorts the tuples from data.items() based on the order of the values
# returned from the lambda function which is the order of the values in data
data_sorted = sorted(data.items(), key = lambda v: v[1], reverse=True)

# print data for the user to see it
for pair in data_sorted:
    print(ascii(pair[0]), "->", pair[1])

# put the data in a file with .hist extension

# make the new file name
new_file_name = file_name_parts[0] + ".hist"

try:
    stream = open(new_file_name, "wt")
    for pair in data_sorted:
        stream.write(str(ascii(pair[0])) + "->" + str(pair[1]) + "\n")
    stream.close()
    print("Done. The content is now written to ",new_file_name)
except IOError as ioe:
    if isinstance(ioe.errno, int):
        print("IOError number: ", ioe.errno, " ", os.strerror(ioe.errno))
    else:
        print("IOError: ", exc)
except Exception as be:
    print("Exception: ", be)
