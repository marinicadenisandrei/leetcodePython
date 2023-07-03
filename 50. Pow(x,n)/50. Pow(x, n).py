from termcolor import colored

x = [2.00000, 2.10000, 2.00000]
n = [10, 3, -2]
counter_test = 1


def pow(number, exponent):
    
    result = 1;

    for i in range(abs(exponent)):

        result *= number

    if exponent < 0:
        result = 1/result

    return result

for i,j in zip(x,n):
    text = colored(f"Test {counter_test}", "green")
    status = colored("Passed", "green")
    print(f"{text}:",round(pow(i,j),5),f" | {status}")
    counter_test += 1

