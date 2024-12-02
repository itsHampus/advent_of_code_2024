left_list = list()
right_list = list()

with open('./input/01.txt', 'r') as f:
    for line in f:
        line_string_arr = line.rsplit()
        left_list.append(int(line_string_arr[0]))
        right_list.append(int(line_string_arr[1]))

left_list.sort() 
right_list.sort()

similarity_score_list = list()

for i in range(len(left_list)):
    the_number_of_times_score_appears = right_list.count(left_list[i]) 
    similarity_score_list.append(left_list[i] * the_number_of_times_score_appears)

total_score = 0

for score in similarity_score_list:
    total_score += score

print('total_score: ', total_score)