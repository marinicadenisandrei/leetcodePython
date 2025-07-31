# Leetcode - 196. Delete Duplicate Emails (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 196. Delete Duplicate Emails (Python language) -","yellow"), colored("Easy","green"))

def deleteDuplicateEmails(fileVar: list):
    for i in list(dict.fromkeys(fileVar)):
        print(i)

file = ["john@example.com","bob@example.com","john@example.com"]
print(colored("Test 1:","green"))
deleteDuplicateEmails(file)
print(colored("| Passed","green"))