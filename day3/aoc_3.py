priority_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
sum_of_priorities = 0
with open('aoc_3_input.txt', 'r') as infile:
    for line in infile:
        line = line.strip()

        for letter in line[:len(line)//2]:
            if letter in line[len(line)//2:]:
                sum_of_priorities += priority_string.index(letter)+1
                break
    print(sum_of_priorities)


# Part 2
sum_of_priorities = 0
triple_set_list = []
with open('aoc_3_input.txt', 'r') as infile:
    for line in infile:
        triple_set_list.append(set(line.strip()))

        if len(triple_set_list) == 3:
            result = ''.join(triple_set_list[0].intersection(
                triple_set_list[1], triple_set_list[2]))
            sum_of_priorities += (priority_string.index(result)+1)
            triple_set_list.clear()
    print(sum_of_priorities)
