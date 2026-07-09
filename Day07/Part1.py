input_data = open('/home/advent-of-code-2025/Day07/advent_of_code_7.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
SplitCount = 0
FullBeamIndexes = []
for i in range(len(input_data_lst[0])):
    if input_data_lst[0][i] == 'S':
        FullBeamIndexes.append(i)
        break
for row in range(1, len(input_data_lst)):
    if row%2 != 0:
        continue
    TempFullBeamIndexes = FullBeamIndexes.copy()
    for col in range(len(input_data_lst[0])):
        if input_data_lst[row][col] == '^':
            for beamIndex in FullBeamIndexes:
                if beamIndex == col:
                    SplitCount += 1
                    if beamIndex - 1 not in TempFullBeamIndexes:
                        TempFullBeamIndexes.append(beamIndex -1)
                    if beamIndex + 1 not in TempFullBeamIndexes:
                        TempFullBeamIndexes.append(beamIndex +1)
                    TempFullBeamIndexes.remove(beamIndex)
    FullBeamIndexes = TempFullBeamIndexes.copy()
print(SplitCount)
input_data.close()