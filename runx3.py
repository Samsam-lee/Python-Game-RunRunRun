import pygame, sys, random

MAX_WIDTH = 1024
MAX_HEIGHT = 512


# def character(x, y):
#     global gamepad, amongCharacter
# 	gamepad.blit(amongCharacter, (x,y))

def main():
    global gamepad, amongCharacter, clock, background1, background2

    # <-- set screen, fps
    pygame.init()
    pygame.display.set_caption('AmongUs')
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # image
    amongCharacter = pygame.image.load('amongus.png')
    background1 = pygame.image.load('background.jpeg')
    background2 = background1.copy()

    clock = pygame.time.Clock()
    # -->

	# background
    x = MAX_WIDTH * 0.05
    y = MAX_HEIGHT * 0.8
    y_change = 0

    background1_x = 0
    background2_x = MAX_WIDTH

    crashed = False

	# tree
    imgTree = pygame.image.load('tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    while not crashed:
        screen.fill((255, 255, 255))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                sys.exit()

        background1_x -= 2
        background2_x -= 2

        if background1_x == -MAX_WIDTH:
            background1_x = MAX_WIDTH

        if background2_x == -MAX_WIDTH:
            background2_x = MAX_WIDTH

        screen.blit(background1, (background1_x, 0))
        screen.blit(background2, (background2_x, 0))

		# tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))

        # update
        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__':
    main()
