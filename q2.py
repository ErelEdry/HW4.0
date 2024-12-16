def divide_pancakes_extended(pancakes, total_size):
    """
    The function distributes pancakes to diners according to a certain size and returns the maximum number of diners who can receive the particular size of pancake
    :param pancakes: list of number representing the size of each pancake
    :param total_size: number that representing the size of the total size of pancake to be distributed
    :return: integer representing the maximum number of diners who can receive the particular size of pancake
    """
    if len(pancakes)==0: # Base case - array is empty
        return 0
    first = pancakes[0]
    remaining_pancakes = pancakes[1:]
    #if the first pancake is total size
    if first == total_size:
        # one eater found moving to the remaining pancakes
        return 1 + divide_pancakes_extended(remaining_pancakes, total_size)

    # skip the current pancake (not including it in any group)
    skip_current = divide_pancakes_extended(remaining_pancakes, total_size)

    # try adding the current pancake to next pancake
    combine_current = 0
    for i in range(len(remaining_pancakes)):
        remaining_pancakes[i] += first
        combine_current = max(combine_current, divide_pancakes_extended(remaining_pancakes, total_size))
        remaining_pancakes[i] -= first

    return max(skip_current, combine_current)


pancakes = [1,3,1,1,5,1,6,7,8]
total_size = 5
print(divide_pancakes_extended(pancakes, total_size))
