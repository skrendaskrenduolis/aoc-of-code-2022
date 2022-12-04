import re
section_search = None
full_overlap_pair_counter = 0
partial_overlap_pair_counter = 0
with open('aoc_4_input.txt', 'r') as infile:
    for line in infile:
        section_search = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line)
        if section_search is not None:
            section_range_1 = tuple(map(int, (section_search.group(1), section_search.group(2))))
            section_range_2 = tuple(map(int, (section_search.group(3), section_search.group(4))))

            if section_range_1[0] <= section_range_2[0] and section_range_1[1] >= section_range_2[1]:
                full_overlap_pair_counter += 1
            elif section_range_1[0] >= section_range_2[0] and section_range_1[1] <= section_range_2[1]:
                full_overlap_pair_counter += 1
                

            elif section_range_1[1] >= section_range_2[0] and section_range_1[0] <= section_range_2[1]:
                partial_overlap_pair_counter += 1
            elif section_range_2[1] >= section_range_1[0] and section_range_2[0] <= section_range_1[1]:
                partial_overlap_pair_counter += 1
            

    print(full_overlap_pair_counter)
    print(partial_overlap_pair_counter + full_overlap_pair_counter)
