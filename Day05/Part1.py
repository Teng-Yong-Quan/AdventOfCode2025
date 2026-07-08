input_data = open('/home/advent-of-code-2025/Day05/advent_of_code_5.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
FreshIngredientRangeList = []
FreshIngredientCount = 0
for line in input_data_lst:
    if not "-" in line and line != "":
        for EachRange in FreshIngredientRangeList:
            StartEnd = EachRange.split("-")
            Start = int(StartEnd[0])
            End = int(StartEnd[1])
            if int(line) >= Start and int(line) <= End:
                FreshIngredientCount += 1
                break
    elif "-" in line:
        FreshIngredientRangeList.append(line)
print(FreshIngredientCount)