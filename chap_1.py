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
def oneAway(s: str, t:str) -> bool:
   return True
    







