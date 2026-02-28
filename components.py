import pygame
import random

class Ground:
    ground_level = 650

    def __init__(self, win_width):
        self.x, self.y = 0, Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, win_width, 5)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)


def draw_stretched_pipe(surface, image, x, y, width, height, cap_height=20):
    cap_height = min(cap_height, height // 2)

    top_cap    = image.subsurface((0, 0, image.get_width(), cap_height))
    middle     = image.subsurface((0, cap_height, image.get_width(), image.get_height() - cap_height * 2))
    bottom_cap = image.subsurface((0, image.get_height() - cap_height, image.get_width(), cap_height))

    surface.blit(pygame.transform.scale(top_cap, (width, cap_height)), (x, y))
    surface.blit(pygame.transform.scale(middle, (width, height - cap_height * 2)), (x, y + cap_height))
    surface.blit(pygame.transform.scale(bottom_cap, (width, cap_height)), (x, y + height - cap_height))


class Pipes:
    width = 52
    opening = 100
    image = None
    cap_height = 20

    def __init__(self, win_width):
        if Pipes.image is None:
            raw = pygame.image.load("assets/pipe.png").convert_alpha()
            Pipes.image = pygame.transform.scale(raw, (Pipes.width, 320))

        self.x = win_width
        self.bottom_height = random.randint(50, 450)
        self.top_height = Ground.ground_level - self.bottom_height - self.opening
        self.bottom_rect = pygame.Rect(0, 0, 0, 0)
        self.top_rect    = pygame.Rect(0, 0, 0, 0)
        self.passed = False
        self.off_screen = False

    def draw(self, window):
        pipe_w = Pipes.image.get_width()

        self.bottom_rect = pygame.Rect(
            self.x, Ground.ground_level - self.bottom_height,
            pipe_w, self.bottom_height
        )
        draw_stretched_pipe(
            window, Pipes.image,
            self.x, Ground.ground_level - self.bottom_height,
            pipe_w, self.bottom_height,
            Pipes.cap_height
        )

        flipped = pygame.transform.flip(Pipes.image, False, True)
        self.top_rect = pygame.Rect(self.x, 0, pipe_w, self.top_height)
        draw_stretched_pipe(
            window, flipped,
            self.x, 0,
            pipe_w, self.top_height,
            Pipes.cap_height
        )

    def update(self):
        self.x -= 1
        if self.x + Pipes.width <= 50:
            self.passed = True
        if self.x <= -Pipes.width:
            self.off_screen = True