def mysplit(myString):
    myList = []
    #check if the string is empty of characters
    if not myString or myString.isspace():
        return myList
    #strip leading and rear white spaces
    myString = myString.strip()
    oneString = ''
    for element in myString:
        if element.isspace():
            myList.append(oneString)
            del oneString
            oneString = ''
        oneString = oneString + element

    #add the last string
    myList.append(oneString)
    return myList

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
