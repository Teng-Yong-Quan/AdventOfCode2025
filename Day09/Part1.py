input_data = open('/home/advent-of-code-2025/Day09/advent_of_code_9.txt','r')
input_data_lst = [tuple(int(y) for y in x.replace("\n","").split(',')) for x in input_data]
PointsAreaDict = {}
CurrentIndex = 0
while CurrentIndex < len(input_data_lst) - 1:
    FirstPoint = input_data_lst[CurrentIndex]
    for num in range(CurrentIndex + 1, len(input_data_lst)):
        SecondPoint = input_data_lst[num]
        Length = abs(FirstPoint[0] - SecondPoint[0]) + 1
        Breadth = abs(FirstPoint[1] - SecondPoint[1]) + 1
        Area = Length*Breadth
        PointsAreaDict[(CurrentIndex,num)] = Area
    CurrentIndex += 1
PointsAreaDict = dict(sorted(PointsAreaDict.items(), key=lambda item: item[1], reverse = True)) 
print(list(PointsAreaDict.values())[0])
input_data.close()