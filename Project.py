import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event - Change Sprite Colour")

clock = pygame.time.Clock()

CHANGE_COLOUR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOUR_EVENT, 1000) 

class BoxSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill(self.random_colour())
        self.rect = self.image.get_rect(center=(x, y))

    def random_colour(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def change_colour(self):
        self.image.fill(self.random_colour())

sprite1 = BoxSprite(200, 200)
sprite2 = BoxSprite(400, 200)

sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOUR_EVENT:
            for sprite in sprites:
                sprite.change_colour()

    screen.fill((30, 30, 30))
    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()