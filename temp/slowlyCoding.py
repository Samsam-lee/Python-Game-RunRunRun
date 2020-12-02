import pygame, random
from time import sleep
import jump

WHITE = (255, 255, 255)
RED = (255, 0, 0)
pad_width = 1024
pad_height = 512
background_width = 900
amongus_width = 90
amongus_height = 120
obstacle1_width = 140
obstacle1_height = 61
obstacle2_width = 86
obstacle2_height = 59
tree_width = 60
tree_height = 131

# 속도와 질량 기본 값
VELOCITY = 7  # 속도
MASS = 2  # 질량

# <-- print text
def textObj(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()
# -->

# <-- message
def dispMessage(text):
    global gamepad

    largeText = pygame.font.Font('04B_19.TTF', 115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((pad_width/2), (pad_height/2))
    gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()
# -->

# <-- crash
def crash():
    global gamepad
    dispMessage('Crashed!')
# -->

# <-- background, character, obstacle
def drawObject(obj, x,y):
    global gamepad
    gamepad.blit(obj, (x,y))
# -->

# <-- initGame() 에서 호출!
def runGame():
    global gamepad, clock, obstacles, background1, background2, background3, underBackground
    global test, test2, test3, test4, jump_img, tree

    # 플레이어 자동차 생성
    player = jump.Characters(VELOCITY, MASS)

    player.load_image(test, pad_width, pad_height)  # 플레이어 캐릭터

    leg_swap = 0;

    # x = pad_width * 0.05
    # y = pad_height * 0.8

    background1_x = 0
    background2_x = background_width
    background3_x = background_width * 2
    underBack_x = 0

    obstacle_x = pad_width
    obstacle_y = random.randrange(0, pad_height)
    random.shuffle(obstacles)
    obstacle = obstacles[0]

    tree_x = pad_width
    tree_y = pad_height - tree_height

    # 게임 종료를 위한 변수
    crashed = False
    while not crashed:
        keys = pygame.key.get_pressed()
        # 스페이스키가 눌려있고, isJump가 2라면 1로 변경한다.
        # 이 작업을 해주지 않으면 스페이스가 눌려있는 상태면 플레이어가 계속 위로 올라가게 된다.
        if (keys[pygame.K_SPACE]):
            if player.isJump == 2:
                player.jump(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            # 화살표 키를 이용해서 플레이어의 움직임 거리를 조정해준다.
            # 키를 떼면 움직임 거리를 0으로 한다.
            if event.type == pygame.KEYDOWN:
                # 스페이스키를 눌렀을 때,
                # 0이면 바닥인 상태 : 1로 변경
                # 1이면 점프를 한 상태 : 2로 변경, 점프한 위치에서 다시 점프를 하게 된다. 즉, 이중점프
                if event.key == pygame.K_SPACE:
                    if player.twoJumpNo != 1:  # 2단 점프
                        if player.isJump == 0:
                            player.jump(1)
                        elif player.isJump == 1:
                            player.jump(2)
                            player.twoJumpNo = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0

        # y += y_change
        gamepad.fill(WHITE)

        # 배경 2 씩 이동
        background1_x -= 2
        background2_x -= 2
        background3_x -= 2
        underBack_x -= 2
        # 배경이 다 지나가면 다시 설정
        if background1_x == -(background_width*2):
            background1_x = background_width*2
        if background2_x == -(background_width*2):
            background2_x = background_width*2
        if background3_x == -(background_width*2):
            background3_x = background_width*2

        if underBack_x == -(underBack_x):
            underBack_x = 0

        # 장애물이 없으면 60씩 이동(시간 지체)
        # 장애물이 있으면 20씩 이동
        if obstacle[1] == None:
            obstacle_x -= 60
        else:
            if obstacle[0] == 1:
                obstacle_y += 5
            obstacle_x -= 20
        # 장애물이 다 지나가면 다시 설정
        if obstacle_x <= 0:
            obstacle_x = pad_width
            obstacle_y = random.randrange(0, (pad_height - amongus_height))
            random.shuffle(obstacles)
            obstacle = obstacles[0]

        tree_x -= 20
        if tree_x <= 0:
            tree_x = pad_width

        # position
        # 캐릭터가 화면 안에서만 움직이게
        # y += y_change
        # if y < 0:
        #     y = 0
        # elif y > pad_height - amongus_height:
        #     y = pad_height - amongus_height

        # wwwww장애물wwwwww
        if obstacle[1] != None:
            if obstacle[0] == 0:
                obstacle_width = obstacle1_width
                obstacle_height = obstacle1_height
            elif obstacle[0] == 1:
                obstacle_width = obstacle2_width
                obstacle_height = obstacle2_height
            
            # 원래 코드
            # if x + player.rect.x >= obstacle_x:
            #     if(y > obstacle_y and y < obstacle_y + obstacle_height) or\
            #         (y+player.rect.y > obstacle_y and y + player.rect.y < obstacle_y + obstacle_height):
            #         crash()
            # 바꾼 코드
            if (player.rect.x >= obstacle_x and player.rect.x <= obstacle_x + obstacle_width):
                if(player.rect.y > obstacle_y and player.rect.y < obstacle_y + obstacle_height):
                    crash()

        if(player.rect.x >= tree_x and player.rect.x <= tree_x + tree_width):
            if(player.rect.y > tree_y and player.rect.y < tree_y + tree_height):
                crash()


        ''' 게임 코드 작성 '''
        player.update(VELOCITY, pad_height)

        # ''' 게임 코드 끝 '''
        '''어몽어스 그리기'''
        if player.isJump == 0:  # 바닥 일 때
            if leg_swap == 0:
                player.chan_image(test)  # 플레이어 캐릭터 이미지 바꾸기
                leg_swap = 1;

            elif leg_swap == 1:
                player.chan_image(test2)
                leg_swap = 2;

            elif leg_swap == 2:
                player.chan_image(test3)
                leg_swap = 3;

            elif leg_swap == 3:
                player.chan_image(test4)
                leg_swap = 0;
        else:  # 1단 점프
            player.chan_image(jump_img)
            if player.twoJumpNo == 1:
                player.chan_image(test)

        # 화면에 출력
        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)
        drawObject(background3, background3_x, 0)
        drawObject(underBackground, underBack_x, 0)
        if obstacle[1] != None:
            drawObject(obstacle[1], obstacle_x, obstacle_y)
        drawObject(tree, tree_x, tree_y)
        # 플레이어 캐릭터 화면에 그려주기
        player.draw_Characters(gamepad)

        pygame.display.update()
        clock.tick(20)

    # 초기화 한 PyGame 종료
    pygame.quit()
    quit()
# -->

# 게임을 초기화하고 시작하는 함수
def initGame():
    global gamepad, clock, obstacles, background1, background2, background3, underBackground
    global test, test2, test3, test4, jump_img, tree
    obstacles = []

    # pygame 라이브러리 초기화
    # 처음에 항상 pygame.init() 호출 필수
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("PyFlying")
    # 그림
    test = 'among_jump/am01.png'
    test2 = 'among_jump/am02.png'
    test3 = 'among_jump/am03.png'
    test4 = 'among_jump/am04.png'
    jump_img = 'among_jump/jump.png'
    background1 = pygame.image.load('background.png')
    background2 = pygame.image.load('background2.png')
    background3 = pygame.image.load('background3.png')
    underBackground = pygame.image.load('underBack_.png')
    obstacles.append((0, pygame.image.load('obstacle1.png')))
    obstacles.append((1, pygame.image.load('obstacle2.png')))
    tree = pygame.image.load('tree.png')

    # 장애물 갯수 조절
    for i in range(3):
        obstacles.append((i+2, None))

    # FPS 설정을 위해 clock 생성 (runGame에서 사용 -> clock.tick(60) -> 60프레임)
    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__':
    initGame()