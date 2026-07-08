input_data = open('/home/advent-of-code-2025/Day5/advent_of_code_5.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
FreshIngredientRangeList = []
FinalisedIngredientRangeList = []
FreshIngredientCount = 0
for line in input_data_lst:
    if "-" in line:
        StartEnd = line.split("-")
        Start = int(StartEnd[0])
        End = int(StartEnd[1])
        FreshIngredientRangeList.append((Start,End))
FreshIngredientRangeList = sorted(FreshIngredientRangeList, key = lambda x : x[0], reverse = False)
CurrentMin, CurrentMax = FreshIngredientRangeList[0][0], FreshIngredientRangeList[0][1]
for EachRange in FreshIngredientRangeList:
    Overlap = False
    CurrentStart = EachRange[0]
    CurrentEnd = EachRange[1]
    if CurrentStart <= CurrentMax:
        if CurrentEnd > CurrentMax: 
            CurrentMax = CurrentEnd
        Overlap = True
    if not Overlap:
        FinalisedIngredientRangeList.append((CurrentMin,CurrentMax))
        CurrentMin = CurrentStart
        CurrentMax = CurrentEnd
FinalisedIngredientRangeList.append((CurrentMin,CurrentMax))
for EachFinalisedRange in FinalisedIngredientRangeList:
    FinalisedStart = EachFinalisedRange[0]
    FinalisedEnd = EachFinalisedRange[1]
    FreshIngredientCount += (FinalisedEnd - FinalisedStart + 1)
print(FreshIngredientCount)