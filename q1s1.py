def lightbulb_changer(lightbulb_array, index):
    """
    this function changes the lightbulb switch from on to off (True to False) and vice versa
    :param lightbulb_array:  the array of lightbulbs
    :param index:  the index we want to change
    :return:  the array after changing the switchs
    """
    if index == 0:  # if this is the first index we can just change the exact bulb and the one next to it
        lightbulb_array[0] = not lightbulb_array[0]
        if len(lightbulb_array) > 1:
            lightbulb_array[1] = not lightbulb_array[1]
    elif index == len(lightbulb_array) - 1:  # if this is the last index we can just change the exact bulb and the one before it
        lightbulb_array[-1] = not lightbulb_array[-1]
        if len(lightbulb_array) > 1:
            lightbulb_array[-2] = not lightbulb_array[-2]
    else:  # change the exact bulb and the one before and after it
        lightbulb_array[index] = not lightbulb_array[index]
        lightbulb_array[index - 1] = not lightbulb_array[index - 1]
        lightbulb_array[index + 1] = not lightbulb_array[index + 1]
    return lightbulb_array
def lightbulb_solver_recursive(lightbulb_array, target_array, index):
        """
         this function is to solve the lightbulb problem recursively
        :param lightbulb_array: the array we have
        :param target_array: the array we want to reach
        :param index: the index of the lightbulb array
        :return: the result of the lightbulb problem
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
    this function is to solve the lightbulb problem
    :param lightbulb_array: the array we have
    :param target_array: the array we want to reach
    :return: the result of the lightbulb problem (True or False)
    """
    return lightbulb_solver_recursive(lightbulb_array, target_array, 0)


