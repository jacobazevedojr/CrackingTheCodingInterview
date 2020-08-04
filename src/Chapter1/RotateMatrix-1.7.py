# Given an image represented by an NxN matrix, where each pixel in the image is represented by an integer,
# write a method to rotate the image by 90 degrees. Can you do this in place?

# Assuming rotation is positive in the clockwise direction, each edge would have to move clockwise to the next edge
# Position edge - 1 would move to the next edge - 1


def rotateMatrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    N = len(matrix)
    # 1X1 matrix, N // 2 = 0, no rotation
    # 2X2 matrix, N // 2 = 1
    # 3X3 matrix, N // 2 = 1
    # 4X4 matrix, N // 2 = 2
    # 5X5 matrix, N // 2 = 2 and so forth
    # Notice that a 5X5 matrix has technically 3 layers with a single middle element,
    # so no rotation is needed in the 3rd layer
    for layer in range(N // 2):
        # layer = 0 signifies the exterior layer, each subsequent increment of layer involves an further interior layer
        # first and last specify the bounds of the subarrays to be rotated
        # In a 4X4 array, initially from 0 - 3 in the first layer and from 1 - 2 in the interior layer
        first = layer
        last = N - 1 - layer
        # Notice how i is never = last, the last element in the first row for example belongs to the right edge,
        # so last is omitted from the iteration. In a 4X4 array only elements 0 - 2 belong to the top edge
        for i in range(first, last):
            # offset will increase as the loop iterates
            # offset is used to specify which elements are currently being operated on.
            # Initially in all layers, offset = 0 because i == first, but as offset increases, the next 4 elements,
            # 1 element CW from the previous 4 will be operated on instead.
            offset = i - first

            # Saving value of the "topEdge" which in actuality is a single element related to offset which is a
            # function of i
            topEdge = matrix[first][i]

            # Moving left edge to the top
            # matrix[first] is constant for the top row
            # matrix[row][first] are elements in the left column (where row varies)
            matrix[first][i] = matrix[last - offset][first]

            # Moving bottom edge to the left
            # matrix[last] is constant for the bottom row
            matrix[last - offset][first] = matrix[last][last - offset]

            # Moving right edge to the bottom
            # matrix[row][last] are elements in the right column (where row varies)
            matrix[last][last - offset] = matrix[i][last]

            # Moving top edge to the right edge
            matrix[i][last] = topEdge
    return True


matrix = []
N = 4
count = 1

for i in range(N):
    row = []
    for j in range(N):
        row.append(count)
        count += 1
    matrix.append(row)

for i in range(N):
    print(matrix[i])

print()

rotateMatrix(matrix)

for i in range(N):
    print(matrix[i])
