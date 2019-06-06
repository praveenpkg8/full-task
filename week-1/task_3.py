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
    split_string = string_list.split()
    vowel_dict = {}
    constant_dict = {}
    for word in split_string:
        count = vowel_count(word.lower())
        vowel_dict.update(key_pair(word, count))
        constant_dict.update(key_pair(word, len(word) - count))

    return vowel_dict, constant_dict


output = get_string_values(string_list)
print(output)
