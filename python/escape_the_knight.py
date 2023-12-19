from pprint import pprint
import random

"""
Background
Consider a 8-by-8 chessboard containing only a knight and a king. The knight wants to check the king. The king wants to avoid this. The knight has a cloaking shield, so it moves invisibly. Help the king escape the knight!

Task
You are given the initial king position, initial knight position, and the number of moves n that the titanic struggle will last. Return a list (or array) of length n containing the king's moves. The first move must be a legal king move from the initial king position, and each subsequent move must be a legal king move from the king's previous position. Your goal is for the king to make all the moves in sequence without ever getting checked by the knight, no matter which moves the knight makes.

Details
(1) Squares on the chessboard are specified as strings giving the horizontal coordinate first (a letter from a to h), followed by the vertical coordinate (a number from 1 to 8). Example: On the board below, the knight N is on "d4" and the king K is on "g7".

(2) The king moves one square in any direction. For example, the king on g7 can move to any of the following squares: f8, f7, f6, g8, g6, h8, h7, h6, as shown below.

(3) The knight moves one square horizontally and two squares vertically, or two squares horizontally and one square vertically. For example, the knight on d4 can move to any of the following squares: b3, c2, e2, f3, f5, e6, c6, b5, as shown below.

(4) The knight and king move simultaneously. The knight wins if it ever checks the king (or if the king moves illegally). The king (and you) win if it survives the specified number of moves without ever being checked.

Example
Given input ("g7", "d4", 6), suppose your function returns ["f8", "e7", "f6", "e7", "d7", "d6"] as the king's moves. If the knight happened to move ["c6", "e5", "g4, "f2", "d1", "e3"], then the knight wins, because after move 3 the knight at g4 checks the king at f6.

Things to Note
(1) The number of moves n satisfies 1 <= n <= 50.

(2) The initial position of the king is always a different square from the initial position of the knight.

(3) It's possible that the knight could be checking the king in the initial position. This is ignored. It's also possible that the same position could occur three times in succession. This is also ignored. (In regular chess this allows a draw to be declared.)

(4) In order to make sure that it never moves to the same square as the king, the knight can access the move-list returned by your function. This means it can use this information when picking its move. (We didn't say this was a fair fight!)
"""

# board = [["." for y in range(8)] for x in range(8)]


def create_board():
    a = []
    n = ["8", "7", "6", "5", "4", "3", "2", "1"]
    l = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for x in range(8):
        row = []
        for y in range(8):
            row.append(l[y] + n[x])
        a.append(row)
    return a


def create_squares():
    squares = {}
    n = ["8", "7", "6", "5", "4", "3", "2", "1"]
    l = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for i in range(8):
        for j in range(8):
            squares[l[i] + n[j]] = [j, i]

    return squares

    return squares


def create_square_colors():
    squares = {}
    n = ["8", "7", "6", "5", "4", "3", "2", "1"]
    l = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for i in range(8):
        for j in range(8):
            if int(n[i]) % 2 == 0:
                if int(n[j]) % 2 == 0:
                    squares[l[i] + n[j]] = "w"
                else:
                    squares[l[i] + n[j]] = "b"
            else:
                if int(n[j]) % 2 == 0:
                    squares[l[i] + n[j]] = "b"
                else:
                    squares[l[i] + n[j]] = "w"

    return squares


board = create_board()
squares = create_squares()
square_colors = create_square_colors()


# pprint(square_colors)


def convert_to_square_coord(coord):
    return list(squares.keys())[list(squares.values()).index(coord)]


def get_square_color(square):
    return square_colors[square]


# pprint(get_square_color("g3"))

king_moves = {
    "left_up": [-1, -1],
    "middle_up": [-1, 0],
    "right_up": [-1, 1],
    "left": [0, -1],
    "right": [0, 1],
    "left_down": [1, -1],
    "middle_down": [1, 0],
    "right_down": [1, 1],
}

knight_moves = {
    "ten": [-1, -2],
    "eleven": [-2, -1],
    "one": [-2, 1],
    "two": [-1, 2],
    "four": [1, 2],
    "five": [2, 1],
    "seven": [2, -1],
    "eight": [1, -2],
}


def king_legal_moves(king_square):
    legal_moves = []
    curr_coords = squares[king_square]

    for move in king_moves:
        x = curr_coords[0] + king_moves[move][0]
        y = curr_coords[1] + king_moves[move][1]

        if x > 7 or x < 0 or y > 7 or y < 0:
            continue

        coord = [x, y]
        square = convert_to_square_coord(coord)

        legal_moves.append(square)

    return legal_moves


def knight_legal_moves(knight_square):
    legal_moves = []
    curr_coords = squares[knight_square]

    for move in knight_moves:
        x = curr_coords[0] + knight_moves[move][0]
        y = curr_coords[1] + knight_moves[move][1]

        if x > 7 or x < 0 or y > 7 or y < 0:
            continue

        coord = [x, y]
        square = convert_to_square_coord(coord)

        legal_moves.append(square)

    return legal_moves


def two_moves_ahead(knight_square):
    first_moves = knight_legal_moves(knight_square)
    second_moves = []
    for move in first_moves:
        second_moves.append(knight_legal_moves(move))

    return [item for move_list in second_moves for item in move_list]


def filter_moves(king_move, knight_move):
    possible_king_moves = king_legal_moves(king_move)
    possible_knight_moves = knight_legal_moves(knight_move)
    knight_square_color = square_colors[knight_move]

    final_king_moves = []

    for move in possible_king_moves:
        if square_colors[move] != knight_square_color:
            final_king_moves.append(move)

    return {
        # "King Moves": possible_king_moves,
        "Knight Moves": possible_knight_moves,
        "Knight Square Color": knight_square_color,
        "Final King Moves": final_king_moves,
    }


# pprint(filter_moves("a8", "h1"))
# pprint(filter_moves("b8", "f2"))
# pprint(filter_moves("a7", "d3"))
# pprint(filter_moves("b8", "b2"))
# pprint(filter_moves("a7", "c4"))
# pprint(filter_moves("b8", "a3"))
# pprint(filter_moves("a7", "b5"))

# print(square_colors["a7"])


# def choose_king_moves(king_square, knight_square, number_of_moves):
#     king_moves_list = []
#     knight_moves_list = []

#     nl = len(knight_moves_list)

#     new_king_square = king_square
#     new_knight_square = knight_square

#     # Creates move lists
#     for i in range(number_of_moves):
#         # Get list of possible King moves, make a random choice
#         possible_king_moves = king_legal_moves(new_king_square)
#         king_move = random.choice(possible_king_moves)

#         # Prevent King from taking a square the Knight is currently on
#         if nl > 0 and king_move == knight_moves_list[nl - 1]:
#             possible_king_moves.remove(knight_moves_list[nl - 1])
#             king_move = random.choice(possible_king_moves)

#         # Add King move to move list
#         king_moves_list.append(king_move)
#         new_king_square = king_move

#         # Get list of possible Knight moves, make a random choice
#         possible_knight_moves = knight_legal_moves(new_knight_square)
#         knight_move = random.choice(possible_knight_moves)

#         # Prevent Knight from taking the square the King is currently on
#         if knight_move == king_move:
#             possible_knight_moves.remove(king_move)
#             knight_move = random.choice(possible_knight_moves)

#         #  Add Knight move to move list
#         knight_moves_list.append(knight_move)
#         new_knight_square = knight_move

#         # Check if Knights move puts the King in Check
#         if king_move in knight_legal_moves(knight_move):
#             king_moves_list[i] = king_moves_list[i] + "-CHECK"

#     return {"King Moves": king_moves_list, "Knight Moves": knight_moves_list}


# pprint(board)
# pprint(squares)
# print(king_legal_moves("g7"))
# pprint(knight_legal_moves("d4"))


# def play_game():
#     king_squares = ["a8", "e5", "g7", "a1"]
#     knight_squares = ["h1", "f2", "d4", "b1"]
#     number_of_moves = 6
#     results = {}

#     for i in range(len(king_squares)):
#         results[f"Game {i + 1}"] = choose_king_moves(
#             king_squares[i], knight_squares[i], number_of_moves
#         )

#     return results


# pprint(play_game())


#! FINAL SOLUTION
def choose_king_moves(king_square, knight_square, number_of_moves):
    king_moves_list = []
    new_king_square = king_square

    # Creates move lists
    for i in range(number_of_moves):
        # Get list of possible King moves
        possible_king_moves = king_legal_moves(new_king_square)

        # Get current Knight square color
        knight_square_color = square_colors[knight_square]

        final_king_moves = []

        for move in possible_king_moves:
            if len(king_moves_list) == 0:
                if square_colors[move] != knight_square_color:
                    final_king_moves.append(move)
            else:
                if (
                    square_colors[move]
                    != square_colors[king_moves_list[len(king_moves_list) - 1]]
                ):
                    final_king_moves.append(move)

        king_move = final_king_moves[0]

        # Add King move to move list
        king_moves_list.append(king_move)
        new_king_square = king_move
