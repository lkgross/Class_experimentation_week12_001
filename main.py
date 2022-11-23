# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    '''Print Hi, name, where name is the parameter.'''
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def loop1():
    '''Use a standard for loop with range(10).'''
    for i in range(10):
        print(i)


def loop2(starting_loop_variable_value):
    '''Use a parameter for the starting value of a loop.'''
    for i in range(starting_loop_variable_value, 10):
        print(i)


def loop3():
    '''Call range with three arguments: 1, 10, and 2.'''
    for i in range(1, 10, 2):
        print(i)


def loop4(starting_value, ending_upper_bound, step_size):
    '''Call range with parameters for the starting value, the upper
    bound on the sequence, and the step size.'''
    for i in range(starting_value, ending_upper_bound, step_size):
        print(i)


def loop5():
    '''Print when you encounter an 'e' in 'excellent'. Count up the
    letters 'e'.'''
    counter = 0
    for i in range(9):
        if "excellent"[i] == "e":
            print("\nThere is an 'e' in 'excellent'.")
            # counter = counter + 1
            # Alternate syntax:
            counter += 1
            print(f"There are {counter} letters 'e' in excellent.")


def loop6():
    '''Loop through a string, one character at a time.'''
    for c in "excellent":
        print(c)


def operation1(n):
    '''Add the first n numbers.'''
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum

def timesTable():
    for i in range(1, 13):
        print(f'1 * {i} = {1*i}')

def timesTable2():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f'{i} * {j} = {i * j}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Laura')
    # loop1()
    # loop2(2)
    # loop3()
    # loop4(1, 10, 2)
    # loop5()
    # loop6()
    # print(operation1(6))
    timesTable2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
