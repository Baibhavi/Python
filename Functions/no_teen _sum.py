'''Given 3 int values, a b c, WAF no_teen_sum(a, b, c) that returns their sum. However, if any of the values 
is a teen i.e. in the range 13 to 19 inclusive, then that value counts as 0. Write a separate helper function
fix_teen(n) that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid 
repeating the teen code 3 times (i.e. "decomposition"). 
no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
'''
def no_teen_sum (a,b,c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0
    return n    
        
