array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def huichange(array):
    start_r = 0
    start_c = 0
    end_r = len(array) - 1
    end_c = len(array[0]) - 1

    while (start_r < end_r):
        change(array, start_r, start_c, end_r, end_c)

        start_c += 1
        start_r += 1
        end_r -= 1
        end_c -= 1


def change(array, start_r, start_c, end_r, end_c):
    for i in range(end_c - start_c):


        a = array[start_r][start_c + i]

        b = array[start_r + i][end_c]

        c = array[end_r][end_c - i]

        d = array[end_r - i][start_r]

        print(a, b,c,d)


        array[start_r][start_c + i] = d

        array[start_r + i][end_c] = a

        array[end_r][end_c - i] = b

        array[end_r - i][start_r] = c


huichange(array)
print(array)