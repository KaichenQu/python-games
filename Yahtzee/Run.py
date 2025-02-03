import pygame

from Yahtzee.Game import Game
from Yahtzee.GUI import PINK, Button, TextBox, Die


pygame.font.init()
FONT_LARGE = pygame.font.Font(None, 36)
FONT_LARGE.set_bold(True)

FONT_MEDIUM = pygame.font.Font(None, 18)
FONT_MEDIUM.set_bold(True)


def run():
    game = Game()

    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Yahtzee")

    # initialize all UI elements
    btn_roll = Button(490, 570, 100, 50, "ROLL!", font=FONT_LARGE, align='center')
    tbox_message_1 = TextBox(390, 460, 300, 30, "MESSAGE", font=FONT_MEDIUM, align='center')
    tbox_message_2 = TextBox(390, 490, 300, 30, "MESSAGE", font=FONT_MEDIUM, align='center')
    tbox_message_3 = TextBox(390, 520, 300, 30, "MESSAGE", font=FONT_MEDIUM, align='center')
    btn_restart = Button(490, 570, 100, 50, "ONE MORE GAME!", font=FONT_LARGE, align='center')

    tbox_name_p1 = TextBox(10, 10, 120, 30, game.p1, font=FONT_LARGE, align='left')
    btn_ones_p1 = Button(10, 50, 80, 20, "ONES" , font=FONT_MEDIUM, align='left')
    btn_twos_p1 = Button(10, 70, 80, 20, "TWOS", font=FONT_MEDIUM, align='left')
    btn_threes_p1 = Button(10, 90, 80, 20, "THREES", font=FONT_MEDIUM, align='left')
    btn_fours_p1 = Button(10, 110, 80, 20, "FOURS", font=FONT_MEDIUM, align='left')
    btn_fives_p1 = Button(10, 130, 80, 20, "FIVES", font=FONT_MEDIUM, align='left')
    btn_sixes_p1 = Button(10, 150, 80, 20, "SIXES", font=FONT_MEDIUM, align='left')
    tbox_upper_sec_p1 = TextBox(10, 170, 80, 20, "UPPER SEC", font=FONT_MEDIUM, align='left')
    tbox_bonus_p1 = TextBox(10, 190, 80, 20, "BONUS", font=FONT_MEDIUM, align='left')
    btn_three_kind_p1 = Button(130, 50, 120, 20, "THREE OF A KIND", font=FONT_MEDIUM, align='left')
    btn_four_kind_p1 = Button(130, 70, 120, 20, "FOUR OF A KIND", font=FONT_MEDIUM, align='left')
    btn_full_house_p1 = Button(130, 90, 120, 20, "FULL HOUSE", font=FONT_MEDIUM, align='left')
    btn_s_straight_p1 = Button(130, 110, 120, 20, "SMALL STRAIGHT", font=FONT_MEDIUM, align='left')
    btn_l_straight_p1 = Button(130, 130, 120, 20, "LARGE STRAIGHT", font=FONT_MEDIUM, align='left')
    btn_yahtzee_p1 = Button(130, 150, 120, 20, "YAHTZEE", font=FONT_MEDIUM, align='left')
    btn_chance_p1 = Button(130, 170, 120, 20, "CHANCE", font=FONT_MEDIUM, align='left')
    tbox_total_p1 = TextBox(130, 190, 120, 20, "TOTAL", font=FONT_MEDIUM, align='left')

    score_ones_p1 = TextBox(90, 50, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_twos_p1 = TextBox(90, 70, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_threes_p1 = TextBox(90, 90, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_fours_p1 = TextBox(90, 110, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_fives_p1 = TextBox(90, 130, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_sixes_p1 = TextBox(90, 150, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_upper_sec_p1 = TextBox(90, 170, 40, 20, "0", font=FONT_MEDIUM, align='center')
    score_bonus_p1 = TextBox(90, 190, 40, 20, "0", font=FONT_MEDIUM, align='center')
    score_three_kind_p1 = TextBox(250, 50, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_four_kind_p1 = TextBox(250, 70, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_full_house_p1 = TextBox(250, 90, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_s_straight_p1 = TextBox(250, 110, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_l_straight_p1 = TextBox(250, 130, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_yahtzee_p1 = TextBox(250, 150, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_chance_p1 = TextBox(250, 170, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_total_p1 = TextBox(250, 190, 40, 20, "0", font=FONT_MEDIUM, align='center')

    tbox_round = TextBox(390, 10, 300, 30, "ROUND %d / 13" % game.get_round(), font=FONT_LARGE, align='center')
    tbox_active_player = TextBox(390, 40, 300, 30, "%s'S TURN" % game.p1, font=FONT_LARGE, align='center')
    tbox_roll_chances = TextBox(390, 70, 300, 30, "ROLL %d / 3" % (3 - game.get_i_roll()), font=FONT_LARGE, align='center')

    btn_die_0 = Die(320, 320, 80, 80, "" , font=FONT_LARGE)
    btn_die_1 = Die(410, 320, 80, 80, "" , font=FONT_LARGE)
    btn_die_2 = Die(500, 320, 80, 80, "" , font=FONT_LARGE)
    btn_die_3 = Die(590, 320, 80, 80, "" , font=FONT_LARGE)
    btn_die_4 = Die(680, 320, 80, 80, "" , font=FONT_LARGE)

    tbox_name_p2 = TextBox(950, 10, 120, 30, game.p2, font=FONT_LARGE, align='right')
    btn_ones_p2 = Button(990, 50, 80, 20, "ONES" , font=FONT_MEDIUM, align='right')
    btn_twos_p2 = Button(990, 70, 80, 20, "TWOS" , font=FONT_MEDIUM, align='right')
    btn_threes_p2 = Button(990, 90, 80, 20, "THREES" , font=FONT_MEDIUM, align='right')
    btn_fours_p2 = Button(990, 110, 80, 20, "FOURS" , font=FONT_MEDIUM, align='right')
    btn_fives_p2 = Button(990, 130, 80, 20, "FIVES" , font=FONT_MEDIUM, align='right')
    btn_sixes_p2 = Button(990, 150, 80, 20, "SIXES" , font=FONT_MEDIUM, align='right')
    tbox_upper_sec_p2 = TextBox(990, 170, 80, 20, "UPPER SEC" , font=FONT_MEDIUM, align='right')
    tbox_bonus_p2 = TextBox(990, 190, 80, 20, "BONUS" , font=FONT_MEDIUM, align='right')
    btn_three_kind_p2 = Button(830, 50, 120, 20, "THREE OF A KIND", font=FONT_MEDIUM, align='right')
    btn_four_kind_p2 = Button(830, 70, 120, 20, "FOUR OF A KIND", font=FONT_MEDIUM, align='right')
    btn_full_house_p2 = Button(830, 90, 120, 20, "FULL HOUSE", font=FONT_MEDIUM, align='right')
    btn_s_straight_p2 = Button(830, 110, 120, 20, "SMALL STRAIGHT", font=FONT_MEDIUM, align='right')
    btn_l_straight_p2 = Button(830, 130, 120, 20, "LARGE STRAIGHT", font=FONT_MEDIUM, align='right')
    btn_yahtzee_p2 = Button(830, 150, 120, 20, "YAHTZEE", font=FONT_MEDIUM, align='right')
    btn_chance_p2 = Button(830, 170, 120, 20, "CHANCE", font=FONT_MEDIUM, align='right')
    tbox_total_p2 = TextBox(830, 190, 120, 20, "TOTAL" , font=FONT_MEDIUM, align='right')

    score_ones_p2 = TextBox(950, 50, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_twos_p2 = TextBox(950, 70, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_threes_p2 = TextBox(950, 90, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_fours_p2 = TextBox(950, 110, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_fives_p2 = TextBox(950, 130, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_sixes_p2 = TextBox(950, 150, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_upper_sec_p2 = TextBox(950, 170, 40, 20, "0", font=FONT_MEDIUM, align='center')
    score_bonus_p2 = TextBox(950, 190, 40, 20, "0", font=FONT_MEDIUM, align='center')
    score_three_kind_p2 = TextBox(790, 50, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_four_kind_p2 = TextBox(790, 70, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_full_house_p2 = TextBox(790, 90, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_s_straight_p2 = TextBox(790, 110, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_l_straight_p2 = TextBox(790, 130, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_yahtzee_p2 = TextBox(790, 150, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_chance_p2 = TextBox(790, 170, 40, 20, "", font=FONT_MEDIUM, align='center')
    score_total_p2 = TextBox(790, 190, 40, 20, "0", font=FONT_MEDIUM, align='center')

    # collection of all elements
    elem_collction = [
        tbox_name_p1, tbox_name_p2, tbox_message_1, tbox_message_2, tbox_message_3, \
        tbox_round, tbox_active_player, tbox_roll_chances, btn_die_0, btn_die_1, btn_die_2, btn_die_3, btn_die_4,\
        btn_ones_p1, btn_twos_p1, btn_threes_p1, btn_fours_p1, btn_fives_p1, btn_sixes_p1, tbox_upper_sec_p1, tbox_bonus_p1, \
        btn_three_kind_p1, btn_four_kind_p1, btn_full_house_p1, btn_s_straight_p1, btn_l_straight_p1, btn_yahtzee_p1, btn_chance_p1, tbox_total_p1, \
        score_ones_p1, score_twos_p1, score_threes_p1, score_fours_p1, score_fives_p1, score_sixes_p1, score_upper_sec_p1, score_bonus_p1, \
        score_three_kind_p1, score_four_kind_p1, score_full_house_p1, score_s_straight_p1, score_l_straight_p1, score_yahtzee_p1, score_chance_p1, score_total_p1, \
        btn_ones_p2, btn_twos_p2, btn_threes_p2, btn_fours_p2, btn_fives_p2, btn_sixes_p2, tbox_upper_sec_p2, tbox_bonus_p2, \
        btn_three_kind_p2, btn_four_kind_p2, btn_full_house_p2, btn_s_straight_p2, btn_l_straight_p2, btn_yahtzee_p2, btn_chance_p2, tbox_total_p2, \
        score_ones_p2, score_twos_p2, score_threes_p2, score_fours_p2, score_fives_p2, score_sixes_p2, score_upper_sec_p2, score_bonus_p2, \
        score_three_kind_p2, score_four_kind_p2, score_full_house_p2, score_s_straight_p2, score_l_straight_p2, score_yahtzee_p2, score_chance_p2, score_total_p2\
    ]

    # collection of 5 dice button
    dice_collection = [btn_die_0, btn_die_1, btn_die_2, btn_die_3, btn_die_4]
    dice_to_roll = [True, True, True, True, True]

    p1_score_tboxes = {
        '1s': score_ones_p1,
        '2s': score_twos_p1,
        '3s': score_threes_p1,
        '4s': score_fours_p1,
        '5s': score_fives_p1,
        '6s': score_sixes_p1,
        '3-of-a-kind': score_three_kind_p1,
        '4-of-a-kind': score_four_kind_p1,
        'full-house': score_full_house_p1,
        'small-straight': score_s_straight_p1,
        'large-straight': score_l_straight_p1,
        'yahtzee': score_yahtzee_p1,
        'chance': score_chance_p1
    }
    p2_score_tboxes = {
        '1s': score_ones_p2,
        '2s': score_twos_p2,
        '3s': score_threes_p2,
        '4s': score_fours_p2,
        '5s': score_fives_p2,
        '6s': score_sixes_p2,
        '3-of-a-kind': score_three_kind_p2,
        '4-of-a-kind': score_four_kind_p2,
        'full-house': score_full_house_p2,
        'small-straight': score_s_straight_p2,
        'large-straight': score_l_straight_p2,
        'yahtzee': score_yahtzee_p2,
        'chance': score_chance_p2
    }

    def reset_dice():
        for i in range(5):
            dice_to_roll[i] = True
            dice_collection[i].set_to_roll(True)

    # Main loop of the pygame
    running = True
    game_continue = True
    while running:
        scores_p1 = game.get_score(0)
        scores_p2 = game.get_score(1)
        i_roll = game.get_i_roll()
        active_player = game.get_active_player()
        # handle the click events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if game_continue:
                # clickable elements are active
                # click the roll button
                if btn_roll.is_clicked(event):
                    if i_roll < 3:
                        game.roll([i for i in range(5) if dice_to_roll[i]])
                        # reset_dice()

                # click the dice
                if btn_die_0.is_clicked(event):
                    dice_to_roll[0] = not dice_to_roll[0]
                    btn_die_0.set_to_roll(dice_to_roll[0])
                if btn_die_1.is_clicked(event):
                    dice_to_roll[1] = not dice_to_roll[1]
                    btn_die_1.set_to_roll(dice_to_roll[1])
                if btn_die_2.is_clicked(event):
                    dice_to_roll[2] = not dice_to_roll[2]
                    btn_die_2.set_to_roll(dice_to_roll[2])
                if btn_die_3.is_clicked(event):
                    dice_to_roll[3] = not dice_to_roll[3]
                    btn_die_3.set_to_roll(dice_to_roll[3])
                if btn_die_4.is_clicked(event):
                    dice_to_roll[4] = not dice_to_roll[4]
                    btn_die_4.set_to_roll(dice_to_roll[4])

                # click to fill a score - p1
                if btn_ones_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['1s'] == -1):
                        game_continue = game.fill('1s')
                        reset_dice()
                if btn_twos_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['2s'] == -1):
                        game_continue = game.fill('2s')
                        reset_dice()
                if btn_threes_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['3s'] == -1):
                        game_continue = game.fill('3s')
                        reset_dice()
                if btn_fours_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['4s'] == -1):
                        game_continue = game.fill('4s')
                        reset_dice()
                if btn_fives_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['5s'] == -1):
                        game_continue = game.fill('5s')
                        reset_dice()
                if btn_sixes_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['6s'] == -1):
                        game_continue = game.fill('6s')
                        reset_dice()
                if btn_three_kind_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['3-of-a-kind'] == -1):
                        game_continue = game.fill('3-of-a-kind')
                        reset_dice()
                if btn_four_kind_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['4-of-a-kind'] == -1):
                        game_continue = game.fill('4-of-a-kind')
                        reset_dice()
                if btn_full_house_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['full-house'] == -1):
                        game_continue = game.fill('full-house')
                        reset_dice()
                if btn_s_straight_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['small-straight'] == -1):
                        game_continue = game.fill('small-straight')
                        reset_dice()
                if btn_l_straight_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['large-straight'] == -1):
                        game_continue = game.fill('large-straight')
                        reset_dice()
                if btn_yahtzee_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['yahtzee'] == -1):
                        game_continue = game.fill('yahtzee')
                        reset_dice()
                if btn_chance_p1.is_clicked(event):
                    if (active_player == 0) and (i_roll > 0) and (scores_p1['chance'] == -1):
                        game_continue = game.fill('chance')
                        reset_dice()

                # click to fill a score - p2
                if btn_ones_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['1s'] == -1):
                        game_continue = game.fill('1s')
                        reset_dice()
                if btn_twos_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['2s'] == -1):
                        game_continue = game.fill('2s')
                        reset_dice()
                if btn_threes_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['3s'] == -1):
                        game_continue = game.fill('3s')
                        reset_dice()
                if btn_fours_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['4s'] == -1):
                        game_continue = game.fill('4s')
                        reset_dice()
                if btn_fives_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['5s'] == -1):
                        game_continue = game.fill('5s')
                        reset_dice()
                if btn_sixes_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['6s'] == -1):
                        game_continue = game.fill('6s')
                        reset_dice()
                if btn_three_kind_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['3-of-a-kind'] == -1):
                        game.fill('3-of-a-kind')
                        reset_dice()
                if btn_four_kind_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['4-of-a-kind'] == -1):
                        game_continue = game.fill('4-of-a-kind')
                        reset_dice()
                if btn_full_house_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['full-house'] == -1):
                        game_continue = game.fill('full-house')
                        reset_dice()
                if btn_s_straight_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['small-straight'] == -1):
                        game_continue = game.fill('small-straight')
                        reset_dice()
                if btn_l_straight_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['large-straight'] == -1):
                        game_continue = game.fill('large-straight')
                        reset_dice()
                if btn_yahtzee_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['yahtzee'] == -1):
                        game_continue = game.fill('yahtzee')
                        reset_dice()
                if btn_chance_p2.is_clicked(event):
                    if (active_player == 1) and (i_roll > 0) and (scores_p2['chance'] == -1):
                        game_continue = game.fill('chance')
                        reset_dice()
            else:
                # only "one more game" is clickable
                if btn_restart.is_clicked(event):
                    game = Game()
                    game_continue = True
                    tbox_name_p1.set_text(game.p1)
                    tbox_name_p2.set_text(game.p2)

        # update the title
        tbox_round.set_text("ROUND %d / 13" % game.get_round())
        if game.get_active_player() == 0:
            tbox_active_player.set_text("%s'S TURN" % game.p1)
        else:
            tbox_active_player.set_text("%s'S TURN" % game.p2)
        tbox_roll_chances.set_text("ROLL %d / 3" % (3 - game.get_i_roll()))

        # update the total score
        if active_player == 0:
            for k, tbox in p1_score_tboxes.items():
                if scores_p1[k] == -1:
                    if i_roll > 0:
                        tbox.set_dark(True)
                        tbox.set_text(str(game.calculate_score(k)))
                    else:
                        tbox.set_dark(False)
                        tbox.set_text("")
                else:
                    tbox.set_dark(False)
                    tbox.set_text(str(scores_p1[k]))
            for k, tbox in p2_score_tboxes.items():
                if scores_p2[k] == -1:
                    tbox.set_dark(False)
                    tbox.set_text("")
                else:
                    tbox.set_dark(False)
                    tbox.set_text(str(scores_p2[k]))

        elif active_player == 1:
            for k, tbox in p2_score_tboxes.items():
                if scores_p2[k] == -1:
                    if i_roll > 0:
                        tbox.set_dark(True)
                        tbox.set_text(str(game.calculate_score(k)))
                    else:
                        tbox.set_dark(False)
                        tbox.set_text("")
                else:
                    tbox.set_dark(False)
                    tbox.set_text(str(scores_p2[k]))
            for k, tbox in p1_score_tboxes.items():
                if scores_p1[k] == -1:
                    tbox.set_dark(False)
                    tbox.set_text("")
                else:
                    tbox.set_dark(False)
                    tbox.set_text(str(scores_p1[k]))

        score_upper_sec_p1.set_text(str(game.upper_sec_total[0]))
        score_bonus_p1.set_text(str(game.bonus[0]))
        score_total_p1.set_text(str(game.total[0]))
        score_upper_sec_p2.set_text(str(game.upper_sec_total[1]))
        score_bonus_p2.set_text(str(game.bonus[1]))
        score_total_p2.set_text(str(game.total[1]))

        # update the dice
        for dice_btn, dice_num in zip(dice_collection, game.get_dice()):
            if dice_num == -1:
                dice_btn.set_text("")
            else:
                dice_btn.set_text(str(dice_num))

        # update message box
        if game_continue:
            if i_roll == 0:
                tbox_message_1.set_text("")
                tbox_message_2.set_text("")
                tbox_message_3.set_text("")
            elif i_roll > 2:
                tbox_message_1.set_text("")
                tbox_message_2.set_text("")
                tbox_message_3.set_text("CLICK ON ANY UNFILLED ROW IN YOUR TABLE TO SCORE ONCE.")
            else:
                tbox_message_1.set_text("CLICK TO LOCK/UNLOCK A DIE.")
                tbox_message_2.set_text("CLICK 'ROLL!' TO RE-ROLL ALL UNLOCKED DICE (WHITE).")
                tbox_message_3.set_text("CLICK ON ANY UNFILLED ROW NAME IN YOUR TABLE TO SCORE ONCE.")
        else:
            if game.get_winner() == 0:
                tbox_message_1.set_text("")
                tbox_message_2.set_text("")
                tbox_message_3.set_text("TIE GAME!")
            elif game.get_winner() == 1:
                tbox_message_1.set_text("%s WIN!" % game.p1)
                tbox_message_2.set_text("")
                tbox_message_3.set_text("")
            elif game.get_winner() == 2:
                tbox_message_1.set_text("%s WIN!" % game.p2)
                tbox_message_2.set_text("")
                tbox_message_3.set_text("")

        # clear everything in the frame
        screen.fill(PINK)

        # draw elements
        for elem in elem_collction:
            elem.draw(screen)

        # draw the button for restart
        if game_continue:
            if i_roll < 3:
                btn_roll.draw(screen)
        else:
            btn_restart.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    run()
    pygame.quit()
