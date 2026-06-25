input_data = open('/home/advent-of-code-2025/Day6/advent_of_code_6.txt','r')
input_data_lst = [[y for y in x.replace("\n","").split(" ") if y != ''] for x in input_data]
total = 0
for index in range(len(input_data_lst[0])):
    if input_data_lst[-1][index] == '+':
        total += (int(input_data_lst[0][index]) + int(input_data_lst[1][index]) + int(input_data_lst[2][index]) + int(input_data_lst[3][index]))
    else:
        total += (int(input_data_lst[0][index]) * int(input_data_lst[1][index]) * int(input_data_lst[2][index]) * int(input_data_lst[3][index]))
print(total)