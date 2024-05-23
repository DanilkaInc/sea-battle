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
    x = 10
    if lvl == 1:
      x = 12
    elif lvl == 2: 
      x = 8
    elif lvl == 3: 
      x = 4
    elif lvl == 4: 
      x = 2
    print("Да начнется игра!")
    for turn in range(x):
      print ("Ход: ", turn)
      grow = int(input("Строка 0-5:" ))
      gcol = int(input("Столбец 0-5:" ))
      if grow == shiprow and gcol == shipcol:
        print("Поздравляю!Ты выиграл!")
        break
      else:
        if (grow < 0 or grow > 5) or (gcol < 0 or gcol > 5):
            print("Ты вышел за игровое поле")
        elif(board[grow][gcol] == "X"):
            print("Эти координаты ты уже называл!")
        else:
            print("Не угадал! Мимо!")
            board[grow][gcol] = "X"
      for row in board:
        print((" ").join(row))
      if turn == x - 1:
        print("Конец! Ты проиграл!")
        continue
    