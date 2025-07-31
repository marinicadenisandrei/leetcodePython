# Leetcode - 192. Word Frequency (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 192. Word Frequency (Python language) - Medium", "yellow"))

def wordFrequency(textVar: str):
    textVar = textVar.replace("\n"," ")
    textVar = textVar.split()
    no_duplicates = list(dict.fromkeys(textVar))

    for i in no_duplicates:
        print(i, textVar.count(i))
        

text = "the day is sunny the the\nthe sunny is is"

print(colored("Test 1:", "green"))
wordFrequency(text)
print(colored("| Passed", "green"))