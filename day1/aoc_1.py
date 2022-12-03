# DAY 1
# part 1. Finding elf with most calories
elf_list = []
calorie_counter = 0
elf_counter = 0
with open('words.txt', 'r') as infile:
    for line in infile:
        line = line.strip()
        if line == '':
            elf_counter += 1
            elf_list.append((elf_counter, calorie_counter))
            calorie_counter = 0
        else:
            calorie_counter += int(line)

    elf_counter += 1
    elf_list.append((elf_counter, calorie_counter))
    calorie_counter = 0

sorted_elf_list_by_cals = sorted(
    elf_list, key=lambda item: item[1], reverse=True)
print(f"Elf with most calories: {sorted_elf_list_by_cals[0][0]}")
print(f"Number of calories on elf: {sorted_elf_list_by_cals[0][1]}")

# part 2. total calories of top 3 elves
top_three_cal_total = 0
for elf, calories in sorted_elf_list_by_cals[:3]:
    top_three_cal_total += calories
print(f"Sum of calories of top 3 calory holding elves: {top_three_cal_total}")
