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


class Snake_Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK, SIZE_BLOCK])


snake_block = [Snake_Block(9, 9), Snake_Block(9, 10)]

d_row = 0
d_col = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)

    for block in snake_block:
        draw_block(SNAKE_COLOR, block.x, block.y)
        block.x += d_row
        block.y += d_col

    pygame.display.flip()
    timer.tick(2)
