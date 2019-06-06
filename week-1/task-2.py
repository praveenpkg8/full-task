string_list = "hello wor36@$^&#$#^$$^ld"
sorted_set_character = sorted(set(string_list))
key_pair = lambda y, x: {y: x}
output_dict = {}
for s in sorted_set_character:
    output_dict.update(key_pair(s, string_list.count(s)))
print(output_dict)
