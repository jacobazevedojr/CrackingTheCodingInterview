# Given two strings, write a method to decide if one is a permutation of the other.

# A string permuation has the same length and the same collection of characters as the original string
# (order of characters doesn't matter)

def isPermutation(str1, str2):
    # permutations must have the same length
    if len(str1) != len(str2):
        return False

    # Sorting strings O(N log N), where N is the length of str1 and str2
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)

    for i in range(len(str1)):
        # Once sorted, the strings should be exactly the same as one another (order now matters)
        if sortedStr1[i] != sortedStr2[i]:
            return False

    return True


str1 = input("String 1:")
str2 = input("String 2:")

if isPermutation(str1, str2):
    print("String 2 is a permutation of String 1")
else:
    print("String 2 is not a permutation of String 1")
