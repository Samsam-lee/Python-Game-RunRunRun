import pygame, sys, random

MAX_WIDTH = 1024
MAX_HEIGHT = 512

def createTree():
    treeH = [tree_height, tree_height*2, tree_height*3]
    random_tree = random.choice(treeH)
    bottom_tree = imgTree.get_rect(midtop = (MAX_WIDTH, random_tree))
    top_tree = imgTree.get_rect(midbottom = (MAX_WIDTH, random_tree))
    return bottom_tree, top_tree


def main():
    # <-- set
    global gamepad, amongCharacter, clock, background1, background2, tree_height, imgTree
    
    pygame.init()
    pygame.display.set_caption('AmongUs')
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    amongCharacter = pygame.image.load('amongus.png')
    charHeight = amongCharacter.get_size()[1]
    # charBottom = MAX_HEIGHT - charHeight

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

        # draw background
        screen.blit(background1, (background1_x, 0))
        screen.blit(background2, (background2_x, 0))

        # draw character
        screen.blit(amongCharacter, (0, MAX_HEIGHT - charHeight))

		# tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # draw tree
        tempNum = random.choice([1, 2])

        if(tempNum == 1):
            screen.blit(imgTree, (tree_x, tree_y))
        else:
            screen.blit(pygame.transform.flip(imgTree, False, True), (tree_x, 0))

        # update
        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__':
    main()
