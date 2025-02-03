import pygame as pg
import os
from Gomoku.config import *
import time


class GameObject:
    def __init__(self, image, color, pos):
        self.image = image
        self.color = color
        self.pos = image.get_rect(center=pos)


class Button(object):
    def __init__(self, text, color, x=None, y=None):
        self.surface = font_big.render(text, True, color)
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        self.x = x
        self.y = y

    def check_click(self, position):
        x_match = self.x < position[0] < self.x + self.WIDTH
        y_match = self.y < position[1] < self.y + self.HEIGHT
        if x_match and y_match:
            return True
        else:
            return False


def set_chess(board_inner, x, y, color):
    if board_inner[x][y] != ' ':
        print('You cannot choose this place')
        print(x, y)
        return False
    else:
        board_inner[x][y] = color
        print(x, y)
        return True


def check_win(board_inner):
    for list_str in board_inner:
        if ''.join(list_str).find('O' * 5) != -1:
            print('White Wins!')
            return 1
        elif ''.join(list_str).find('X' * 5) != -1:
            print('Black Wins!')
            return 0
    else:
        return -1


def check_win_all(board_inner):
    board_c = [[] for _ in range(29)]
    for x in range(15):
        for y in range(15):
            board_c[x - y].append(board_inner[x][y])
    board_d = [[] for _ in range(29)]
    for x in range(15):
        for y in range(15):
            board_d[x + y].append(board_inner[x][y])
    return [check_win(board_inner), check_win([list(i) for i in zip(*board_inner)]), check_win(board_c),
            check_win(board_d)]


def value(board_inner, temp_list, value_model):
    score = 0
    num = 0
    for list_str in board_inner:
        if len(''.join(list_str).replace(' ', '')) < 2:
            continue
        a = 0
        for i in range(11):
            if a == 0:
                temp = []
                for j in range(5, 12):
                    if i + j > len(list_str):
                        break
                    num += 1
                    if i == 0:
                        for k in value_model[0].items():
                            if ''.join(list_str[i:i + j]) == k[1][0]:
                                temp.append((i, k))
                    else:
                        if i + j < len(list_str):
                            for k in value_model[1].items():
                                if ''.join(list_str[i:i + j]) == k[1][0]:
                                    temp.append((i, k))
                        elif i + j == len(list_str):
                            for k in value_model[2].items():
                                if ''.join(list_str[i:i + j]) == k[1][0]:
                                    temp.append((i, k))
            else:
                a -= 1
                temp = []
            if temp:
                max_value = max([i[1][1][1] for i in temp])
                max_shape = [i for i in temp if i[1][1][1] == max_value][0]
                if max_shape[1][0] in ['4_3', '3_0', '3_16', '2_3']:
                    a = 1
                elif max_shape[1][0] in ['4_5', '4_13', '3_5', '2_0']:
                    a = 2
                elif max_shape[1][0] in ['4_4']:
                    a = 5
                temp_list.append(max_shape)
                score += max_value
    return score


def additional(te_list):
    score = 0
    temp_list = [i[1][0] for i in te_list]
    if sum([temp_list.count(i) for i in ['3_0', '3_3', '3_4', '3_5', '3_6', '4_1', '4_2', '4_3', '4_4',
                                         '4_5', '4_6', '4_7', '4_8', '4_9', '4_10', '4_11', '4_12',
                                         '4_13', '4_14', '4_15', '4_16',
                                         '4_17', '4_18', '4_19']]) >= 2:
        score += 30
    elif sum([temp_list.count(i) for i in ['3_0', '3_3', '3_4', '3_5', '3_6', '3_1', '3_2', '3_7', '3_8', '3_9', '3_10',
                                           '3_11', '3_12', '3_13', '3_14', '3_15', '3_16', '3_17']]) >= 2 \
            and sum([temp_list.count(i) for i in ['3_0', '3_3', '3_4', '3_5', '3_6']]) > 0:
        score += 15
    return score


def value_all(board_inner, temp_list, value_model):
    board_c = [[] for _ in range(29)]
    for x in range(15):
        for y in range(15):
            board_c[x + y].append(board_inner[x][y])
    board_d = [[] for _ in range(29)]
    for x in range(15):
        for y in range(15):
            board_d[x - y].append(board_inner[x][y])
    a = value(board_inner, temp_list, value_model)
    b = value([list(i) for i in zip(*board_inner)], temp_list, value_model)
    c = value(board_c, temp_list, value_model)
    d = value(board_d, temp_list, value_model)
    add = additional(temp_list)
    return a + b + c + d + add


def value_chess(board_inner):
    t1 = time.time()
    if board_inner == [[' '] * 15 for line in range(15)]:
        return 7, 7, 0
    temp_list_x = []
    temp_list_o = []
    tp_list_x_2 = []
    tp_list_o_2 = []
    tp_list_d = []
    score_x = value_all(board_inner, temp_list_x, value_model_X)
    pos_x = (0, 0)
    score_o = value_all(board_inner, temp_list_o, value_model_O)
    pos_o = (0, 0)
    pos_d = (0, 0)
    score_x_2 = 0
    score_o_2 = 0
    score_diff = 0
    chess_range_x = [x for x in range(15) if ''.join(board_inner[x]).replace(' ', '') != '']
    chess_range_y = [y for y in range(15) if ''.join([list(i) for i in zip(*board_inner)][y]).replace(' ', '') != '']
    range_x = (max(0, min(chess_range_x) - 4), min(max(chess_range_x) + 4, 15))
    range_y = (max(0, min(chess_range_y) - 4), min(max(chess_range_y) + 4, 15))
    for x in range(*range_x):
        for y in range(*range_y):
            tp_list_x = []
            tp_list_o = []
            tp_list_c = []
            if board_inner[x][y] != ' ':
                continue
            else:
                board_inner[x][y] = 'X'
                score_a = value_all(board_inner, tp_list_x, value_model_X)
                score_c = value_all(board_inner, tp_list_c, value_model_O)
                if score_a > score_x_2:
                    pos_x = x, y
                    tp_list_x_2 = tp_list_x
                    score_x_2 = score_a
                board_inner[x][y] = 'O'
                score_b = value_all(board_inner, tp_list_o, value_model_O)
                if score_b > score_o_2:
                    pos_o = x, y
                    tp_list_o_2 = tp_list_o
                    score_o_2 = score_b
                board_inner[x][y] = ' '
                diff = 1.1 * (score_a - score_x) + score_o - score_c + score_b - score_c
                if diff > score_diff:
                    pos_d = x, y
                    tp_list_d = tp_list_x
                    score_diff = diff
    if score_x_2 >= 1000:
        print('——' * 30)
        print('Strategy 1:')
        print('BLACK:', temp_list_x)
        print('WHITE:', temp_list_o)
        score = score_x_2
        pos = pos_x
        x, y = pos
        board_inner[x][y] = 'X'
        score_o_e = value_all(board_inner, temp_list_o, value_model_O)
        board_inner[x][y] = ' '
        print('Continue on strategy 1 - Win')
        print('Black best place:Cord {},X_score {},O_score {}'.format(pos, score, score_o_e))
        print('White original score {},expected{}, difference {}'.format(score_o, score_o_2, score_o_2 - score_o))
        print('If white placed on {},O_model{}'.format(pos_o, tp_list_o_2))
        print('Black original score{}, Expected highest{}, '
              'difference {}'.format(score_x, score_x_2, score_x_2 - score_x))
        print('If black placed on {},X_model{}'.format(pos_x, tp_list_x_2))
        print('——' * 30)
    elif score_o_2 >= 1000:
        print('——' * 30)
        print('Strategy 2')
        print('Black: ', temp_list_x)
        print('White: ', temp_list_o)
        x, y = pos_o
        board_inner[x][y] = 'X'
        temp_list_x.clear()
        score = value_all(board_inner, temp_list_x, value_model_X)
        score_o_e = value_all(board_inner, temp_list_o, value_model_O)
        board_inner[x][y] = ' '
        pos = pos_o
        print('Continue on strategy 2: Defense')
        print('Black best place:Cord {},Black score{}, White score{}'.format(pos, score, score_o_e))
        # print(' White best place:Cord {}'.format(pos_o))
        print(
            ' White original score{},expected highest{}, difference{}'.format(score_o, score_o_2, score_o_2 - score_o))
        print('If White placed on{}, White model{}'.format(pos_o, tp_list_o_2))
        print('Black original score{},expected max{}, difference{}'.format(score_x, score_x_2, score_x_2 - score_x))
        print('IfBlack placed on{},Black model{}'.format(pos_x, tp_list_x_2))
        print('——' * 30)
    else:
        print('——' * 30)
        print('Strategy 3 :')
        print('Black :', temp_list_x)
        print(' White :', temp_list_o)
        x, y = pos_d
        board_inner[x][y] = 'X'
        temp_list_x.clear()
        temp_list_o.clear()
        score = value_all(board_inner, temp_list_x, value_model_X)
        score_o_e = value_all(board_inner, temp_list_o, value_model_O)
        board_inner[x][y] = 'O'
        score_test = value_all(board_inner, [], value_model_O)
        board_inner[x][y] = ' '
        pos = pos_d
        print('Black original  score', score_x)
        print('Black score', score)
        print(' White original  score', score_o)
        print(' White score', score_o_e)
        print('If place White, White score', score_test)
        print('Black after', temp_list_x)
        print('Conduct Strategy3、Defense:Defense+Attack')
        print('score for me + score for opponent:{}'.format(score_diff))
        print('Black best place:Cord {},Black score{}, White score{}'.format(pos, score, score_o_e))
        # print(' White best place:Cord {}'.format(pos_o))
        print(' White original score{},expected max{}, difference{}'.format(score_o, score_o_2, score_o_2 - score_o))
        print('If White placed on{}, White model{}'.format(pos_o, tp_list_o_2))
        print('Black original score{},expected max{}, difference{}'.format(score_x, score_x_2, score_x_2 - score_x))
        print('If Black placed on{},Black model{}'.format(pos_x, tp_list_x_2))
        print('——' * 30)
    print('Over,Time：{} sec'.format(round(time.time() - t1, 2)))
    return *pos, score


def main():
    board_inner = board
    # init
    clock = pg.time.Clock()
    objects = []
    recover_objects = []
    ob_list = [objects, recover_objects]
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    black = pg.image.load('./Gomoku/data/chess_black.png').convert_alpha()
    white = pg.image.load('./Gomoku/data/chess_white.png').convert_alpha()
    background = pg.image.load('./Gomoku/data/bg.png').convert_alpha()
    regret_button = Button('Withdraw', RED, 630, 200)
    recover_button = Button('Redo', BLUE, 665, 300)
    restart_button = Button('Restart', GREEN, 655, 400)
    screen.blit(regret_button.surface, (regret_button.x, regret_button.y))
    screen.blit(recover_button.surface, (recover_button.x, recover_button.y))
    screen.blit(restart_button.surface, (restart_button.x, restart_button.y))
    pg.display.set_caption('Gomoku')
    flag = 0
    chess_list = [black, white]
    letter_list = ['X', 'O']
    word_list = ['Black', 'White']
    word_color = [(0, 0, 0), (255, 255, 255)]
    going = True
    while going:
        screen.blit(background, (0, 0))
        text = font.render('Term for {}'.format(word_list[flag]), True, word_color[flag])
        text_pos = text.get_rect(centerx=background.get_width() / 2, y=2)
        screen.blit(text, text_pos)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if regret_button.check_click(pos) or recover_button.check_click(pos):
                    index = 0 if regret_button.check_click(pos) else 1
                    if ob_list[index]:
                        x, y = [round((p + 18 - 27) / 40) for p in ob_list[index][-1].pos[:2]]
                        board_inner[y][x] = ' ' if index == 0 else ob_list[index][-1].color
                        ob_list[index - 1].append(ob_list[index][-1])
                        ob_list[index].pop()
                        try:
                            x, y = [round((p + 18 - 27) / 40) for p in ob_list[index][-1].pos[:2]]
                        except IndexError:
                            continue
                        board_inner[y][x] = ' ' if index == 0 else ob_list[index][-1].color
                        ob_list[index - 1].append(ob_list[index][-1])
                        ob_list[index].pop()
                elif restart_button.check_click(pos):
                    hint_text = font.render('RESTART', True, word_color[flag])
                    hint_text_pos = hint_text.get_rect(centerx=background.get_width() / 2, y=200)
                    screen.blit(hint_text, hint_text_pos)
                    pg.display.update()
                    pg.time.delay(1000)
                    board_inner = [[' '] * 15 for _ in range(15)]
                    objects.clear()
                    recover_objects.clear()
                    flag = 0
                    continue
                else:
                    a, b = round((pos[0] - 27) / 40), round((pos[1] - 27) / 40)
                    if a >= 15 or b >= 15:
                        continue
                    else:
                        x, y = max(0, a) if a < 0 else min(a, 14), max(0, b) if b < 0 else min(b, 14)
                        if set_chess(board_inner, y, x, letter_list[flag]):
                            objects.append(GameObject(chess_list[flag], letter_list[flag], (27 + x * 40, 27 + y * 40)))
                            recover_objects.clear()
                            if flag in check_win_all(board_inner):
                                for o in objects:
                                    screen.blit(o.image, o.pos)
                                win_text = font.render('{}Wins, Restart in 5 seconds'.format(word_list[flag]), True,
                                                       word_color[flag])
                                win_text_pos = win_text.get_rect(centerx=background.get_width() / 2, y=200)
                                screen.blit(win_text, win_text_pos)
                                pg.display.update()
                                pg.time.delay(5000)
                                board_inner = [[' '] * 15 for _ in range(15)]
                                objects.clear()
                                recover_objects.clear()
                                continue
                            flag ^= 1
                        else:
                            hint_text = font.render('Chess exist', True, word_color[flag])
                            hint_text_pos = hint_text.get_rect(centerx=background.get_width() / 2, y=200)
                            for o in objects:
                                screen.blit(o.image, o.pos)
                            screen.blit(hint_text, hint_text_pos)
                            pg.display.update()
                            pg.time.delay(300)
        if flag == 0:
            y, x = value_chess(board_inner)[:2]
            if set_chess(board_inner, y, x, letter_list[flag]):
                objects.append(GameObject(chess_list[flag], letter_list[flag], (27 + x * 40, 27 + y * 40)))
                if flag in check_win_all(board_inner):
                    for o in objects:
                        screen.blit(o.image, o.pos)
                    win_text = font.render('{} Wins, Restart in 5 sec'.format(word_list[flag]), True,
                                           word_color[flag])
                    win_text_pos = win_text.get_rect(centerx=background.get_width() / 2, y=200)
                    screen.blit(win_text, win_text_pos)
                    pg.display.update()
                    pg.time.delay(5000)
                    board_inner = [[' '] * 15 for _ in range(15)]
                    objects.clear()
                    recover_objects.clear()
                    continue
                flag ^= 1
        for o in objects:
            screen.blit(o.image, o.pos)
        clock.tick(60)
        pg.display.update()


main_dir = os.path.split(os.path.abspath(__file__))[0]
font = pg.font.SysFont('Times New Roman', 20)
font_big = pg.font.SysFont('Times New Roman', 40)


def run():
    pg.init()
    main()


if __name__ == '__main__':
    run()
