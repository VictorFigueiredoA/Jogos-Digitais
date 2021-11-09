import pygame,sys

width = 850
height = 570
x=70
y=200
x_change=0
y_change=0
gravidade=2.5

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,500))
    screen.blit(floor_surface,(floor_x_pos + 850,500))

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#constantes do jogo
duck_movement = 0

#fundo
bg_surface = pygame.image.load('background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)


#chão e regulagem da imagem
floor_surface = pygame.image.load('floor.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0


#personagem e regulagem da imagem
duck_surface = pygame.image.load('skate_duck.png')
duck_surface = pygame.transform.scale(duck_surface,(80,80))
duck_rect = duck_surface.get_rect()

def test(x,y):
    screen.blit(duck_surface,(x,y))

while True:
    if y > height - 155:
        y = height - 155
    elif y < 0:
        y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #movimentação do pato, feita pelo jogador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_change=-2.5*gravidade
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                y_change=2*gravidade
    
    screen.blit(bg_surface,(0,0))
    y+=y_change
    #chão
    print(y)
    floor_x_pos -=1
    test(x,y)
    draw_floor()
    if floor_x_pos <= -850:
        floor_x_pos = 0
    screen.blit(floor_surface,(floor_x_pos,500))

    pygame.display.update()
    clock.tick(60)