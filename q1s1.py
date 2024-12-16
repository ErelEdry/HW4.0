
def lightbulb_changer(lightbulb_array, index):
    """
    This function changes the state of the lightbulb at the given index and the two adjacent lightbulbs
    """
    if index == 0:  # if this is the first index we can just change the exact bulb and the one next to it
        lightbulb_array[0] = not lightbulb_array[0]
        lightbulb_array[1] = not lightbulb_array[1]
    elif index == len(lightbulb_array) - 1:  # if this is the last index we can just change the exact bulb and the one before it
        lightbulb_array[-1] = not lightbulb_array[-1]
        lightbulb_array[-2] = not lightbulb_array[-2]
    else:  # change the exact bulb and the one before and after it
        lightbulb_array[index] = not lightbulb_array[index]
        lightbulb_array[index - 1] = not lightbulb_array[index - 1]
        lightbulb_array[index + 1] = not lightbulb_array[index + 1]
    return lightbulb_array
def lightbulb_solver_recursive(lightbulb_array, target_array, index):
        """
        Reference to the section that default parameters are prohibited in the function definition
        """
        if lightbulb_array == target_array:
            return True
        if index >= len(lightbulb_array):
            return False

        # Try changing the switch the current index
        new_array = lightbulb_changer(lightbulb_array[:], index)#doing shallow copy to keep the original array
        if lightbulb_solver_recursive(new_array, target_array, index + 1):
            return True

        # Try solving without changing the current index switch
        if lightbulb_solver_recursive(lightbulb_array, target_array, index + 1):
            return True

        return False

def lightbulb_solver(lightbulb_array, target_array):
    """
    This function solves the lightbulb problem using recursion
    """
    return lightbulb_solver_recursive(lightbulb_array, target_array, 0)

lightbulb_array=[False, True, False ,True]
target_array=[True, True, False ,False]
print(lightbulb_solver(lightbulb_array, target_array))