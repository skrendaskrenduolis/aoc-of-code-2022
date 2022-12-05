import re


def transpose_reverse(matrix):
    result_matrix = []
    transposed = [[matrix[j][i]
                   for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for row in transposed:
        no_gaps = [item for item in row if item != '   ']
        no_gaps.reverse()
        result_matrix.append(no_gaps)
    return result_matrix


crate_setup = True
crate_matrix = []
with open('aoc_5_input.txt', 'r') as infile:
    for line in infile:

        if crate_setup:
            column_search = re.search(r'(\[[A-Z]\]|\s{3})(?:\s{1})', line)
            if column_search is not None:
                column_compile = re.compile(r'(\[[A-Z]\]|\s{3})(?:\s{1})')
                crate_matrix_row = []
                for x in re.finditer(column_compile, line):
                    crate_matrix_row.append(
                        str(x.group(1)).rstrip(']').lstrip('['))
                crate_matrix.append(crate_matrix_row)
            else:
                modified_crate_matrix_1, modified_crate_matrix_2 = transpose_reverse(crate_matrix), transpose_reverse(crate_matrix)
                crate_setup = False

        if crate_setup is False:
            instruction_search = re.search(
                r'move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)', line)
            if instruction_search is not None:
                moving_number = int(instruction_search.group(1))  # 1
                crate_start_index = int(instruction_search.group(2)) - 1  # 1
                crate_end_index = int(instruction_search.group(3)) - 1  # 0
                
                remaining_crates = moving_number
                while remaining_crates > 0:
                    removed_crate = modified_crate_matrix_1[crate_start_index].pop()
                    modified_crate_matrix_1[crate_end_index].append(removed_crate)
                    remaining_crates -= 1

                    if remaining_crates == 0:
                        break
                
                removal_start_index = len(modified_crate_matrix_2[crate_start_index])-moving_number
                removed_multi_crates = modified_crate_matrix_2[crate_start_index][removal_start_index::]


                del modified_crate_matrix_2[crate_start_index][removal_start_index:]
                for item in removed_multi_crates:
                    modified_crate_matrix_2[crate_end_index].append(item)

# for row in modified_crate_matrix_1:
#     print(row)

result_string = ''
for row in modified_crate_matrix_1:
    result_string += row[-1]
print("part 1 answer:")
print(result_string)


# for row in modified_crate_matrix_2:
#     print(row)

result_string = ''
for row in modified_crate_matrix_2:
    if row == []:
        result_string += "_"
    else:
        result_string += row[-1]
print("part 2 answer:")
print(result_string)
