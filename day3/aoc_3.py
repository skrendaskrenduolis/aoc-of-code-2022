priority_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
sum_of_priorities = 0
with open('aoc_3_input.txt', 'r') as infile:
    for line in infile:
        line = line.strip()

        for i in range(0, len(line)//2):
            for j in range(len(line)//2, len(line)):
                if line[i] == line[j]:
                    duplicate_letter = line[i]
                    break

        sum_of_priorities += (priority_string.index(duplicate_letter)+1)

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
