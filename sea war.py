from random import randint, choice, random
board = []
for x in range(6):
      board.append(["O"] * 6)
for row in board:
    print((" ").join(row))
    shiprow = randint(0, len(board) - 1)
    shipcol = randint(0, len(board[0]) - 1)
    print('1) Легкий: 12 попыток')
    print('2) Средний: 8 попыток')
    print('3) Сложный: 4 попытки')
    print('4) Хард: 2 попытки')
    lvl = int(input('Выбери уровень сложности'))
 
    