forest_matrix = []
visible_tree_counter = 0

#part 1
with open('/home/marty/aoc_2022/day8/aoc_8_input.txt', 'r') as infile:
    for line in infile:
        forest_matrix.append(list(map(int, list(line.strip()))))

for row_index, row in enumerate(forest_matrix):
    if row_index == 0 or row_index == len(forest_matrix) - 1:
        visible_tree_counter += len(row)
        continue

    for item_index, item in enumerate(row):
        not_visible_x_left, not_visible_x_right, not_visible_y_top, not_visible_y_bottom = False, False, False, False
        if item_index == 0 or item_index == len(row)-1:
            visible_tree_counter += 1

        else:
            for row_index_2, row_2 in enumerate(forest_matrix):
                if row_index == row_index_2:
                    continue
                if row_2[item_index] >= row[item_index]:
                    if row_index_2 < row_index:
                        not_visible_y_top = True
                    elif row_index_2 > row_index:
                        not_visible_y_bottom = True
                    
            
            for item_index_2, item_2 in enumerate(row):
                if item_index == item_index_2:
                    continue
                if  item_2 >= item:
                    if item_index_2 < item_index:
                        not_visible_x_left = True
                    elif item_index_2 > item_index:
                        not_visible_x_right = True
        
                
            if not_visible_x_left and not_visible_x_right and not_visible_y_bottom and not_visible_y_top:
                continue
            else:
                visible_tree_counter += 1

print(visible_tree_counter)



#part 2
top_scenic_score = None
for row_index, row in enumerate(forest_matrix):

    for item_index, item in enumerate(row):
        scenic_score_left, scenic_score_right, scenic_score_up, scenic_score_down = 0, 0, 0, 0

        for row_index_2, row_2 in reversed(list(enumerate(forest_matrix))):
            if row_index == 0:
                break
            if row_index_2 >= row_index:
                continue
            else:
                scenic_score_up += 1
                if row_2[item_index] >= row[item_index]:
                    break
        
        for row_index_2, row_2 in enumerate(forest_matrix):
            if row_index == len(forest_matrix)-1:
                break
            if row_index_2 <= row_index:
                continue
            else:
                scenic_score_down += 1
                if row_2[item_index] >= row[item_index]:
                    break


        for item_index_2, item_2 in reversed(list(enumerate(row))):
            if item_index == 0:
                break
            if item_index_2 >= item_index:
                continue
            else:
                scenic_score_left += 1
                if item_2 >= item:
                    break

        for item_index_2, item_2 in enumerate(row):
            if item_index == len(row)-1:
                break
            if item_index_2 <= item_index:
                continue
            else:
                scenic_score_right += 1
                if item_2 >= item:
                    break     

        temp_scenic_score = scenic_score_up * scenic_score_down * scenic_score_left * scenic_score_right
        if top_scenic_score is None or top_scenic_score < temp_scenic_score:
            top_scenic_score = temp_scenic_score

print(top_scenic_score)

            

