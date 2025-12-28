from collections import Counter

#1.1
def isUnique(s: str) -> bool:
    return len(s) == len(Counter(s))

#1.2
def checkPermutation(s: str, t: str) -> bool:
    return False if len(s) != len(t) else Counter(s) == Counter(t)

#1.3
def URLify(s: str) -> str:
    s_lst = s.split()
    ans_lst = []
    i = 0
    if len(s_lst) == 1:
        if s.isalpha():
            return s
        else:
            return "%20"
    for i in range(len(s_lst) - 1):
        ans_lst.append(s_lst[i])
        ans_lst.append("%20")
    
    ans_lst.append(s_lst[i + 1])
    return "".join(ans_lst)

#1.4
def palindromePermutation(s: str) -> bool:
    s_letter_counts = Counter(s)
    odd_count = 0
    for letter_count in s_letter_counts.values():
        if letter_count % 2 == 0:
            continue
        else:
            if odd_count == 1:
                return False
            odd_count += 1
    
    return True

#1.5
def oneAway(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
       return False
    if len(s) > len(t):
       s, t = t, s
    ptr1 = ptr2 = 0
    found_diff = False
    while ptr1 < len(s) and ptr2 < len(t):
        if s[ptr1] != t[ptr2]:
            if found_diff:
                return False
            found_diff = True

            if len(s) != len(t):
                ptr2 += 1
        else:
            ptr1 += 1
            ptr2 += 1

    return True

#1.6
def stringCompression(s: str) -> str:
    if len(s) <= 1:
        return s
    ans = []
    ptr1 = ptr2 = 0
    while ptr1 < len(s):
        while ptr2 < len(s) and s[ptr2] == s[ptr1]:
            ptr2 += 1
        ans.append(s[ptr1])
        ans.append(str(ptr2 - ptr1))
        ptr1 = ptr2

    compressed = "".join(ans)
    return compressed if len(compressed) < len(s) else s

#1.7
def rotateMatrix(m: list[list[int]]) -> None:
    n = len(m)
    if n == 0 or any(len(row) != n for row in m):
        return
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i]
            m[first][i] = m[last - offset][first]
            m[last - offset][first] = m[last][last - offset]
            m[last][last - offset] = m[i][last]
            m[i][last] = top

#1.8
def zeroMatrix(m: list[list[int]]) -> None:
    if not m or not m[0]:
        return
    def nullify_row(row: int) -> None:
        for j in range(len(m[0])):
            m[row][j] = 0
    def nullify_col(col: int) -> None:
        for i in range(len(m)):
            m[i][col] = 0
    zero_rows = set()
    zero_columns = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    for row in zero_rows:
        nullify_row(row)
    for col in zero_columns:
        nullify_col(col)

#1.9 
def isRotation(s1: str, s2: str) -> bool:
    def isSubstring(s1: str, s2: str) -> bool:
        return s2 in s1
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return False

