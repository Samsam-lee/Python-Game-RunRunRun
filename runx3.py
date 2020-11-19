import pygame, sys, random

pygame.init()
pygame.display.set_caption('AmongUs')
MAX_WIDTH = 1024
MAX_HEIGHT = 512


def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

	# tree
    imgTree = pygame.image.load('tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    while True:
        screen.fill((255, 255, 255))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
