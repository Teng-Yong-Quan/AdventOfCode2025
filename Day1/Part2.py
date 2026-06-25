input_data = open('/home/advent-of-code-2025/Day1/advent_of_code_1.txt','r')
input_data_lst = [x for x in input_data]
ZeroCount = 0
CurrentValue = 50
for rotation in input_data_lst:
    RotationValue = 0
    if "L" in rotation:
        RotationValue = int(rotation.replace("L",""))
        for i in range(RotationValue):
            CurrentValue -= 1
            if CurrentValue == 0:
                ZeroCount += 1
            if CurrentValue < 0:
                CurrentValue = 99
    else:
        RotationValue = int(rotation.replace("R",""))
        for i in range(RotationValue):
            CurrentValue += 1
            if CurrentValue == 100:
                ZeroCount += 1
                CurrentValue = 0
print(ZeroCount)