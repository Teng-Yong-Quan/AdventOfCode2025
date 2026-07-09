input_data = open('/home/advent-of-code-2025/Day06/advent_of_code_6.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
total = 0
CurrentIndex = len(input_data_lst[0]) - 1
AllDigits = []
while CurrentIndex >= 0:
    CurrentDigit = ''
    CurrentSymbol = ''
    for index in range(len(input_data_lst) - 1):
        CurrentDigit += input_data_lst[index][CurrentIndex]
    CurrentSymbol = input_data_lst[-1][CurrentIndex].replace(" ","")
    CurrentDigit = CurrentDigit.replace(" ","")
    if CurrentSymbol == "":
        if CurrentDigit != "":
            AllDigits.append(int(CurrentDigit))
    elif CurrentSymbol == "+":
        AllDigits.append(int(CurrentDigit))
        total += sum(AllDigits)
        AllDigits = []
    else:
        AllDigits.append(int(CurrentDigit))
        CurrentTotal = 1
        for num in AllDigits:
            CurrentTotal *= num
        total += CurrentTotal
        AllDigits = []
    CurrentIndex -= 1
print(total)
input_data.close()