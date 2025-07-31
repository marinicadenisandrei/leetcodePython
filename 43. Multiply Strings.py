num1 = "123"
num2 = "456"

# num1 = "2"
# num2 = "3"


def stringToInt(stringInteger):

    lungime = len(stringInteger)
    final_integer = 0
    var_div = int(10**lungime/10)

    for i in stringInteger:
        final_integer = final_integer + (int(i) * var_div)
        var_div /= 10

    return final_integer

print(int(stringToInt(num1)*stringToInt(num2)))


