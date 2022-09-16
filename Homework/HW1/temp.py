# initialize trackers
cur_word = None
cur_count = 0

# read input key-value pairs from standard input
for line in sys.stdin:
    word, count  = line.split()
    # tally counts from current key
    if word == cur_word: 
        cur_count += int(count)
    elif cur_word is None:
        cur_word = word
        cur_count += int(count)
    # OR emit current total and start a new tally 
    else: 
        if cur_word:
            print(f'{cur_word}\t{cur_count}')
        cur_word, cur_count  = word, int(count)

# don't forget the last record! 
print(f'{cur_word}\t{cur_count}')