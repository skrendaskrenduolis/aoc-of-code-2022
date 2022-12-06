processed_chars_for_packets = 0
processed_chars_for_messages = 0
letter_set = set()
with open('aoc_6_input.txt','r') as infile:
    for line in infile:
        for letters in range(len(line)-4):
            letter_set.update(list(line[letters:letters+4]))
            if len(letter_set) < 4:
                processed_chars_for_packets += 1
                letter_set.clear()
            elif len(letter_set) == 4:
                processed_chars_for_packets += 4
                break
        for letters in range(len(line)-14):
            letter_set.update(list(line[letters:letters+14]))
            if len(letter_set) < 14:
                processed_chars_for_messages += 1
                letter_set.clear()
            elif len(letter_set) == 14:
                processed_chars_for_messages+= 14
                break
    print(processed_chars_for_packets)
    print(processed_chars_for_messages)
