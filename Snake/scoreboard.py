import pygame


class Scoreboard:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.score = 0

    def show_score(self):
        score_text = self.font.render(f"Score {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, [0, 0])

    def increase_score(self):
        self.score += 1

    def game_over(self):
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.screen.get_width() / 2,
                                                    self.screen.get_height() / 2))
        self.screen.blit(game_over_text, text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
