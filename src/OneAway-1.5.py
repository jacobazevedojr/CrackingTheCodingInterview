# There are three types of edits that can be performed on strings: insert a character, remove a character,
# or replace a character. Given two strings, write a function to check if they are one edit (or zero edits away)


def isOneEdit(str1, str2):
    # Strings must be within +-1 length
    if len(str1) - len(str2) > 1 or len(str1) - len(str2) < 1:
        return False

    # Replacement of 1 character is the only possible 1 edit if lens are equal
    if len(str1) == len(str2):
        return replacementEdit(str1, str2)

    # Insertion and removal are then checked for all remaining cases
    # Insertion is for the smaller string while removal is for the larger string,
    # fixating on the smaller string will allow for a single insertion function to be used
    elif len(str1) > len(str2):
        return insertionEdit(str2, str1)
    else:
        return insertionEdit(str1, str2)

def replacementEdit(str1, str2):
    editFlag = False
    for i in range(len(str1)):
            if str1[i] != str2[i]:
                if editFlag:
                    return False
                editFlag = True
    return True


def insertionEdit(str1, str2):
    # str1 will always be smaller than str2 by 1 character
    index1 = 0
    index2 = 0

    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

if isOneEdit("Flag", "lag"):
    print("One edit")
