import pygame

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512

# <--character
def among(x,y):
    global gamepad, amongus
    gamepad.blit(amongus, (x,y))

# <-- initGame() 에서 호출!
def runGame():
    global gamepad, clock, amongus

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

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
        among(x,y)
        pygame.display.update()
        clock.tick(60)

    # 초기화 한 PyGame 종료
    pygame.quit()
    quit()
# -->

# 게임을 초기화하고 시작하는 함수
def initGame():
    global gamepad, clock, amongus

    # pygame 라이브러리 초기화
    # 처음에 항상 pygame.init() 호출 필수
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("PyFlying")
    amongus = pygame.image.load('amongus.png')

    # FPS 설정을 위해 clock 생성 (runGame에서 사용 -> clock.tick(60) -> 60프레임)
    clock = pygame.time.Clock()
    runGame()



initGame()