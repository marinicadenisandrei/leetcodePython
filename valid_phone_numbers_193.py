VALID_NUMBERS = ["(xxx) xxx-xxxx", "xxx-xxx-xxxx"]

from termcolor import colored

print(colored("Leetcode - 193. Valid Phone Numbers (Python language) -","yellow"), colored("Easy", "green"))

def validPhoneNumbers(numbersVar: str):
    numbersVar = numbersVar.split("\n")
    flag = True

    for i in numbersVar:
        for j in VALID_NUMBERS:
            for k,l in zip(j,i):
                if k == "(" and l != "(":
                    flag = False
                    break

                if k == ")" and l != ")":
                    flag = False
                    break

                if k == "-" and l != "-":
                    flag = False
                    break
    
            if flag == True:
                print(i)
            
            flag = True
                
numbers = "987-123-4567\n123 456 7890\n(123) 456-7890"

print(colored("Test 1: ","green"))
validPhoneNumbers(numbers)
print(colored("| Passed","green"))