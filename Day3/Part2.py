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
    LargestValueString = ''
    Substring = ''
    RangeStart = 0
    RangeEnd = len(bank) - 12
    for i in range(12):
        for key in list(NumberIndexDict.keys()):
            CurrentIndex = NumberIndexDict[key][0]
            for index in NumberIndexDict[key]:
                if index >= RangeStart and index <= RangeEnd:
                    CurrentIndex = index
                    break
            if CurrentIndex == RangeEnd:
                Substring = bank[RangeEnd:]
                break
            elif CurrentIndex < RangeEnd and RangeStart <= CurrentIndex:
                LargestValueString += bank[CurrentIndex]
                RangeStart = CurrentIndex + 1
                RangeEnd += 1
                break
            else:
                continue
        if Substring != '':
           break
    LargestValueString += Substring
    LargestValue = int(LargestValueString)
    LargestJoltage += LargestValue 
print(LargestJoltage)