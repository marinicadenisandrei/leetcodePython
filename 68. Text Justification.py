# Leetcode - 68. Text Justification (Python Language)

from termcolor import colored

print(colored("Leetcode - 68. Text Justification (Python Language)", "yellow"))
state = colored("Passed", "green")

wordsTest = [["This", "is", "an", "example", "of", "text", "justification."],
             ["What","must","be","acknowledgment","shall","be"],
             ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]]

maxWidthTest = [16,16,20]

for test, value in zip(wordsTest, maxWidthTest):
    words = test
    maxWidth = value

    wordFormation = ""
    returnString = ""
    listOfWords = []

    output = []

    while len(words) > 0:
        for i in words:
            if len(wordFormation + i) + len(wordFormation.split()) <= maxWidth:
                wordFormation += i + " "
            else:
                returnString = i
                break
        
        if len(wordFormation) + len(returnString) <= maxWidth:
            wordFormation += returnString

        if wordFormation[-1] == " ":
            wordFormation = wordFormation[:len(wordFormation)-1]

        listOfWords.append(wordFormation)

        words = words[len(wordFormation.split(" ")):]
        wordFormation = ""
        returnString = ""

    for i in listOfWords:
        if len(i.split(" ")) > 1:
            spaces = maxWidth - len(i) + len(i.split(" ")) - 1
            text = i.split(" ")
                
            while spaces != 0:
                for i in range(len(text)-1):
                    text[i] += " "
                    spaces -= 1

                    if spaces == 0: break

            finalString = ' '.join([str(elem) for elem in text])
            output.append(finalString)
            
            finalString = ""
            spaces = 0
            text = []
        else:
            spaces = maxWidth - len(i)
            text = i

            for i in range(spaces):
                text += " "
            
            output.append(text)

            text = ""
            spaces = 0

    testNumber = wordsTest.index(test) + 1
    text = colored(f"Test {testNumber}: ", "green")

    print(text)

    for i in output:
        print(i)
    
    print("| ",state)

    print("\n")







