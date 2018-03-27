# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***
def reverse_string(string):
    loop_list = []
    new_string = []
    for word in string:
        for letter in word:
           loop_list.append(letter)
    loop_legnth = len(loop_list)
    for i in range(loop_legnth):
        new_string.append(loop_list.pop())
    print(new_string)




reverse_string("Let's do a coding challenge")
reverse_string("is this right?")
