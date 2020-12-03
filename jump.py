import pygame
class Characters:
    
    
    def __init__(self, VELOCITY, MASS):
        self.image = ""
        self.dx = 0
        self.dy = 0
        self.rect = ""  # 이미지 사각형 이미지 크기와 같은 사각형 객체 만들기
        self.isJump = 0
        self.twoJumpNo = 0  # 뛰다_바꾸다
        self.v = VELOCITY  # 속도
        self.m = MASS  # 질량

    def load_image(self, image, pad_width, pad_height):
        # 플레이어 캐릭터
        self.image = pygame.image.load(image)
        # 크기 지정
        self.image = pygame.transform.scale(self.image, (90, 120))
        self.rect = self.image.get_rect()
        self.rect.centerx = pad_width / 5 
        self.rect.bottom = pad_height 

    # 그림 바꿔주기 함수
    def chan_image(self, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (90, 120))

    # 점프 상태 확인하는 메서드
    def jump(self, j):
        self.isJump = j

    '''update'''

    def update(self, VELOCITY, pad_height):
        f = 0.6;
        # isJump 값이 0보다 큰지 확인
        if self.isJump > 0:
            # isJump 값이 2일 경우 속도를 리셋
            # 점프 한 상태에서 다시 점프를 위한 값

            # 이 코드를 주석처리하면 이중점프를 못한다.
            if self.isJump == 2:
                self.v = VELOCITY

            # 역학공식 계산 (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                F = (f * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                F = -(f * self.m * (self.v * self.v))

            # 좌표 수정 : 위로 올라가기 위해서는 y 좌표를 줄여준다.
            self.rect.y -= round(F)

            # 속도 줄여줌
            self.v -= 1

            # 바닥에 닿았을때, 변수 리셋
            if self.rect.bottom > pad_height:
                self.rect.bottom = pad_height
                self.isJump = 0  # 점프 판단
                self.twoJumpNo = 0  # 점프 2단 이상 막기
                self.v = VELOCITY

    '''update'''

    # 스크린에 그리기
    def draw_Characters(self, gamepad):
        gamepad.blit(self.image, [self.rect.x, self.rect.y])  # 이미지 복사해서 넣기