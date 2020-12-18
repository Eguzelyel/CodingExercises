def common_character_count(s1, s2):
    s1_dct = {}
    s2_dct = {}

    for i in s1:
        if i not in s1_dct:
            s1_dct[i]=1
        else:
            s1_dct[i]+=1

    for i in s2:
        if i not in s2_dct:
            s2_dct[i]=1
        else:
            s2_dct[i]+=1

    res = 0
    for key, val in s2_dct.items():
        if key in s1_dct:
            res += min(s1_dct[key], s2_dct[key])

    return res


print(common_character_count("aabcc", "accde"))
