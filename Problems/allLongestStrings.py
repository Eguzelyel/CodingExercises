
def all_longest_strings(inputArray):
    length_dict = {}

    for i in inputArray:
        if len(i) not in length_dict:
            length_dict[len(i)] = [i]
        else:
            length_dict[len(i)].append(i)

    return length_dict[max(length_dict.keys())]

print(all_longest_strings(["aba", "aa", "ad", "vcd", "aba"]))
# Should return: ["aba", "vcd", "aba"]
