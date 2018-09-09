def get_number(s):
    n = '0'
    i = 0
    for c in s:
        i += 1
        if c != '.':
            n += c
        else:
            break
    return [int(n), i]


def compareVersion(version1, version2):
    n_index = [[0, 0], [0, 0]]
    v1_len = len(version1)
    v2_len = len(version2)
    i1 = 0
    i2 = 0

    while i1 < v1_len or i2 < v2_len:
        n_index[0] = get_number(version1[i1:])
        n_index[1] = get_number(version2[i2:])
        if n_index[0][0] > n_index[1][0]:
            return 1
        elif n_index[0][0] < n_index[1][0]:
            return -1
        i1 += n_index[0][1]
        i2 += n_index[1][1]

    return 0


print("Result is: %d" % compareVersion("7.5.2.4", "7.5.3"))

