import pygame, random

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512
background_width = 1024

#<-- background, character, obstacle
def drawObject(obj, x,y):
    global gamepad
    gamepad.blit(obj, (x,y))
# -->

# <-- initGame() 에서 호출!
def runGame():
    global gamepad, clock, amongus, background1, background2
    global obstacles

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width

    obstacle_x = pad_width
    obstacle_y = random.randrange(0, pad_height)
    random.shuffle(obstacles)
    obstacle = obstacles[0]

    # 게임 종료를 위한 변수
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change

        gamepad.fill(WHITE)

        # 배경 2 씩 이동
        background1_x -= 2
        background2_x -= 2

        # 장애물이 없으면 30씩 이동(시간 지체)
        # 장애물이 있으면 15씩 이동
        if obstacle == None:
            obstacle_x -= 50
        else:
            obstacle_x -= 15

        # 장애물이 다 지나가면 다시 설정
        if obstacle_x <= 0:
            obstacle_x = pad_width
            obstacle_y = random.randrange(0, pad_height)
            random.shuffle(obstacles)
            obstacle = obstacles[0]

        # 배경이 다 지나가면 다시 설정
        if background1_x == -background_width:
            background1_x = background_width
        if background2_x == -background_width:
            background2_x = background_width

        # 화면에 출력
        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)
        if obstacle != None:
            drawObject(obstacle, obstacle_x, obstacle_y)
        drawObject(amongus, x,y)
        pygame.display.update()
        clock.tick(60)

    # 초기화 한 PyGame 종료
    pygame.quit()
    quit()
# -->

# 게임을 초기화하고 시작하는 함수
def initGame():
    global gamepad, clock, amongus, background1, background2
    global obstacles
    obstacles = []

    # pygame 라이브러리 초기화
    # 처음에 항상 pygame.init() 호출 필수
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("PyFlying")
    amongus = pygame.image.load('amongus.png')
    background1 = pygame.image.load('background.jpeg')
    background2 = background1.copy()
    obstacles.append(pygame.image.load('obstacle1.png'))
    obstacles.append(pygame.image.load('obstacle2.png'))

    # 난이도 조절 가능
    for i in range(5):
        obstacles.append(None)

    # FPS 설정을 위해 clock 생성 (runGame에서 사용 -> clock.tick(60) -> 60프레임)
    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__':
    initGame()