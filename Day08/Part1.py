import math

input_data = open('/home/advent-of-code-2025/Day08/advent_of_code_8.txt','r')
input_data_lst = [[int(y) for y in x.replace("\n","").split(',')] for x in input_data]
PointsDistanceDict = {}
CurrentIndex = 0
while CurrentIndex < len(input_data_lst) - 1:
    FirstPoint = input_data_lst[CurrentIndex]
    for num in range(CurrentIndex + 1, len(input_data_lst)):
        SecondPoint = input_data_lst[num]
        DiffSquared = 0
        for i in range(len(FirstPoint)):
            DiffSquared += (FirstPoint[i] - SecondPoint[i])**2
        distance = math.sqrt(DiffSquared)
        PointsDistanceDict[(CurrentIndex,num)] = distance
    CurrentIndex +=1
PointsDistanceDict = dict(sorted(PointsDistanceDict.items(), key=lambda item: item[1]))
Circuits = []
for key in list(PointsDistanceDict.keys())[:1000]:
    CircuitsCopy = Circuits.copy()
    TemporaryCircuit = []
    for CircuitCopy in CircuitsCopy:
        if key[0] in CircuitCopy or key[1] in CircuitCopy:
            TemporaryCircuit.append(CircuitCopy)
            Circuits.remove(CircuitCopy)
            if list(key) not in TemporaryCircuit:
                TemporaryCircuit.append(list(key))
    if TemporaryCircuit == []:
        Circuits.append(list(key))
    else:
        NewCircuitSet = []
        for tempCircuit in TemporaryCircuit:
            NewCircuitSet += tempCircuit
        Circuits.append(list(set(NewCircuitSet)))
Circuits = list(sorted(Circuits, key = lambda circuit: len(circuit), reverse = True))
LargestThreeCircuits = 1
for x in Circuits[:3]:
    LargestThreeCircuits*= len(x)
print(LargestThreeCircuits)
input_data.close()