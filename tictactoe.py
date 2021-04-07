# 7   #   8   #   9   #
#################################
#   4   #   5   #   6   #
##################################
#   1   #   2   #   3   #
##################################

board_dictionary = {'7': ' ', '8': ' ', '9': ' ',
                    '4': ' ', '5': ' ', '6': ' ',
                    '1': ' ', '2': ' ', '3': ' ',
                    }
board_keys = []
for key in board_dictionary:
    board_keys.append(key)


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')


def the_game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(board_dictionary)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()
        if board_dictionary[move] == ' ':
            board_dictionary[move] = turn
            count += 1
        else:
            print("That place is filled, Please try again")
            continue

        if count >= 5:
            if board_dictionary['7'] == board_dictionary['8'] == board_dictionary['9'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            elif board_dictionary['4'] == board_dictionary['5'] == board_dictionary['6'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            elif board_dictionary['1'] == board_dictionary['2'] == board_dictionary['3'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            elif board_dictionary['1'] == board_dictionary['4'] == board_dictionary['7'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            elif board_dictionary['2'] == board_dictionary['5'] == board_dictionary['8'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            elif board_dictionary['3'] == board_dictionary['6'] == board_dictionary['9'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            elif board_dictionary['1'] == board_dictionary['5'] == board_dictionary['9'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            elif board_dictionary['7'] == board_dictionary['5'] == board_dictionary['3'] != ' ':
                print_board(board_dictionary)
                print("\nGame Over. \n")
                print("*******" + turn + " won.******")
                break

            # If neither X or O wins the decision will be tie

        if count == 9:
            print("\n Game Over \n")
            print("It's a Tie ")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        # Change player after every move


restart = input("Do you want to play again ? (Y/N)")

if restart == 'Y' or restart == 'y':
    for key in board_keys:
        board_dictionary[key] = " "




if __name__ == "__main__":
    the_game()
