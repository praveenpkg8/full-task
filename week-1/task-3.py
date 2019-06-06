string_list = "hello woRLd"
VOWELS = list("aeiou")
key_pair = lambda y, x: {y: x}


def vowel_count(word):
    count = 0
    for s in word:
        if s in VOWELS:
            count += 1
    return count


def get_string_values(string_list):
    splited_string = string_list.split()
    vowel_list = []
    constant_list = []
    for word in splited_string:
        count = vowel_count(word.lower())
        vowel_list.append(key_pair(word, count))
        constant_list.append(key_pair(word, len(word) - count))

    return vowel_list, constant_list


output = get_string_values(string_list)
print(output)



