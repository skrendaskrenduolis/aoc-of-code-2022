import re
add_to_folder = False
directory_dict = dict()


adress = ''
directory_check = None
file_check = None
with open('aoc_7_input.txt', 'r') as infile:
    for line in infile:


        
        make_folder_check = re.search(r'\$ cd (.+)', line)
        if make_folder_check is not None:
            folder = make_folder_check.group(1)
            if folder != '..':
                adress += f'{folder}/'
                directory_dict[adress] = {}
            else:
                adress = re.sub(fr'/([^/]*\/$)', '', adress)
                adress += '/'


        directory_check = re.search(r'dir (.+)', line)
        if directory_check is not None:
            sub_folder = f"{adress}{directory_check.group(1)}/"
            directory_dict[adress][sub_folder] = {}


        file_check = re.search(r'(\d+) (.+)', line)
        if file_check is not None:
            file_size = file_check.group(1)
            file_name = f"{adress}{file_check.group(2)}/"
            directory_dict[adress][file_name] = int(file_size)
            

        

for key, value in directory_dict.items():
    for sub_key, sub_value in value.items():
        if sub_key in directory_dict:
            value[sub_key] = directory_dict[sub_key]




def directory_under_100k(dict):
    total_sum = 0
    under_100k_sum = 0
    for key, value in dict.items():
        if type(value) is int:
            total_sum += value
        else:
            temp1, temp2 = directory_under_100k(value)
            total_sum += temp1
            under_100k_sum += temp2
    if total_sum < 100000:
        under_100k_sum += total_sum
    return total_sum, under_100k_sum

print(directory_under_100k(directory_dict['//'])[1])



unused_space = 70000000 - directory_under_100k(directory_dict['//'])[0]
space_to_free_up = 30000000 - unused_space
print(space_to_free_up)

smallest_possible = None
def smallest_dir_size_to_delete(dict):
    global smallest_possible
    total_sum = 0
    treshold = 0

    for key, value in dict.items():
        if type(value) is int:
            total_sum += value
        else:
            temp1, temp2 = smallest_dir_size_to_delete(value)
            total_sum += temp1
            treshold += temp2

    if total_sum >= space_to_free_up:
        if smallest_possible is None:
            smallest_possible = total_sum
        elif total_sum < smallest_possible:
            smallest_possible = total_sum
    return total_sum, treshold


smallest_dir_size_to_delete(directory_dict['//'])
print(smallest_possible)
