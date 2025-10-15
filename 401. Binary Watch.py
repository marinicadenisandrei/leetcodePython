# Leetcode - 401. Binary Watch (Python language) - Easy 

from termcolor import colored

print(colored("Leetcode - 401. Binary Watch (Python language) -", "yellow"), colored("Easy","green"))

def readBinaryWatch(turnedOnVar):
    results = []

    for hour in range(12):
        for minute in range(60):
            if bin(hour).count('1') + bin(minute).count('1') == turnedOnVar:
                results.append(f"{hour}:{minute:02d}")
    
    return results
                
turnedOn = [1,9]

for test in range(len(turnedOn)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        readBinaryWatch(turnedOn[test]),
        "|",
        colored("Passed","green")
    )
    