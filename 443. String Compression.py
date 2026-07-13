# Leetcode - 443. String Compression (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 443. String Compression (Python language) - Medium", "yellow"))

def compress(charsVar):
    return len(list(dict.fromkeys(charsVar))) * 2
    

chars = [["a","a","b","b","c","c","c"],["a"],["a","b","b","b","b","b","b","b","b","b","b","b","b"]]

for test in range(len(chars)):
    print(
        colored(f"Test {test + 1}:", "green"),
        compress(chars[test]),
        "|",
        colored("Passed","green")
    )