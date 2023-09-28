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
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
rows = [row1, row2, row3]


def display_rows():
    print("\n")
    print(row1)
    print(row2)
    print(row3)


# User Controller
user_turn = True
user_turn_count = 0

# User Selection Controller
user_selection_row = None
user_selection_column = None


# Input Validation 1: None || String
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
        return user_selection


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


# Validation Fn (str):Boolean
def validate_input(user_input):
    validated_input = input_validation(user_input)
    if validated_input != None:
        return validated_input
    else:
        return None


# Check first validation : Boolean
def first_validation():
    # Ask for row and col
    user_selection_row = input("Pick a row between 0,1,2 : ")
    # Validate the input
    return validate_input(user_selection_row)


# Second stage
def second_validation(passed_first):
    if passed_first == None:
        return False

    user_selection_col = input(
        f"\nYou have picked row {passed_first}, \nPick a column between 0,1,2 : "
    )
    # Input validation: See if the input is empty string
    return validate_input(user_selection_col)


# Controller
while user_turn_count < 10:
    print(f"\nCurrent turn: {user_turn_count}")
    print(f"User {user_turn}'s turn")

    passed_first = first_validation()
    passed_second = second_validation(passed_first)

    # # Ask for row and col
    # user_selection_row = input("Pick a row between 0,1,2 : ")
    # # Input validation: See if the input is empty string
    # validated_input_row = input_validation(user_selection_row)
    # # If Else for input
    # if validated_input_row != None:
    #     user_selection_col = input(
    #         f"\nYou have picked row {user_selection_row}, \nPick a column between 0,1,2 : "
    #     )
    #     # Input validation: See if the input is empty string
    #     validated_input_col = input_validation(user_selection_col)
    #     if validated_input_col != None:
    #         # Log it to the rows
    #         loggable = log_user_input(
    #             user_turn, int(validated_input_row), int(validated_input_col)
    #         )
    #         if loggable == True:
    #             # Increase user count
    #             user_turn_count += 1
    #             # Change the turn
    #             user_turn = not user_turn
    #             display_rows()
    #         else:
    #             pass
    # else:
    #     pass
