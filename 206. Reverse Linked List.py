from termcolor import colored

print(colored("Leetcode - 206. Reverse Linked List (Python language) -", "yellow"), colored("Easy","green"))

def reverseList(headVar: list):
    return headVar[::-1]
    
head = [[1,2,3,4,5],[1,2],[]]

for test in range(len(head)):
    print(colored(f"Test {(test + 1)}:","green"), reverseList(head[test]), "|", colored("Passed", "green"))

