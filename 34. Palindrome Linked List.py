# Leetcode - 234. Palindrome Linked List (Python language) - Easy 

from termcolor import colored
print(colored("Leetcode - 234. Palindrome Linked List (Python language) -", "yellow"), colored("Easy", "green"))

def isPalindrome(headVar):
    return headVar == headVar[::-1]

head = [[1,2,2,1],[1,2]]

for test in range(len(head)):
    print(colored(f"Test {(test + 1)}:", "green"), isPalindrome(head[test]), "|", colored("Passed","green"))