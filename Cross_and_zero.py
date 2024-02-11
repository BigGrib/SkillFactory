
def show_board():
    print('\n-----------')
    print(board[0], end=' ')
    print(board[1], end=' ')
    print(board[2], end=' ')
    print(board[3], end=' ')
    print(board[4], end=' ')
    print('\n-----------')
    print(board[5], end=' ')
    print(board[6], end=' ')
    print(board[7], end=' ')
    print(board[8], end=' ')
    print(board[9], end=' ')
    print('\n-----------')
    print(board[10], end=' ')
    print(board[11], end=' ')
    print(board[12], end=' ')
    print(board[13], end=' ')
    print(board[14], end=' ')
    print('\n-----------')

def turn(step, num):
    ind = board.index(step)
    board[ind] = num

def get_result():
    win = 0
    for i in line_to_victory:
        if board[i[0]] == "x" and board[i[1]] == "x" and board[i[2]] == "x":
            win = 1
        if board[i[0]] == "o" and board[i[1]] == "o" and board[i[2]] == "o":
            win = 2
    return win

def start_game():
    print(f'Играют:'
          f'\nX - {player1}'
          f'\nO - {player2}')

def winner(win):
    if win == 1:
        wins[0] = wins[0] + 1
        print(f'победил {player1}  {wins[0]} раз(а)')
        show_board()
    if win == 2:
        wins[1] = wins[1] + 1
        print(f'победил {player2} {wins[1]} раз(а)')
        show_board()
    if win == 3:
        print('Ничья')
        show_board()

def one_more():
    global board
    flag1 = True
    print("хотите сыграть?  y/n - ")
    play = input()
    if play == 'y':
        flag1 = flag1
    else: flag1 = not flag1
    board = [1, '|', 2, '|', 3,
             4, '|', 5, '|', 6,
             7, '|', 8, '|', 9]
    return flag1


def game(count = 0):
    game_over = False
    flag = True
    while game_over == False:
        show_board()
        if flag == True:
            num = "x"
            step = int(input(f"{player1}, ваш ход: "))
        else:
            num = "o"
            step = int(input(f"{player2}, ваш ход: "))
        turn(step, num)
        win = get_result()
        count += 1
        print(count)
        if count == 9:
            win = 3
        if win != 0:
            game_over = True
        else:
            game_over = False
        flag = not (flag)
        if count == 9:
            win = 3
    return (win)

def play():
    while one_more() == True:
        start_game()
        winner(game())
    print("спасибо за игру")

board = [1,'|',2,'|',3,
        4,'|',5,'|',6,
        7,'|',8,'|',9]

line_to_victory = [[0, 2, 4],
             [5, 7, 9],
             [10, 12, 14],
             [0, 7, 14],
             [4, 7, 10],
             [0, 5, 10],
             [2, 7, 12],
             [4, 9, 14]]
wins = [0, 0]
player1 = input('Введите имя первого игрока  -  ')
player2 = input('Введите имя второго игрока  -  ')
play()

