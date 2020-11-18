import pygame, sys, random

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (500,random_pipe_pos - 200))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 600:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe,pipe)

def remove_pipes(pipes):
	for pipe in pipes:
		if pipe.centerx == -600:
			pipes.remove(pipe)
	return pipes


# <--
game_active = True

pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()
screen = pygame.display.set_mode((900,600))

bg_surface = pygame.image.load('background.jpg').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

pipe_surface = pygame.image.load('obstacle.png')
pipe_surface = pygame.transform.scale(pipe_surface, (100, 250))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [150,300,450]
# -->

while True:
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    pygame.quit()
		    sys.exit()

	    if event.type == pygame.KEYDOWN:
		    pipe_list.clear()

	    if event.type == SPAWNPIPE:
        	pipe_list.extend(create_pipe())

    screen.blit(bg_surface,(0,0))

    if game_active:
		# Pipes
    	pipe_list = move_pipes(pipe_list)
    	pipe_list = remove_pipes(pipe_list)
    	draw_pipes(pipe_list)

    pygame.display.update()