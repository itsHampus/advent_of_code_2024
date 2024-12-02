left_list = list()
right_list = list()

with open('./input/01.txt', "r") as f:
    for line in f:
        line_string_arr = line.rsplit()
        left_list.append(int(line_string_arr[0]))
        right_list.append(int(line_string_arr[1]))

left_list.sort() 
right_list.sort() 

diff_list = list()

for i in range(len(left_list)):
    diff_list.append(abs(left_list[i] - right_list[i]))

total_distance_sum = 0

for diff in diff_list:
    total_distance_sum += diff

print('total_distance_sum: ', total_distance_sum)