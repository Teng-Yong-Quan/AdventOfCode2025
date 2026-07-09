input_data = open('/home/advent-of-code-2025/Day04/advent_of_code_4.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
totalCount = 0
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
                totalCount += 1
print(totalCount)
input_data.close()