def solution(keyinput, board):
    x, y = 0, 0
    max_x = board[0] // 2
    max_y = board[1] // 2
    dic = {"left": [-1, 0], "right": [1, 0], "up": [0, 1], "down": [0, -1]}

    for i in keyinput:
        if i in dic:
            new_x = x + dic[i][0]
            new_y = y + dic[i][1]

            if -max_x <= new_x <= max_x and -max_y <= new_y <= max_y:
                x = new_x
                y = new_y

    return [x, y]