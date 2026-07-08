def dfs_stack(graph, start, end, start_count):
    # Initialize visited dictionary
    visited = {node: 0 for node in graph}
    visited[start] = start_count
    visited["out"] = 0  # special key
    graph["out"] = []
    height = {node: 0 for node in graph}
    height["out"] = 0
    
    current_nodes = [start]
    while current_nodes:
        next_nodes = []
        for parent in current_nodes:
            if parent not in (end, "out"):
                for child in graph[parent]:
                    height[child] = height[parent] + 1
                    # Only append once
                    if child not in next_nodes:
                        next_nodes.append(child)
        current_nodes = next_nodes
    #print(height)
    current_nodes = [start]
    while current_nodes:
        next_nodes = []
        for parent in current_nodes:
            if parent not in (end, "out"):
                for child in graph[parent]:
                    visited[child] += visited[parent]
                    # Only append once
                    if child not in next_nodes and height[child] == height[parent] + 1:
                        next_nodes.append(child)
        current_nodes = next_nodes
    #print(visited)
    return visited[end]

input_data = open('/home/advent-of-code-2025/Day11/advent_of_code_11.txt','r')
input_data_lst = [x.replace("\n","").split(':') for x in input_data]
input_dict = {key:value.strip().split(' ') for key,value in input_data_lst}
print(dfs_stack(input_dict,'svr','fft',1)*dfs_stack(input_dict,'fft','dac',1)*dfs_stack(input_dict,'dac','out',1))