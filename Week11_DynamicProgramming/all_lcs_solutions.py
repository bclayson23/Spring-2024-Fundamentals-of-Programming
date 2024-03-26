# RECURSION #
def lcs_rec(A, B, i, j):
    global calls
    calls += 1
    if len(A) == 0 or len(B) == 0 or A[i] == '\0' or B[j] == '\0':
        # return 0
        return " "
    elif A[i] == B[j]:
        # return 1 + lcs_rec(A, B, i+1, j+1)
        return A[i] + lcs_rec(A, B, i + 1, j + 1)
    else:
        # return max(lcs_rec(A, B, i+1, j), lcs_rec(A, B, i, j+1))
        return max(lcs_rec(A, B, i + 1, j), lcs_rec(A, B, i, j + 1), key=len)


calls = 0
# str1 = "bd"
# str2 = "abcd"

str1 = "CGATAATTGAGA"
str2 = "GTTCCTAATA"

str1 = str1 + "\0"
str2 = str2 + "\0"

# seq_len = lcs_rec(A=str1, B=str2, i=0, j=0)
# print(seq_len)


lcs_char = lcs_rec(A=str1, B=str2, i=0, j=0)
print(lcs_char)
print(f"Recursion Calls: {calls}")


# MEMORIZATION #
def lcs_memorization(A, B, i, j):
    global lcs_memo, calls
    calls += 1
    if len(A) == 0 or len(B) == 0 or A[i] == '\0' or B[j] == '\0':
        return 0
    if lcs_memo[i][j] == ' ':
        if A[i] == B[j]:
            lcs_memo[i][j] = 1 + lcs_memorization(A, B, i + 1, j + 1)
        else:
            lcs_memo[i][j] = max(lcs_memorization(A, B, i + 1, j), lcs_memorization(A, B, i, j + 1))
    return lcs_memo[i][j]


calls = 0
# str1 = "bd"
#  = "abcd"

str1 = "CGATAATTGAGA"
str2 = "GTTCCTAATA"

str1 = str1 + "\0"
str2 = str2 + "\0"

lcs_memo = []

for _ in range(len(str1)):
    # print([" "] * len(str2))
    lcs_memo.append([" "] * len(str2))

# print(lcs_memo)

seq_len = lcs_memorization(A=str1, B=str2, i=0, j=0)
print(seq_len)
print(f"Memorization Calls: {calls}")


# TABULATION #
def find_lcs(x, y):
    len_x = len(x)
    len_y = len(y)

    lcs_array = []
    for _ in range(len_x + 1):  # UNDERSCORE IS PLACEHOLDER
        empty_row = [0] * (len_y + 1)
        lcs_array.append(empty_row)

    for arr_row in lcs_array:
        print(arr_row)

    # lcs_array1 = [[0] * len_y for _ in range(len_x+1)]

    for row in range(1, len_x + 1):
        for col in range(1, len_y + 1):
            if x[row - 1] == y[col - 1]:
                lcs_array[row][col] = 1 + lcs_array[row - 1][col - 1]
            else:
                lcs_array[row][col] = max(lcs_array[row - 1][col], lcs_array[row][col - 1])
    return lcs_array[row][col]


str1 = "stone"
str2 = "longest"
print(find_lcs(str1, str2))
