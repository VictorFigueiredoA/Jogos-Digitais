import pygame,sys

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,500))
    screen.blit(floor_surface,(floor_x_pos + 850,500))

pygame.init()
screen = pygame.display.set_mode((850,570))
clock = pygame.time.Clock()

#gameplay 
gravidade = 0.25
duck_movement = 0

bg_surface = pygame.image.load('background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('floor.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

duck_surface = pygame.image.load('skate_duck.png')
duck_surface = pygame.transform.scale(duck_surface,(80,80))
duck_rect = duck_surface.get_rect(center=(100,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                duck_movement = 0
                duck_movement -= 6
    screen.blit(bg_surface,(0,0))

    duck_movement += gravidade
    duck_rect.centery += duck_movement
    screen.blit(duck_surface,duck_rect)
    floor_x_pos -=1
    draw_floor()
    if floor_x_pos <= -850:
        floor_x_pos = 0
    screen.blit(floor_surface,(floor_x_pos,500))

    pygame.display.update()
    clock.tick(120)