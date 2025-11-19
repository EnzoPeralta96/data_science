from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# la entrada se lee desde la entrada estandar
for line in sys.stdin:
    line = line.strip()

    # parse the input from mapper.py
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError as e:
        continue

    # TODO
    if current_word is None:
        current_word = word
        current_count = count
    else:
        if current_word == word:
            current_count += count
        else:
            print('{}\t{}'.format(current_word, current_count))
            current_word = word
            current_count = count

if current_word == word:
    print('{}\t{}'.format(current_word, current_count))

