# 1. Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row
# and column to O's. You must do it in place.

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# 1 0

# 0 0

# 1 0

# 1

# 1

# 1

# 1

# 0

# 1

# 1

# 1

# 1

# 1

# 0

# 1


def matrix_zeroes(arr):
    arr1 = [row.copy() for row in arr]  
    rows = len(arr)
    cols = len(arr[0])
    
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                for n in range(cols):
                    arr1[i][n] = 0
                for n in range(rows):
                    arr1[n][j] = 0
                    
    return arr1

print(matrix_zeroes([[1,1,1],[1,0,1],[1,1,1]]))