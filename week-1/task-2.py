string_list = "hello wor36@$^&#$#^$$^ld"
sorted_set_character = sorted(set(string_list))
key_pair = lambda y,x: {y:x}
output_list = []
for s in sorted_set_character:
    output_list.append(key_pair(s,string_list.count(s)))
print(output_list)