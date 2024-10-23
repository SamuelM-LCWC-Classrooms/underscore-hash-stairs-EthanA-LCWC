def staircase(number):
    all_stairs = ""
    if number > 0:
        for i in range(1, number + 1):
            stair = ""
            for j in range(1, number + 1):
                if i >= j:
                    stair = stair + "#"
                else:
                    stair = "_" + stair
            all_stairs += stair
            if not i == number:
                all_stairs += "\n"
    if number < 0:
        number = number - number - number
        print(number)
        for i in range(1, number + 1):
            stair = ""
            for j in range(1, number + 1):
                if i <= j:
                    stair = stair + "#"
                else:
                    stair = "_" + stair
            all_stairs += stair
            if not i == number:
                all_stairs += "\n"
    return all_stairs
