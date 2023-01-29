import random
import sys
import pygame
import pygame_menu

pygame.init()
bg_img = pygame.image.load('змейка-шаржа-смешная-3626431.jpg')
COUNT_BLOCKS = 20
SIZE_BLOCK = 20
HEADER_COLOR = (0, 204, 100)
HEADER_MARGIN = 70
SNAKE_COLOR = (255, 255, 0)
FRAME_COLOR = (100, 255, 204)
BLUE = (204, 200, 255)
BLACK = (0, 0 , 0)
RED = (224, 0, 0)
MARGIN = 1
WHITE = (255, 255, 255)
size = (SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK + HEADER_MARGIN)
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
timer = pygame.time.Clock()
calibri = pygame.font.SysFont('calibri', 32)
score_font = pygame.font.SysFont("comicsansms", 35)
res = 800


class Snake_Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    # head in snake blocks

    def __eq__(self, other):
        return isinstance(other, Snake_Block) and self.x == other.x and self.y == other.y


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK, SIZE_BLOCK])


def start_the_game():

    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS - 1)
        empty_block = Snake_Block(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
        return empty_block

    snake_blocks = [Snake_Block(9, 8), Snake_Block(9, 9), Snake_Block(9, 10)]
    apple = get_random_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    total = 0
    speed = 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        text_score = calibri.render(f'Score: {total}', 0, WHITE)
        text_speed = calibri.render(f'Speed: {speed}', 0, WHITE)
        screen.blit(text_score, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE

                draw_block(color, row, column)

        head = snake_blocks[-1]
        if not head.is_inside():
            print('crash')
            break
            # pygame.quit()
            # sys.exit()

        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)

        pygame.display.flip()

        if apple == head:
            total += 1
            speed = total // 5 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        d_row = buf_row
        d_col = buf_col
        new_head = Snake_Block(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print('kill yourself')
            # pygame.quit()
            # sys.exit()
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        timer.tick(3 + speed)


main_theme = pygame_menu.themes.THEME_ORANGE.copy()
main_theme.set_background_color_opacity(0.5)
menu = pygame_menu.Menu('', 220, 300,
                        theme=main_theme)

menu.add.text_input('Player :', default='_')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

while True:

    screen.blit(bg_img, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()
