# from distutils import cmd
from functools import cmp_to_key


# while True:
#     response = input("Enter a number:")
#     if int(response) % 7 == 0:
#         break

def custom_comparator(word1, word2):
    if word1 == word2:
        return 0

    p = 0
    
    while p <= len(word1) - 1 and p <= len(word2) - 1:
        diff = ord(word1[p]) - ord(word2[p]) 
        if diff != 0:
            return diff
        
        p += 1
    
    return -1 if p == len(word1) else 1

arr = ["bbb", "aaa", "abb", "abbbb"]

answer = sorted(arr, key=cmp_to_key(custom_comparator))
print(answer)