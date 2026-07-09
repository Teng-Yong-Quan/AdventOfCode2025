input_data = open('/home/advent-of-code-2025/Day04/advent_of_code_4.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
totalCount = 0
PreviousTotalCount = -1
while PreviousTotalCount != totalCount:
    PreviousTotalCount = totalCount
    RemovedPaperRollLocation = []
    for row in range(len(input_data_lst)):
        for col in range(len(input_data_lst[row])):
            CurrentLocation = input_data_lst[row][col]
            if CurrentLocation != '@':
                continue
            else:
                PaperRollLocation = []
                for neighbourRow in range(row-1,row+2,1):
                    for neighbourCol in range(col-1,col+2,1):
                       if neighbourRow < 0 or neighbourRow == len(input_data_lst) or neighbourCol < 0 or neighbourCol == len(input_data_lst[row]):
                           continue
                       if neighbourRow == row and neighbourCol == col:
                           continue
                       if input_data_lst[neighbourRow][neighbourCol] == '@':
                           PaperRollLocation.append((neighbourRow,neighbourCol))
                if len(PaperRollLocation) < 4:
                    RemovedPaperRollLocation.append((row,col))
                    totalCount += 1
    for rowcol in RemovedPaperRollLocation:
        ReplacedRow = rowcol[0]
        ReplacedCol = rowcol[1]
        CurrentString = input_data_lst[ReplacedRow]
        input_data_lst[ReplacedRow] = CurrentString[:ReplacedCol] + 'X' + CurrentString[ReplacedCol + 1:]
print(totalCount)
input_data.close()