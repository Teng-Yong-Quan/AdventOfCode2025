input_data = open('/home/advent-of-code-2025/Day02/advent_of_code_2.txt','r').read().strip()
input_data_lst = [part.split("-") for part in input_data.split(",")]
TotalInvalid = 0
for NestedRangeList in input_data_lst:
    Start = NestedRangeList[0]
    End = NestedRangeList[1]
    Current = Start
    while int(Current) <= int(End):
        if len(Current)%2 == 0:
            HalfIndex =  len(Current)//2
            FirstHalf = Current[:HalfIndex]
            SecondHalf = Current[HalfIndex:]
            if FirstHalf == SecondHalf:
                TotalInvalid += int(Current)
        Current = str(int(Current) + 1)
print(TotalInvalid)