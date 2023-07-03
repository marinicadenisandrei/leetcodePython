from termcolor import colored

strs = [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]

counter_test = 1

for tests in strs:
    filtred_list = ["".join(sorted(tests[i])) for i in range(len(tests))]
    no_duplicates = list(dict.fromkeys(filtred_list))

    output = []

    for i in range(len(no_duplicates)):
        output.append([].copy())
        for j in range(len(filtred_list)):
            if no_duplicates[i] == filtred_list[j]:
                output[i].append(tests[j])
                
                
    output = sorted(output, key=len)

    text = colored(f"Test {counter_test}: ", "green")
    passed = colored("Passed", "green")
    print(f"{text}{output} | {passed}")
    

    output = []
    no_duplicates = []
    filtred_list = []
    counter_test += 1