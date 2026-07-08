input_data = open('/home/advent-of-code-2025/Day7/advent_of_code_7.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
StartingIndex = -1
FullBeamDict = {}
for i in range(len(input_data_lst[0])):
    if input_data_lst[0][i] == 'S':
        StartingIndex = i
        FullBeamDict[i] = []
        FullBeamDict[i].append(1)
        break
for row in range(1, len(input_data_lst)):
    if row%2 != 0:
        continue
    for col in range(len(input_data_lst[0])):
        if input_data_lst[row][col] == '^':
            for beamIndex in list(FullBeamDict.keys()):
                if beamIndex == col:
                    if beamIndex - 1 not in list(FullBeamDict.keys()):
                        FullBeamDict[beamIndex - 1] = []
                    FullBeamDict[beamIndex -1].append(FullBeamDict[beamIndex][0])
                    if beamIndex + 1 not in list(FullBeamDict.keys()):
                        FullBeamDict[beamIndex + 1] = []
                    FullBeamDict[beamIndex +1].append(FullBeamDict[beamIndex][0])
                    FullBeamDict.pop(beamIndex)    
    for Index in list(FullBeamDict.keys()):
        FullBeamDict[Index] = list([sum(FullBeamDict[Index]),])        
total = 0
for key in FullBeamDict.keys():
    total += FullBeamDict[key][0]
print(total)