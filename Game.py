
def printGame(data):
    print('   A | B | C ')
    print('  ---|---|---')
    print("1|", data['a1'], "|", data['b1'], "|", data['c1'], "|")
    print('  ---|---|---')
    print("2|", data['a2'], "|", data['b2'], "|", data['c2'], "|")
    print('  ---|---|---')
    print("3|", data['a3'], "|", data['b3'], "|", data['c3'], "|")
    print('  ---|---|---')

def go(player):
    global data
    print('Ход игрока ', player)
    wait=True
    while wait:
        nextStep=input('Введите ячейку в формате букваЦифра (например a1): ')
        if nextStep in data.keys():
            if data[nextStep]==' ':
                data[nextStep]=player
                wait=False
            else:
                print('Ячейка уже занята. Выберите другую.')
        else:
            print('Такой ячейки нет на поле. Выберите с a1 по c3')

def winner(player):
    if (data['a1']==data['b1']==data['c1']==player) or (data['a2']==data['b2']==data['c2']==player) or (data['a3']==data['b3']==data['c3']==player) or (data['a1']==data['a2']==data['a3']==player) or (data['b1']==data['b2']==data['b3']==player) or (data['c1']==data['c2']==data['c3']==player) or (data['a1']==data['b2']==data['c3']==player) or (data['a3']==data['b2']==data['c1']==player):
        print('Player ', player, 'WIN!')
        return True

def isItAll(data):
    for item in data:
        if data[item]==' ':
            return False
    print('НИЧЬЯ!')
    return True

def replay():
    return input('Сыграем еще раз? Enter Yes or No: ').lower().startswith('y')

while True:
    data = {'a1': ' ', 'b1': ' ', 'c1': ' ', 'a2': ' ', 'b2': ' ', 'c2': ' ', 'a3': ' ', 'b3': ' ', 'c3': ' '}

    printGame(data)

    while True:
        player='X'
        go(player)

        printGame(data)
        if winner(player):
            break
        if isItAll(data):
            break
        player='O'
        go(player)

        printGame(data)
        if winner(player):
            break
        if isItAll(data):
            break
    if not replay():
        break