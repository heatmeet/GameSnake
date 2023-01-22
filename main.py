import pygame

size = [800, 800]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
