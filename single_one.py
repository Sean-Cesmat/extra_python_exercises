# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***

def odd_man_out(list):
    odd_man = list[0]
    for n in list:
        if n == 0:
            odd_man == list[n]
        elif list[n] == list[n - 1]:
            odd_man = list[n + 1]
    return odd_man

print( odd_man_out([1,1,2,2,3,3,4,5,5,6,6,7,7]) )
