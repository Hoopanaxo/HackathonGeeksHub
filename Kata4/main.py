import pygame, random

#variables
screen_width = 920
screen_height = 560
obj_size = 50

#Colors
white_color = (200, 200, 200)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

def mover_rectangulo():
    global speed
    if rectangulo.top + obj_size < screen_height:
        rectangulo.top += speed

def mover_bola():
    global speed_bola_x,speed_bola_y

    #invierte sentido vertical
    if bola.top + obj_size > screen_height or bola.top <= 0:
        speed_bola_x = -speed_bola_x

    if bola.left + obj_size > screen_width or bola.left <= 0:
        start_bola()

    if bola.left < obj_size and rectangulo.top < bola.top < rectangulo.top + obj_size:
        speed_bola_y = -speed_bola_y

    bola.top += speed_bola_x
    bola.left += speed_bola_y

def start_bola():
    global speed_bola_x,speed_bola_y
    bola.top = screen_height // 2
    bola.left = screen_width // 2

    speed_bola_x = 3 * random.choice((1, -1))
    speed_bola_y = 3 * random.choice((1, -1))

rectangulo = pygame.Rect(10, 10, obj_size, obj_size)
bola = pygame.Rect(50, 10, obj_size, obj_size)
speed = 0
speed_bola_x = 3
speed_bola_y = 3

while True:
    screen.fill(light_gray)

    mover_rectangulo()
    mover_bola()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -3
            elif event.key == pygame.K_DOWN:
                speed = 3
        elif event.type == pygame.KEYUP:
            speed = 0
    pygame.draw.rect(screen,white_color, rectangulo )
    pygame.draw.ellipse(screen, white_color, bola)
    pygame.display.flip()
    clock.tick(60)
    