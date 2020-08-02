# Write a method to replace all spaces in as string with "%20." You may assume that the string has sufficient space at
# the end to hold the additional characters, and that you are given the "true" length of the string.
# (Note: If implementing in Java, please use a character array so that you can perform this operation in place)

# Python strings are immutable as is in Java, and this algorithm is O(N) as is converting a str to a list
# So I will follow the Java instructions as well and utilize a list of characters

# Example
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

# Parse for space and substitute with the token.

def URLify(str1, trueLen):
    token = "%20"
    # Parse for spaces to identify length of URLified string
    spacesCount = charCount(str1, 0, trueLen,' ')
    str1List = list(str1)

    # Specifies where the end of the new string will begin
    # len(token) - 1 is how many more characters are needed to substitute in the token
    # Example: token = ".", len(token) = 1, therefore; '.' will simply substitute ' ' (no additional space needed)
    endIndex = trueLen - 1 + (len(token) - 1) * spacesCount
    finalLength = endIndex + 1

    for i in range(trueLen - 1, 0, -1):
        if str1List[i] == ' ':
            for j in range(len(token)):
                str1List[endIndex - j] = token[len(token) - 1 - j]

            endIndex -= len(token)
        else:
            str1List[endIndex] = str1[i]
            endIndex -= 1

    URLstring = ''
    for i in range(finalLength):
        URLstring += str1List[i]

    return URLstring

def charCount(str1, start, end, char):
    count = 0
    for i in range(start, end):
        if str1[i] == char:
            count += 1

    return count


print(URLify("Mr John Smith    ", 13))
