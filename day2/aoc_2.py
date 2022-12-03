#A, B, C -- rock, paper, scissors
#X,Y,Z -- rock, paper scissors
#rock - 1, paper - 2, scissors - 3

#Part 1
rps_scores_dict = {'X':1,
                   'Y':2,
                   'Z':3}

rps_battles_dict = {('A','X'):3,
                    ('B','X'):0,
                    ('C','X'):6,
                    ('A','Y'):6,
                    ('B','Y'):3,
                    ('C','Y'):0,
                    ('A','Z'):0,
                    ('B','Z'):6,
                    ('C','Z'):3}

total_score = 0
with open('aoc_2_input.txt', 'r') as infile:
    for line in infile:
        line_list = line.split()
        oppoenents_choice = line_list[0]
        player_choice = line_list[1]

        battle_tuple = (oppoenents_choice, player_choice)
        total_score += (rps_battles_dict[battle_tuple]+rps_scores_dict[player_choice])
print(total_score)




#Part 2
rigged_outcomes_dict = {
    'X': {
        'A':'Z',
        'B':'X',
        'C':'Y'
    },
    'Y': {
        'A':'X',
        'B':'Y',
        'C':'Z'
    },
    'Z': {
        'A':'Y',
        'B':'Z',
        'C':'X'
    }
}
total_score = 0
with open('aoc_2_input.txt', 'r') as infile:
    for line in infile:
        line_list = line.split()
        oppoenents_choice = line_list[0]
        desired_outcome = line_list[1]
        player_choice = rigged_outcomes_dict[desired_outcome][oppoenents_choice]
        battle_tuple = (oppoenents_choice, player_choice)
        total_score += (rps_battles_dict[battle_tuple]+rps_scores_dict[player_choice])
print(total_score)