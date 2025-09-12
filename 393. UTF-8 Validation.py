from termcolor import colored

print(colored("Leetcode - 393. UTF-8 Validation (Python language) - Medium","yellow"))

def validUtf8(dataVar):
    n = 0

    for byte in dataVar:
        if n == 0:
            if (byte >> 5) == 0b110:
                n = 1
            elif (byte >> 4) == 0b1110:
                n = 2
            elif (byte >> 3) == 0b11110:
                n = 3
            elif (byte >> 7): 
                return False
        else:
            if (byte >> 6) != 0b10:  
                return False
            n -= 1

    return n == 0

data = [[192, 130, 1], [235, 140, 4]]

for test in range(len(data)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        validUtf8(data[test]), 
        "|",
        colored("Passed","green")
    )
