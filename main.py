import pygame
import sys

pygame.init()

window_width = 800

# Налаштування вікна
screen = pygame.display.set_mode((window_width, 400))
pygame.display.set_caption("Виявлення та обробка колізій")

# Колір фону
background_color = (255, 255, 255)

width = 50
height = 50

# Параметри спрайтів
sprite1_x = 100
sprite1_y = 150
sprite1_width = width
sprite1_height = height
sprite1_color = (255, 0, 0)
sprite1_speed_x = 10

sprite2_x = 300
sprite2_y = 150
sprite2_width = width
sprite2_height = height
sprite2_color = (0, 0, 255)
sprite2_speed_x = -8

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Оновлення позиції спрайтів, політ за віссю Х
    sprite1_x += sprite1_speed_x
    sprite2_x += sprite2_speed_x

    # Виявлення колізій
    if (sprite1_x < sprite2_x + sprite2_width and sprite1_x + sprite1_width > sprite2_x and
        sprite1_y < sprite2_y + sprite2_height and sprite1_y + sprite1_height > sprite2_y):

        sprite1_speed_x *= -1
        sprite2_speed_x *= -1
    
    elif(sprite1_x <= 0):

        sprite1_speed_x *= -1

    elif(sprite2_x >= window_width - width):

        sprite2_speed_x *= -1

    # Оновлення відображення
    screen.fill(background_color)
    pygame.draw.rect(screen, sprite1_color, (sprite1_x, sprite1_y, sprite1_width, sprite1_height))
    pygame.draw.rect(screen, sprite2_color, (sprite2_x, sprite2_y, sprite2_width, sprite2_height))
    pygame.display.flip()

    clock.tick(60)  # Встановлення обмеження на 60 кадрів в секунду

pygame.quit()
sys.exit()
