def evaluation():
    us_input = list(input('Введите римское число:\n'))
    print(us_input)
    c = 0
    for _ in us_input:
        if _ == 'I':
            us_input[c] = 1
        elif _ == 'V':
            us_input[c] = 5
        elif _ == 'X':
            us_input[c] = 10
        elif _ == 'L':
            us_input[c] = 50
        elif _ == 'C':
            us_input[c] = 100
        elif _ == 'D':
            us_input[c] = 500
        elif _ == 'M':
            us_input[c] = 1000
        c += 1
    print(us_input)
    len_numbers = len(us_input)
    c_w = 2
    result = 0
    if us_input[0] < us_input[1]:
        if us_input[0] == 1 or us_input[0] == 10 or us_input[0] == 100 or us_input[0] == 1000:
            result = us_input[1] - us_input[0]
    else:
        result = us_input[0] + us_input[1]
    while c_w < len_numbers:
        result = result + us_input[c_w]
        c_w += 1
    print(result)


if __name__ == '__main__':
    evaluation()
