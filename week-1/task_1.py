orginal_list = [1, 2, 3, 4, 5, 6, 7]


def add_tuple(**x):
    return x


add_tuple = lambda *y: y


def generate_tuple_pair(o_list):
    output = []
    lam_check = []
    left = 0
    right = len(o_list) - 1
    for x in range(len(o_list) // 2):
        output.append(add_tuple(a=o_list[left], b=o_list[right]))
        left += 1
        right -= 1

    if len(o_list) % 2 != 0:
        output.append(add_tuple(a=o_list[len(o_list) // 2]))

    return lam_check


output_list = generate_tuple_pair(orginal_list)
print(output_list)
