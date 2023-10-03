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
WON_SEQUENCE = ["OOO", "XXX"]

# State Management
game_state = {
    "rows": {"row0": [" ", " ", " "], "row1": [" ", " ", " "], "row2": [" ", " ", " "]},
    "game_finished": False,
    "user_turn": True,
    "user_turn_count": 0,
}

# rows
# row0 = [" ", " ", " "]
# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
rows = [game_state.rows.row0, game_state.row.row1, game_state.row.row2]
# this doesnt work


# User Controller
game_finished = False
user_turn = True
user_turn_count = 0


class Helpers:
    def get_user_name(self):
        global user_turn
        if user_turn == True:
            return "O"
        else:
            return "X"


class InputController:
    def __init__(
        self,
        message,
    ):
        self.message = message

    def validation(self, user_selection):
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

    def get_input(self):
        user_selection = input(self.message)
        result = self.validation(user_selection)

        if result != None:
            return result
        else:
            return None

    def get_user_name(self):
        global user_turn
        if user_turn == True:
            return "O"
        else:
            return "X"


class GameLogic:
    def __init__(self, user_turn, row, column):
        self.user_turn = user_turn
        self.row = row
        self.column = column

    def log_user_input(self):
        # Guard
        if game_state.rows[self.row][self.column] != " ":
            print("\n### Unavailable. The column is already taken ###")
            return False
        # Based on User turn,
        if self.user_turn == True:
            game_state.rows[self.row][self.column] = "O"
        else:
            game_state.rows[self.row][self.column] = "X"
        return True

    def check_won(self):
        global game_finished
        # Horizontal
        for row in rows:
            joined_row = "".join(row)

            if joined_row in WON_SEQUENCE:
                game_finished = True
                break
        pass

        # Vertical
        i = 0
        while i < 3:
            joined_row = row0[i] + row1[i] + row2[i]

            i += 1
            if joined_row in WON_SEQUENCE:
                game_finished = True
                break

        # Diagonal
        sequence_1 = row0[0] + row1[1] + row2[2]
        sequence_2 = row0[2] + row1[1] + row2[0]
        if sequence_1 in WON_SEQUENCE or sequence_2 in WON_SEQUENCE:
            game_finished = True
        return game_finished

    def display_rows(self):
        print("\n")
        print(game_state.rows.row0)
        print(game_state.rows.row1)
        print(game_state.rows.row2)

    def increase_user_turn_count(self):
        global user_turn_count
        user_turn_count += 1

    def switch_user_turn(self):
        global user_turn
        user_turn = not user_turn


# Controller
while user_turn_count < 10:
    print(f"\nCurrent turn: {user_turn_count}")

    input_controller = InputController("Pick a row between 0,1,2 : ")
    print(f"User {Helpers().get_user_name()}'s turn")

    # Validate first input
    passed_first = input_controller.get_input()

    # Validate second input IF first validation succesful
    passed_second = None
    if passed_first != None:
        passed_second = InputController(
            f"\nYou have picked row {passed_first}, \nPick a column between 0,1,2 : "
        ).get_input()
    else:
        pass

    # All pased. Log the result, change turn, and add turn count
    if passed_first != None and passed_second != None:
        # Log result
        # loggable = log_user_input(user_turn, passed_first, passed_second)
        game_logic = GameLogic(user_turn, passed_first, passed_second)
        is_loggable = game_logic.log_user_input()

        if is_loggable != False:
            # Display the row
            game_logic.display_rows()

            # Check if won
            if game_logic.check_won() == True:
                # If won, break out
                print("\n")
                print(f"GAME OVER. PLAYER {Helpers().get_user_name()} WON")
                break

            # Increase turn count
            game_logic.increase_user_turn_count()

            # Change turn
            game_logic.switch_user_turn()

    # First validation failed
    else:
        pass
