import pygame

COUNT_BLOCKS = 20
SIZE_BLOCK = 20
HEADER_COLOR = (0, 204, 153)
HEADER_MARGIN = 70
SNAKE_COLOR = (0, 102, 0)
FRAME_COLOR = (0, 255, 204)
BLUE = (204, 255, 255)
MARGIN = 1
WHITE = (255, 255, 255)
size = (SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK + HEADER_MARGIN)
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK, SIZE_BLOCK])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)
    draw_block(SNAKE_COLOR, 0, 0)


    pygame.display.flip()
