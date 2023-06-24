import sys


def add_word_to_trie(trie, word):
    current_node = trie
    for char in word:
        if char not in current_node:
            current_node[char] = {}
        current_node = current_node[char]
    current_node['is_end'] = True


def count_prefixes(trie, word):
    count = 0
    current_node = trie
    for char in word:
        current_node = current_node[char]
        if len(current_node) > 1 or 'is_end' in current_node:
            count += 1
    return count


while True:
    main_trie = {}
    word_list = []

    try:
        num_of_words = int(sys.stdin.readline())
    except:
        break
    for _ in range(num_of_words):
        word = sys.stdin.readline().strip()
        add_word_to_trie(main_trie, word)
        word_list.append(word)

    total_prefixes = 0
    for word in word_list:
        total_prefixes += count_prefixes(main_trie, word)

    print(f"{total_prefixes / num_of_words:.2f}")
