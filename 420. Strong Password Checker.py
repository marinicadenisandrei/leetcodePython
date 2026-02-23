# Leetcode - 420. Strong Password Checker (Python language) - Hard

import re
from termcolor import colored

print(colored("Leetcode - 420. Strong Password Checker (Python language) -", "yellow"), colored("Hard","red"))

def strongPasswordChecker(passwordVar: str) -> int:
    has_number = any(ch.isdigit() for ch in passwordVar)
    has_upper  = any(ch.isupper() for ch in passwordVar)
    has_bad_run = bool(re.search(r"(.)\1{2,}", passwordVar))
    no_run = not has_bad_run

    checker = [has_number, has_upper, no_run]
    missing = checker.count(False)

    if len(passwordVar) < 6:
        need_len = 6 - len(passwordVar)
        return max(need_len, missing)
    elif missing == 0:
        return 0
    else:
        return missing

password = ["a","aA1","1337C0d3"]

for test in range(len(password)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        strongPasswordChecker(password[test]),
        "|",
        colored("Passed","green")
    )
