# my_dogs = "aang aaang"

# print(my_dogs)

# print(type(my_dogs))

# print(my_dogs[0])

# print(len(my_dogs))

# Sames as <string>.slice();
# print(my_dogs[2:])
# print(my_dogs[2:7])

# Strings are immutable
# name = "please God"

# numbaa = 0
# print(numbaa)
# numbaa = 1
# print(numbaa)

# String concat
# print(name + 'p')
# print(name.upper())
# print(name.capitalize())
# print(name.split("l"))

# String Interpolation
# print('this is a string {}'.format('aaang'))
# print('The {2} {0} {1}'.format('fox', 'brown', 'quick'))
# print('the {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
# result = 100/77
# print('the result was {r:1.3f}'.format(r=result))
# print(f'hello, his name is {name}')
# my_list = ["1", "0", "2"]
# print(my_list[0])
# another_list = ["3", "4"]
# another_list[1] = "5"
# print(my_list + another_list)
# new_list = my_list + another_list
# print(new_list)
# new_list.append("six")
# new_list.pop(0)
# print(new_list)
# new_list.sort()
# print(new_list)
# print(type(new_list))

# Dictionary (Object)
# my_dick = {"size": "big", "length": "long", "used_by": ["minseo", "Lindsey", "Yoonjeong", "Kerry", "YeWeon"]}
# print(my_dick["used_by"][2].upper())
# my_dick["watned_by"] = "Yoonjeong"
# print(my_dick["watned_by"])

# Tuples
# t = (1, 2, 3)
# print(t[2])
# print(t.count("a"))

# Sets
# myset = set()
# myset.add(1)
# print(myset)
# myset.add(2)
# myset.add(2)
# print(myset)

# Bool
# print(1 == "1")
# if 1 == 1 or not 2 == 1:
#     print("true")
# else:
#     print("wrong")

# my_iterable = [1, 2, 3]

# for item in my_iterable:
# print(f"fuck Yoonjeong {item} times")
# for num in my_iterable:
#     if num % 2 == 0:
#         print(num)

# tup_arr = [(1, 2), (3, 4)]
# for a, b in tup_arr:
#     print(a + b)

# d = {"k1": 1, "k2": 2}

# for value in d.keys():
#     print(value)

# x = 0
# while x < 5:
#     print(x)
#     x += 1
# else:
#     print("aaang")

# print("y" in "yoonjeong")
# print(int("30"))
# mylist = [num**2 for num in range(0, 11)]
# mylist = [x for x in range(0, 11) if x > 5]
# results = [x if x % 2 == 0 else "odd" for x in range(0, 11)]
# print(results)

# Array methods
# mylist = [1, 2, 3, 4]
# mylist.insert(0, 0)
# print(mylist)


# def name_function(name):

#     return name


# print(name_function("shit"))


# def checkcheck(a, b):
#     if a > b:
#         print("a is bigger")
#     elif b > a:
#         print("b is bigger")
#     else:
#         print("they same")


# checkcheck(5, 1)


# def square(num):
# return num**2


# my_nums = [1, 2, 3, 4, 5]


# for el in map(square, my_nums):
# print(el)

# print(list(map(square, my_nums)))


# lexical_name = 1


# def lexcal_function():
#     print("first level")
#     print(lexical_name)
#     lexical_name = 2

#     def lexical_function2():
#         print("second level")
#         print(lexical_name)

#     lexical_function2()


# lexcal_function()

# test_list = [1, 2, 3, 4, 5]
# for el in test_list:
# print(el)
# x = 20


# def func():
#     print(x)


# func()

# user_input1 = input("aanag : ")

# print(user_input1)


# Tik Tak Toe

# rows
row0 = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
rows = [row0, row1, row2]


# User Controller
game_finished = False
user_turn = True
user_turn_count = 0

# User Selection Controller
user_selection_row = None
user_selection_column = None


def get_user_name(user_turn):
    if user_turn == True:
        return "O"
    else:
        return "X"


# Input Validation 1: None || Number
def input_validation(user_selection):
    if (
        user_selection.isdigit() == False
        or user_selection == ""
        or user_selection == None
        or int(user_selection) >= 3
    ):
        print("\nWrong input. Must be a number and less than 3")
        return None
    else:
        return int(user_selection)


# Validation Fn (str):Boolean
def get_input(message):
    user_input = input(message)
    validated_input = input_validation(user_input)
    if validated_input != None:
        return validated_input
    else:
        return None


# Log machine
def log_user_input(user_turn, row, column):
    # Guard
    if rows[row][column] != " ":
        print("\n### Unavailable. The column is already taken ###")
        return False
    # Based on User turn,
    if user_turn == True:
        rows[row][column] = "O"
    else:
        rows[row][column] = "X"
    return True


# Displays rows
def display_rows():
    print("\n")
    print(row0)
    print(row1)
    print(row2)


# Check if won
def check_won(game_finished):
    if user_turn_count == 0:
        pass

    # Horizontal
    won_sequence = ["OOO", "XXX"]
    for row in rows:
        joined_row = "".join(row)

        if joined_row in won_sequence:
            game_finished = True
            break

    # Vertical
    i = 0
    while i < 3:
        joined_row = row0[i] + row1[i] + row2[i]

        i += 1
        if joined_row in won_sequence:
            game_finished = True
            break

    # Diagonal
    sequence_1 = row0[0] + row1[1] + row2[2]
    sequence_2 = row0[2] + row1[1] + row2[0]
    if sequence_1 in won_sequence or sequence_2 in won_sequence:
        game_finished = True
    return game_finished


# Controller
while user_turn_count < 10:
    print(f"\nCurrent turn: {user_turn_count}")

    print(f"User {get_user_name(user_turn)}'s turn")

    passed_first = get_input("Pick a row between 0,1,2 : ")
    passed_second = None
    if passed_first != None:
        passed_second = get_input(
            f"\nYou have picked row {passed_first}, \nPick a column between 0,1,2 : "
        )

    # All pased. Log the result, change turn, and add turn count
    if passed_first != None and passed_second != None:
        # Log result
        loggable = log_user_input(user_turn, passed_first, passed_second)

        if loggable != False:
            # Display the row
            display_rows()

            # Check if won
            if check_won(game_finished) == True:
                # If won, break out
                print("\n")
                print(f"GAME OVER. PLAYER {get_user_name(user_turn)} WON")
                break

            # Increase turn count
            user_turn_count += 1
            # Change turn
            user_turn = not user_turn
    # First validation failed
    else:
        pass
