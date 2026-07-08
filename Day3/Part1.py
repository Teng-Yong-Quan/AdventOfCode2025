input_data = open('/home/advent-of-code-2025/Day3/advent_of_code_3.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
LargestJoltage = 0
for bank in input_data_lst:
    NumberIndexDict = {}
    for BatteryIndex in range(len(bank)):
        CurrentBattery = bank[BatteryIndex]
        if int(CurrentBattery) not in NumberIndexDict.keys():
            NumberIndexDict[int(CurrentBattery)] = []
        NumberIndexDict[int(CurrentBattery)].append(BatteryIndex)
    NumberIndexDict = dict(sorted(NumberIndexDict.items(), reverse=True))     
    HighestKey = list(NumberIndexDict.keys())[0]
    SecondHighestKey = list(NumberIndexDict.keys())[1]
    LargestValue = 0
    if len(NumberIndexDict[HighestKey]) > 1:
        LargestValue = int(str(HighestKey)*2)
    elif max(NumberIndexDict[SecondHighestKey]) > min(NumberIndexDict[HighestKey]):
        LargestValue = int(str(HighestKey) + str(SecondHighestKey))
    else:
        IsFound = False
        while not IsFound:
            if min(NumberIndexDict[HighestKey]) == len(bank) - 1:
                LargestValue = int(str(SecondHighestKey) + str(HighestKey))
                IsFound = True
            else:
                SecondHighestKeyIndex = list(NumberIndexDict.keys()).index(SecondHighestKey) + 1 
                SecondHighestKey = list(NumberIndexDict.keys())[SecondHighestKeyIndex]
                if max(NumberIndexDict[SecondHighestKey]) > min(NumberIndexDict[HighestKey]):
                    LargestValue = int(str(HighestKey) + str(SecondHighestKey))
                    IsFound = True
    LargestJoltage += LargestValue 
print(LargestJoltage)