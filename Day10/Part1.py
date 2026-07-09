import re
import ast

def parse_line(text):
    # get bracket part (as string)
    bracket_m = re.search(r"\[.*?\]", text)
    bracket = bracket_m.group() if bracket_m else None

    # get contents of all parentheses (without the surrounding parens)
    paren_contents = re.findall(r"\(([^()]*)\)", text)

    tuples_list = []
    for s in paren_contents:
        # split on commas, strip spaces and ignore empty pieces
        parts = [p.strip() for p in s.split(',') if p.strip() != ""]
        # convert to ints (or leave as empty tuple if no parts)
        if not parts:
            tup = tuple()
        else:
            nums = [int(p) for p in parts]
            tup = tuple(nums)
        # Ensure single-element stays a tuple, e.g. (3,) not 3
        tuples_list.append(tup)

    # parse set part safely
    set_m = re.search(r"\{.*?\}", text)
    the_set = [int(z) for z in set_m.group().replace("{","").replace("}","").split(",")]

    return bracket, tuples_list, the_set

import itertools

input_data = open('/home/advent-of-code-2025/Day10/advent_of_code_10.txt','r')
input_data_lst = [x.replace("\n","") for x in input_data]
machines = []
buttons = []
joltages = []
for line in input_data_lst:
    bracket_part, tuples_list, the_set = parse_line(line)
    machines.append(bracket_part.replace("[","").replace("]",""))
    buttons.append(tuples_list)
    joltages.append(the_set)
LeastNumberButtons = []

for index in range(len(machines)):
    CurrentMachine = machines[index]
    CurrentButtons = buttons[index]
    all_permutations = list(itertools.product([0,1], repeat=len(CurrentButtons)))
    PassPermutationsIndex = []
    for perm in range(len(all_permutations)):
        NewMachineString = '.' * len(CurrentMachine)
        for perm_index in range(len(all_permutations[perm])):
            if all_permutations[perm][perm_index] == 0:
                continue
            else:
                CurrentButton = CurrentButtons[perm_index]
                for i in CurrentButton:
                    if NewMachineString[i] == '.':
                        NewMachineString = NewMachineString[:i] + '#' + NewMachineString[i+1:]
                    else:
                        NewMachineString = NewMachineString[:i] + '.' + NewMachineString[i+1:]
        if NewMachineString == machines[index]:
            PassPermutationsIndex.append(perm)
    MinPress = min([sum(all_permutations[x]) for x in PassPermutationsIndex])     
    LeastNumberButtons.append(MinPress)
print(sum(LeastNumberButtons))
input_data.close()