from termcolor import colored

print(colored("Leetcode - 166. Fraction to Recurring Decimal (Python language) - Medium", "yellow"))

def fractionToDecimal(numeratorVar: int, denominatorVar: int):
    fraction = str(numeratorVar / denominatorVar)
    fraction = fraction.split(".")

    temp = ""
    bigString = ""
    maxVar = 0

    for i in fraction[1]:
        temp += i
        
        if fraction[1].count(temp) >= maxVar and len(temp) > 1:
            maxVar = fraction[1].count(temp)
            bigString = temp

    if maxVar > 0:            
        return f"{fraction[0]}.({bigString})"
    else:
        return f"{fraction[0]}.{fraction[1][0]}"
    

numerator = [1,2,4] 
denominator = [2,1,333]

for test in range(len(numerator)):
    print(colored(f"Test {test + 1}:","green"),fractionToDecimal(numerator[test], denominator[test]),"|",colored("Passed","green"))
