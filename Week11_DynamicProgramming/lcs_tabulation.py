# Tabulation

def find_lcs(x, y):
    len_x = len(x)
    len_y = len(y)

    lcs_array = []
    for _ in range(len_x + 1):  # UNDERSCORE IS PLACEHOLDER
        empty_row = [0] * len_y
        lcs_array.append(empty_row)

    # lcs_array1 = [[0] * len_y for _ in range(len_x+1)]

    for row in range(1, len_x):
        for col in range(1, len_y):
            if x[row] == y[col]:
                lcs_array[row][col] = 1 + lcs_array[row - 1][col - 1]
            else:
                lcs_array[row][col] = max(lcs_array[row - 1][col], lcs_array[row][col - 1])
    return lcs_array[row][col]


str1 = "bd"
str2 = "abcd"
print(find_lcs(str1, str2))
