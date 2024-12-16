from q1s1 import lightbulb_changer
def lightbulb_solver_recursive_with_steps(lightbulb_array, target_array, index, steps):
    """
    Reference to the section that default parameters are prohibited in the function definition

    """
    # If the current state of the lightbulb array matches the target array, return the steps taken so far
    if lightbulb_array == target_array:
        return steps

    # If the index is out of bounds, return None indicating no solution found
    if index >= len(lightbulb_array):
        return None

    # Try changing the current index
    new_array = lightbulb_changer(lightbulb_array[:], index)
    steps.append(index)
    result = lightbulb_solver_recursive_with_steps(new_array, target_array, index + 1, steps)
    if result is not None:
        return result

    # Try solving without changing the current index
    steps.pop()  # Remove the last step if it didn't lead to a solution
    return lightbulb_solver_recursive_with_steps(lightbulb_array, target_array, index + 1, steps)

def lightbulb_solver_with_stpes(lightbulb_array, target_array):
    """
    This function shows the steps to solve the lightbulb problem
    """
    return lightbulb_solver_recursive_with_steps(lightbulb_array, target_array, 0, []) or [-1] #if the result is None because we cant find a solution,so [-1]




lightbulb_array = [False, False, False, False, False]
target_array = [False, False, False, False, True]
print(lightbulb_solver_with_stpes(lightbulb_array, target_array))