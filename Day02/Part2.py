input_data = open('/home/advent-of-code-2025/Day02/advent_of_code_2.txt','r').read().strip()
input_data_lst = [part.split("-") for part in input_data.split(",")]
TotalInvalid = 0
for NestedRangeList in input_data_lst:
    Start = NestedRangeList[0]
    End = NestedRangeList[1]
    Current = Start
    while int(Current) <= int(End):
        CurrentStringLength = len(Current)
        factors = []
        for i in range(2, CurrentStringLength + 1):
            if CurrentStringLength % i == 0:
                factors.append(i)
        for factor in factors:
            SplitIndex = CurrentStringLength//factor
            segment = Current[:SplitIndex]
            if segment*factor == Current:
                TotalInvalid += int(Current)
                break
        Current = str(int(Current) + 1)
print(TotalInvalid)
input_data.close()