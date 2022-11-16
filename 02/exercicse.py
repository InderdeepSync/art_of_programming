"""
For a given n, print the following pattern to the console:

Input: n = 4 
Output: 
1 1 1 1 1 1 1 
1 2 2 2 2 2 1 
1 2 3 3 3 2 1 
1 2 3 4 3 2 1 
1 2 3 3 3 2 1 
1 2 2 2 2 2 1 
1 1 1 1 1 1 1

Input: n = 2
Output: 
1 1 1 
1 2 1 
1 1 1

"""
n=3

def display_pattern(num: int):
    for i in range(n*2-1):
        # print (i+1)
        a = 0
        for j in range(n*2-1):
            if (a == i):
                print (a, end="")
            elif (a < i):
                print (a, end="")
                a+=1
        print()

display_pattern(n)

