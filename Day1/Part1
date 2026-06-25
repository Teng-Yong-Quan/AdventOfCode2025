input_data = open('advent-of-code-2025/Day1/advent_of_code_1.txt','r')
input_data_lst = [x for x in input_data]
ZeroCount = 0
CurrentValue = 50
for rotation in input_data_lst:
    RotationValue = 0
    if "L" in rotation:
        RotationValue = -int(rotation.replace("L",""))
    else:
        RotationValue = int(rotation.replace("R",""))
    CurrentValue += RotationValue 
    while CurrentValue < 0:
        CurrentValue += 100
    while CurrentValue >= 100:
        CurrentValue -= 100
    if CurrentValue == 0:
        ZeroCount += 1
print(ZeroCount)