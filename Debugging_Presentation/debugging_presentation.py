# Problem 1.a identifies where the original calculation produces an incorrect
# result. Problem 1.b corrects that calculation, and Problem 2.a applies the
# same correction to the numeric section of a larger function.

# %% Problem 1.a — Identify the Error

'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake. Structure the print() statement to show what the
expected output ought to be.

1.b
Then, changing as little as possible, modify the function, using the same
general structure to output the correct answer. Call this new function
correct_add_function().
'''

def wrong_add_function(arg1, arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
        > wrong_add_function([1, 2, 3], [1, 1, 1])
        > [6, 9, 12]

    The later assignment example establishes that the intended result is
    [4, 5, 6].

    Parameters
    ----------
    arg1 : list
        List of integers.

    arg2 : list
        List of integers.

    Returns
    -------
    arg1 : list
        Elements of arg1 after the calculation is performed.
    '''

    arg1_index = 0

    # These print statements identify the location of the error and state
    # the expected result before the code is corrected in Problem 1.b.
    print("The error is in the for loop, where arg_2_sum is calculated")
    print(f"The correct answer is supposed to be: {[4, 5, 6]}")

    while arg1_index < len(arg1):
        arg_2_sum = 0

        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index] + i for i in arg2])

        arg1[arg1_index] = arg_2_sum
        arg1_index += 1

    return arg1


# Test Problem 1.a and display the incorrect result.
arg1 = [1, 2, 3]
arg2 = [1, 1, 1]

print(wrong_add_function(arg1, arg2))


# %% Problem 1.b — Correct the Calculation

def correct_add_function(arg1, arg2):
    # Start at the first element of arg1 so each value can be updated.
    arg1_index = 0

    # Continue until every element in arg1 has been processed.
    while arg1_index < len(arg1):
        arg_2_sum = 0

        # sum(arg2) already adds every value in arg2, so arg2_elements is not
        # needed in the corrected calculation.
        for arg2_elements in arg2:
            arg_2_sum = arg1[arg1_index] + sum(arg2)

        # Store the corrected value, then move to the next item.
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1

    # Return arg1 after every value has been updated.
    return arg1


# Reset the input lists because Problem 1.a changed its version of arg1.
arg1 = [1, 2, 3]
arg2 = [1, 1, 1]

print(correct_add_function(arg1, arg2))


# %% Problem 2.a — Apply the Correction to the Numeric Section

def wrong_add_function(arg1, arg2):
    

    # Use this section only when both input lists contain integers.
    if sum([type(i) == int for i in arg1]) == len(arg1) and \
       sum([type(i) == int for i in arg2]) == len(arg2):
        arg1_index = 0

        while arg1_index < len(arg1):
            arg_2_sum = 0

            # 
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index] + sum(arg2)

            # Store the corrected value, then move to the next item.
            arg1[arg1_index] = arg_2_sum
            arg1_index += 1

        return arg1

    # This original section handles lists containing only strings.
    elif sum([type(i) == str for i in arg1]) == len(arg1) and \
         sum([type(i) == str for i in arg2]) == len(arg2):

        arg1_index = 0

        while arg1_index < len(arg1):
            arg_2_sum = ''

            # This loop combines all string values in arg2.
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements

            # Add the combined string to the current value in arg1.
            arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
            arg1_index += 1

        return arg1


# Test only the corrected numeric section for Problem 2.a.
numeric_arg1 = [1, 2, 3]
numeric_arg2 = [1, 1, 1]

print(wrong_add_function(numeric_arg1, numeric_arg2))


# %%