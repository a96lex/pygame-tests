import pygame

COLOR_TRESHOLD = 0


class BackgroundChannel(object):
    value: int
    amount: int
    sign: int
    position: int

    def __init__(self, value, amount, sign, position) -> None:
        self.value = value
        self.amount = amount
        self.sign = sign
        self.position = position

        color = [0, 0, 0]
        color[position] = 255

        self.color = tuple(color)

    def update(self):
        new_val = self.value + self.sign * self.amount
        if 0 + COLOR_TRESHOLD > new_val or new_val > 255 - COLOR_TRESHOLD:
            self.sign = -self.sign
        self.value += self.sign * self.amount

    def draw(self, surface):
        rect = pygame.rect.Rect((10, 20 + 30 * self.position, 255, 20))
        pygame.draw.rect(surface, (0, 0, 0), rect)
        rect.width = self.value
        pygame.draw.rect(surface, self.color, rect)
