
def divide_pancakes_extended_rec(pancakes, total_size,current_sum):
    """
    The function gives pancakes to diners according to a  size and returns the maximum number of diners who can receive the specific size of pancake
    :param pancakes: list of number representing the size of each pancake
    :param total_size: number that representing the size of the total size of pancake to be distributed
    :return: number that representing the maximum number of eaters who can receive the size of pancake
    """
    if total_size == 0:
        return 0

    if len(pancakes)==0: # Base case - array is empty
        return 0

    if current_sum + sum(pancakes) < total_size:
        return 0

    first = pancakes[0]

    if first > total_size:
        return divide_pancakes_extended_rec(pancakes[1:], total_size, current_sum)

    if current_sum+first > total_size:
        return divide_pancakes_extended_rec(pancakes[1:], total_size,current_sum)

    remaining_pancakes = pancakes[1:]
    #if the first pancake is total size
    if current_sum+first == total_size:
        # one eater found moving to the remaining pancakes
        return 1 + divide_pancakes_extended_rec(remaining_pancakes, total_size,current_sum)

    # skip the current pancake (not including it in any group)
    skip_current = divide_pancakes_extended_rec(remaining_pancakes, total_size,current_sum)

    # try adding the current pancake to next pancake
    combine_current = 0
    for i in range(len(remaining_pancakes)):
        if current_sum+remaining_pancakes[i] + first > total_size:
            continue
        remaining_pancakes[i] += first # Add current pancake to next
        combine_current = max(combine_current, divide_pancakes_extended_rec(remaining_pancakes, total_size,current_sum))
        remaining_pancakes[i] -= first # Revert addition

    return max(skip_current, combine_current)

def divide_pancakes_extended(pancakes,total_size):
    return divide_pancakes_extended_rec(pancakes,total_size,0)
