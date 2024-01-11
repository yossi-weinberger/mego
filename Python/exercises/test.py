
list_num = []
list_max = []
list_min = []
temp_list = []
num_in = 0

while num_in < 99 or num_in > 999:
    num_in = int(input())
    list_num.append(num_in)
    temp_list = [int(x) for x in str(num_in)]
    list_max.append(max(temp_list))
    list_min.append(min(temp_list))

for i in range(len(list_num)):
    print(f"number: {list_num[i]} max: {list_max[i]} min: {list_min[i]}")