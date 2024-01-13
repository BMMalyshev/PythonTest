while True:
    start = int(input('Enter start index: '))
    end = int(input('Enter end index: '))
    OutVal = ' '

    if (start == 0 or end == 0):
        break

    for num in range(start, end + 1):
        OutVal = num * 2
        print(OutVal)