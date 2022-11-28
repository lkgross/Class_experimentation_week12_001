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


def operation2(n):
    '''Add the first n numbers.'''
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product


def timesTable():
    for i in range(1, 13):
        print(f'1 * {i} = {1 * i}')


def timesTable2():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f'{i} * {j} = {i * j}')


#  Recursion is another way to write indefinite loops
#  besides while.
#  Recursive actions invoke themselves.

def maze():
    '''Remain lost if you turn left and
    fall in a pit if you do anything else.'''
    response = 'left'
    while response == 'left':
        response = input("You are lost in a scary maze. "
                         "Will you go left or right? ")
    print("You fall in a pit. You lose.")


# Recursive functions call themselves.
def maze2():
    '''Use recursion to remain lost if you turn left and
        fall in a pit if you do anything else.'''
    # INITIALIZE the variable response
    # and subsequently update it.
    response = input("You are lost in a scary maze. "
                     "Will you go left or right? ")
    # Define a STOP condition.
    if response != 'left':
        print("You fall in a pit. You lose.")
    else:
        # Have the function CALL ITSELF.
        maze2()


# A for loop is a definite.
# Loops with while and recursion are indefinite loops.
# Functions that can be written with for can also be written with while.
# Functions that can be written with for can also be written with recursion.
# Functions that can be written with recursion can't necessarily be written with for.

def countdown_recursive(number):
    # Define a STOP condition.
    if number < 0:
        print("Blastoff!")
    else:
        print(number)
        countdown_recursive(number - 1)


# This function contains a common error!
# Put the stop condition in an if
# and then put the recursive call in an else block.
'''
def countdown_recursive2(number):
    print(number)
    countdown_recursive2(number - 1)
    # Define a STOP condition.
    if number < 0:
        print("Blastoff!")
'''

# An alternative to a stop condition is a go condition.
def countdown_recursive3(number):
    # Define a GO condition.
    if number >= 0:
        print(number)
        countdown_recursive(number - 1)
    else:
        print("Blastoff!")


# What is the error in this version?
def countdown_recursive_wrong(number):
    # Define a GO condition.
    if number >= 0:
        print(number)
        countdown_recursive_wrong(number - 1)
    print("Blastoff!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Laura')
    # loop1()
    # loop2(3)
    # loop3()
    # loop4(3, 10, 3)
    # loop5()
    # loop6()
    # print(operation1(6))
    # print(operation2(6))
    # timesTable()
    # timesTable2()
    # maze()
    # maze2()
    # countdown_recursive(10)
    # countdown_recursive2(10)
    # countdown_recursive3(10)
    countdown_recursive_wrong(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
