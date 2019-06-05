orginal_list = [1, 2, 3, 4, 5, 6, 7]


def add_tuple(*x):
    return x


def generate_tuple_pair(o_list):
    output = []
    left = 0
    right = len(o_list) - 1
    for x in range(len(o_list) // 2):
        output.append(add_tuple(o_list[left], o_list[right]))
        left += 1
        right -= 1

    if len(o_list) % 2 != 0:
        output.append(add_tuple(o_list[len(o_list) // 2]))

    return output


output_list = generate_tuple_pair(orginal_list)
print(output_list)
