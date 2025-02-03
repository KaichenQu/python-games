import pygame

PINK = (255, 192, 203)
pygame.font.init()
FONT_MEDIUM = pygame.font.Font(None, 18)
FONT_MEDIUM.set_bold(True)


class Button:
    def __init__(self, x, y, w, h, text, font=FONT_MEDIUM, align='center'):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        if (align == 'center') or (align == 'left') or (align == 'right'):
            self.align = align
        else:
            raise ValueError("Invalid input of align: only 'center', 'left' or 'right' are allowed.")

        # TO DO: CODE DEFENSIVELY, ONLY PYGAME FONT OBJECTS
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, PINK, self.rect, 0)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        if self.align == 'center':
            text_pos = text_surf.get_rect(center=self.rect.center)
        elif self.align == 'left':
            text_y = self.rect.y + (self.rect.height - text_surf.get_height()) // 2
            text_pos = (self.rect.x, text_y)
        elif self.align == 'right':
            text_x = self.rect.x + self.rect.width - text_surf.get_width()
            text_y = self.rect.y + (self.rect.height - text_surf.get_height()) // 2
            text_pos = (text_x, text_y)
        else:
            raise ValueError("Invalid input of align: only 'center', 'left' or 'right' is allowed.")
        screen.blit(text_surf, text_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class TextBox:
    def __init__(self, x, y, w, h, text, font=FONT_MEDIUM, align='center'):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        if (align == 'center') or (align == 'left') or (align == 'right'):
            self.align = align
        else:
            raise ValueError("Invalid input of align: only 'center', 'left' or 'right' are allowed.")

        # TO DO: CODE DEFENSIVELY, ONLY PYGAME FONT OBJECTS
        self.font = font
        self.dark = False

    def draw(self, screen):
        pygame.draw.rect(screen, PINK, self.rect, 0)
        if not self.dark:
            text_surf = self.font.render(self.text, True, (255, 255, 255))
            if self.align == 'center':
                text_pos = text_surf.get_rect(center=self.rect.center)
            elif self.align == 'left':
                text_y = self.rect.y + (self.rect.height - text_surf.get_height()) // 2
                text_pos = (self.rect.x, text_y)
            elif self.align == 'right':
                text_x = self.rect.x + self.rect.width - text_surf.get_width()
                text_y = self.rect.y + (self.rect.height - text_surf.get_height()) // 2
                text_pos = (text_x, text_y)
            else:
                raise ValueError("Invalid input of align: only 'center', 'left' or 'right' is allowed.")
        else:
            text_surf = self.font.render(self.text, True, (235, 172, 183))
            if self.align == 'center':
                text_pos = text_surf.get_rect(center=self.rect.center)
            elif self.align == 'left':
                text_y = self.rect.y + (self.rect.height - text_surf.get_height()) // 2
                text_pos = (self.rect.x, text_y)
            elif self.align == 'right':
                text_x = self.rect.x + self.rect.width - text_surf.get_width()
                text_y = self.rect.y + (self.rect.height - text_surf.get_height()) // 2
                text_pos = (text_x, text_y)
            else:
                raise ValueError("Invalid input of align: only 'center', 'left' or 'right' is allowed.")
        screen.blit(text_surf, text_pos)

    def set_text(self, txt):
        self.text = txt

    def set_dark(self, is_dark):
        self.dark = is_dark


class Die:
    def __init__(self, x, y, w, h, text, font=FONT_MEDIUM):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.to_roll = True
        # TO DO: CODE DEFENSIVELY, ONLY PYGAME FONT OBJECTS
        self.font = font

    def draw(self, screen):
        if self.to_roll:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
            text_surf = self.font.render(self.text, True, (255, 255, 255))
        else:
            pygame.draw.rect(screen, (235, 172, 183), self.rect, 2)
            text_surf = self.font.render(self.text, True, (235, 172, 183))
        text_pos = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def set_text(self, txt):
        self.text = txt

    def set_to_roll(self, to_roll):
        self.to_roll = to_roll
