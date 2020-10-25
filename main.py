import pygame
import random

pygame.init()
SIZE = (450, 700)
BACKGROUND_CLR = (40, 195, 140)
DICE_CLR = (235, 235, 150)
DOT_CLR = (0, 0, 0)
TXT_CLR = (120, 20, 150)
DOT_RAD = 12
DICE_SIZE = 150
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Dice Roller')
courier = pygame.font.SysFont('courier', 42, bold=True)


class DiceRoll:
    def __init__(self, x, y):
        self.x_coord = x * 50 + (x - 1) * DICE_SIZE
        self.y_coord = 100 + (y - 1) * (50 + DICE_SIZE)
        self.z = random.randint(1, 6)
        self.random_dots()

    def draw_dice(self):
        """Draw dice in 2 columns and 3 rows coords"""
        pygame.draw.rect(screen, DICE_CLR, (self.x_coord, self.y_coord, DICE_SIZE, DICE_SIZE))

    def dots_1(self):
        pygame.draw.circle(screen, DOT_CLR, (self.x_coord + DICE_SIZE // 2, self.y_coord + DICE_SIZE // 2), DOT_RAD)

    def dots_2(self):
        pygame.draw.circle(screen, DOT_CLR, (self.x_coord + 40, self.y_coord + 40), DOT_RAD)
        pygame.draw.circle(screen, DOT_CLR, (self.x_coord + DICE_SIZE - 40, self.y_coord + DICE_SIZE - 40), DOT_RAD)

    def dots_3(self):
        self.dots_1()
        self.dots_2()

    def dots_4(self):
        self.dots_2()
        pygame.draw.circle(screen, DOT_CLR, (self.x_coord + DICE_SIZE - 40, self.y_coord + 40), DOT_RAD)
        pygame.draw.circle(screen, DOT_CLR, (self.x_coord + 40, self.y_coord + DICE_SIZE - 40), DOT_RAD)

    def dots_5(self):
        self.dots_1()
        self.dots_4()

    def dots_6(self):
        self.dots_4()
        pygame.draw.circle(screen, DOT_CLR, (self.x_coord + 40, self.y_coord + DICE_SIZE // 2), DOT_RAD)
        pygame.draw.circle(screen, DOT_CLR, (self.x_coord + DICE_SIZE - 40, self.y_coord + DICE_SIZE // 2), DOT_RAD)

    def random_dots(self):
        self.draw_dice()
        method = getattr(DiceRoll, 'dots_' + str(self.z))
        method(self)


# IMPORTANT HINT
# import foo
# method_to_call = getattr(foo, 'bar')
# result = method_to_call()


def setup():
    num = 1
    while True:
        print('Random dice roller. Enter number of dices from 1 to 6 or type "stop" to quit')
        user_input = input()
        if user_input.lower() == 'stop':
            quit()
        if user_input in {'1', '2', '3', '4', '5', '6'}:
            num = int(user_input)
            app(num)
        elif user_input == '':
            app(num)
        else:
            print('Enter a number between 1 and 6. Try again.')


def app(num):
    while True:
        pygame.event.get()
        screen.fill(BACKGROUND_CLR)
        name = courier.render(f"Dice Roller", 3, TXT_CLR)
        screen.blit(name, (100, 30))
        count = 0
        total = 0
        for i in range(1, 3):
            if count >= num:
                break
            for j in range(1, 4):
                if count >= num:
                    break
                count += 1
                temp = DiceRoll(i, j)
                total += temp.z

        total_text = courier.render(f"Total: {total}", 3, TXT_CLR)
        screen.blit(total_text, (100, 650))
        pygame.display.flip()

        break


setup()
