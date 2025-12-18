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




   
    







