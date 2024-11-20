#pip install pygame
import pygame
import random
import time

# 초기화
pygame.init()

# 상수 정의
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * BOARD_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# 테트리스 블록 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("테트리스")
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.reset_piece()

    def reset_piece(self):
        self.current_piece = random.choice(SHAPES)
        self.current_x = BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0
        if not self.is_valid():
            self.game_over()

    def game_over(self):
        print(f"게임 오버! 점수: {self.score}")
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.reset_piece()

    def is_valid(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_x + x
                    new_y = self.current_y + y
                    if (new_x < 0 or new_x >= BOARD_WIDTH or 
                        new_y >= BOARD_HEIGHT or
                        (new_y >= 0 and self.board[new_y][new_x])):
                        return False
        return True

    def freeze_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + y][self.current_x + x] = 1
        self.clear_lines()
        self.reset_piece()

    def clear_lines(self):
        lines_cleared = 0
        for y in range(BOARD_HEIGHT - 1, -1, -1):
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared * 100

    def rotate_piece(self):
        rotated = list(zip(*self.current_piece[::-1]))
        previous = self.current_piece
        self.current_piece = [list(row) for row in rotated]
        if not self.is_valid():
            self.current_piece = previous

    def draw(self):
        self.screen.fill(BLACK)
        
        # 보드 그리기
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, GRAY,
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE,
                                    BLOCK_SIZE - 1, BLOCK_SIZE - 1))

        # 현재 조각 그리기
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, RED,
                                   ((self.current_x + x) * BLOCK_SIZE,
                                    (self.current_y + y) * BLOCK_SIZE,
                                    BLOCK_SIZE - 1, BLOCK_SIZE - 1))

        # 점수 표시
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    def run(self):
        last_drop_time = time.time()
        running = True
        
        while running:
            current_time = time.time()
            
            # 자동 낙하
            if current_time - last_drop_time > 1.0:
                self.current_y += 1
                if not self.is_valid():
                    self.current_y -= 1
                    self.freeze_piece()
                last_drop_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_x -= 1
                        if not self.is_valid():
                            self.current_x += 1
                    elif event.key == pygame.K_RIGHT:
                        self.current_x += 1
                        if not self.is_valid():
                            self.current_x -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_y += 1
                        if not self.is_valid():
                            self.current_y -= 1
                            self.freeze_piece()
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()

            self.draw()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()