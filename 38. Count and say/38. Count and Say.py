def countAndSay(n):
    rep = n
    dictionar = {}

    if rep == 1:
        print(f"{rep}")
    elif rep == 2:
        print("11")
    elif rep >= 3:
        n = 11
        for i in range(rep-2):
            for i in str(n):
                if i not in dictionar:
                    dictionar[i] = 1
                else:
                    dictionar[i] += 1

            output_string = ""

            for i in dictionar:
                output_string += str(dictionar[i])
                output_string += i
            
            n = int(output_string)
            dictionar = {}
            output_string = ""
            

        print(n)

countAndSay(1)
countAndSay(2)
countAndSay(3)
countAndSay(4)
        