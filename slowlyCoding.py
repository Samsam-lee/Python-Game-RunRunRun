import pygame

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512

# <-- initGame() 에서 호출!
def runGame():
    global gamepad, clock

    # 게임 종료를 위한 변수
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gamepad.fill(WHITE)
        pygame.display.update()
        clock.tick(60)

    # 초기화 한 PyGame 종료
    pygame.quit()
# -->

# 게임을 초기화하고 시작하는 함수
def initGame():
    global gamepad, clock

    # pygame 라이브러리 초기화
    # 처음에 항상 pygame.init() 호출 필수
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("PyFlying")

    # FPS 설정을 위해 clock 생성 (runGame에서 사용 -> clock.tick(60) -> 60프레임)
    clock = pygame.time.Clock()
    runGame()



initGame()