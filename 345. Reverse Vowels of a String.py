from termcolor import colored

print(colored("Leetcode - 345. Reverse Vowels of a String (Python language) -","yellow"), colored("Easy","green"))

def reverseVowels(sVar):
    s_list = list(sVar) 
    vowels = 'aeiouAEIOU'

    vowel_indices = [i for i, ch in enumerate(s_list) if ch in vowels]
    
    i, j = 0, len(vowel_indices) - 1
    while i < j:
        s_list[vowel_indices[i]], s_list[vowel_indices[j]] = s_list[vowel_indices[j]], s_list[vowel_indices[i]]
        i += 1
        j -= 1
    
    return ''.join(s_list)

s = ["IceCreAm", "leetcode"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:","green"), reverseVowels(s[test]), "|", colored("Passed","green"))
    
