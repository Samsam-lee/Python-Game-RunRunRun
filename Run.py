import pygame, random
from time import sleep
import jump

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pad_width = 1024
pad_height = 512
background_width = 1024

amongus_width = 90
amongus_height = 120

obstacle1_width = 200
obstacle1_height = 254
obstacle2_width = 72
obstacle2_height = 55

knife_width = 157
knife_height = 99

crashed = 3

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

    largeText = pygame.font.Font('./assets/fonts/04B_19.TTF', 115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((pad_width/2), (pad_height/2))
    gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()
# -->

# <-- crash
def crash():
    global gamepad, crashed
    crashed -= 1
    if crashed == 0: 
        dispMessage('End!')
# -->

# <-- background, character, obstacle
def drawObject(obj, x,y):
    global gamepad
    gamepad.blit(obj, (x,y))
# -->



# 게임을 초기화하고 시작하는 함수
def initGame():
    global gamepad, clock, obstacles, background1, background2
    global test, test2, test3, test4, jump_img, crashed, knives

    knives = []
    obstacles = []

    # pygame 라이브러리 초기화
    # 처음에 항상 pygame.init() 호출 필수
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("PyFlying")

    # 그림
    test = './assets/image/am01.png'
    test2 = './assets/image/am02.png'
    test3 = './assets/image/am03.png'
    test4 = './assets/image/am04.png'
    jump_img = './assets/image/amJump.png'

    background1 = pygame.image.load('./assets/image/background.png')
    background2 = pygame.image.load('./assets/image/background.png')

    knives.append((0, pygame.image.load('./assets/image/knife.png')))
    obstacles.append((0, pygame.image.load('./assets/image/obstacle.png')))
    obstacles.append((1, pygame.image.load('./assets/image/obstacle2.png')))

    # 장애물 갯수 조절
    for i in range(2):
        knives.append((i+1, None))
    for i in range(3):
        obstacles.append((i+2, None))
        
    # FPS 설정을 위해 clock 생성 (runGame에서 사용 -> clock.tick(60) -> 60프레임)
    clock = pygame.time.Clock()
    runGame()


# <-- initGame() 에서 호출!
def runGame():
    global gamepad, clock, obstacles, background1, background2
    global test, test2, test3, test4, jump_img, crashed, knives

    # 플레이어 자동차 생성
    player = jump.Characters(VELOCITY, MASS)

    player.load_image(test, pad_width, pad_height)  # 플레이어 캐릭터

    leg_swap = 0;

    # 배경 위치
    background1_x = 0
    background2_x = background_width

    # 장애물 위치
    obstacle_x = pad_width
    obstacle_y = pad_height - obstacle1_height
    obstacle2_y = pad_height - obstacle2_height
    random.shuffle(obstacles)
    obstacle = obstacles[0]
    

    # 칼 위치
    knife_x = pad_width
    knife_y = random.randrange(0, pad_height)
    random.shuffle(knives)
    knife = knives[0]


    # 게임 종료를 위한 변수
    if crashed != 0:
        flag = False
    else:
        flag = True

    while not flag:
        keys = pygame.key.get_pressed()
        # 스페이스키가 눌려있고, isJump가 2라면 1로 변경한다.
        # 이 작업을 해주지 않으면 스페이스가 눌려있는 상태면 플레이어가 계속 위로 올라가게 된다.
        if (keys[pygame.K_SPACE]):
            if player.isJump == 2:
                player.jump(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = 0

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

        # 배경이 다 지나가면 다시 설정
        if background1_x == -(background_width):
            background1_x = background_width
        if background2_x == -(background_width):
            background2_x = background_width

        # 장애물이 없으면 60씩 이동(시간 지체)
        # 장애물이 있으면 20씩 이동
        if obstacle[1] == None:
            obstacle_x -= 60
        else:
            obstacle_x -= 20
            # if obstacle[0] == 1:
            #     obstacle_x -= 10
        
        if obstacle_x <= 0:
            obstacle_x = pad_width
            random.shuffle(obstacles)
            obstacle = obstacles[0]


        # 칼 이동
        if knife[1] == None:
            knife_x -= 60
        else:
            knife_x -= 30

        # 장애물이 다 지나가면 다시 설정
        if knife_x <= 0:
            knife_x = pad_width
            knife_y = random.randrange(0, (pad_height - amongus_height))
            random.shuffle(knives)
            knife = knives[0]

        # wwwww장애물wwwwww
        if obstacle[1] != None:
            if obstacle[0] == 0:
                obstacle_width = obstacle1_width
                obstacle_height = obstacle1_height
                if(player.rect.x >= obstacle_x and player.rect.x <= obstacle_x + obstacle_width):
                    if(player.rect.y > obstacle_y and player.rect.y < obstacle_y + obstacle_height):
                        crash()

            elif obstacle[0] == 1:
                obstacle_width = obstacle2_width
                obstacle_height = obstacle2_height
                if(player.rect.x >= obstacle_x and player.rect.x <= obstacle_x + obstacle_width):
                    if(player.rect.y > obstacle2_y and player.rect.y < obstacle2_y + obstacle_height):
                        crash()

                    
        # 칼
        if knife[1] != None:            
            if (player.rect.x >= knife_x and player.rect.x <= knife_x + knife_width):
                if(player.rect.y > knife_y and player.rect.y < knife_y + knife_height):
                    crash()
            


        ''' 게임 코드 작성 '''
        player.update(VELOCITY, pad_height)

        '''캐릭터 그리기'''
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

        if obstacle[1] != None:
            if obstacle[0] == 0:
                drawObject(obstacle[1], obstacle_x, obstacle_y)
            if obstacle[0] == 1:
                drawObject(obstacle[1], obstacle_x, obstacle2_y)

        if knife[1] != None:
            drawObject(knife[1], knife_x, knife_y)

        # 플레이어 캐릭터 화면에 그려주기
        player.draw_Characters(gamepad)

        pygame.display.update()
        clock.tick(20)

    # 초기화 한 PyGame 종료
    pygame.quit()
    quit()
# -->



# 시작
if __name__ == '__main__':
    initGame()