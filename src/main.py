import sys
import pygame
import random

# 初始化Pygame
pygame.init()

# 常量定义
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
COLORS = {
    'bg': (30, 30, 30),
    'tile': (255, 165, 0),
    'text': (255, 255, 255)
}

class PuzzleGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.tiles = []
        self.empty_pos = (3, 3)  # 初始空格位置
        self.init_game()
        
    def init_game(self):
        # 生成可解随机排列
        numbers = list(range(1, 16)) + [0]
        while True:
            random.shuffle(numbers)
            if self.is_solvable(numbers):
                break
                
        # 创建方块矩阵
        self.tiles = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                num = numbers[i*GRID_SIZE + j]
                row.append({
                    'num': num,
                    'rect': pygame.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE-2, TILE_SIZE-2)
                })
            self.tiles.append(row)

    def is_solvable(self, numbers):
        # 实现可解性检查逻辑
        inversions = 0
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] > numbers[j] and numbers[i] != 0 and numbers[j] != 0:
                    inversions +=1
        return inversions % 2 == 0

    def handle_click(self, pos):
        # 转换点击坐标到网格位置
        x, y = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
        
        # 检查相邻性
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if self.tiles[ny][nx]['num'] == 0:
                    # 执行方块移动
                    self.tiles[ny][nx]['num'] = self.tiles[y][x]['num']
                    self.tiles[y][x]['num'] = 0
                    self.empty_pos = (y, x)
                    return True
        return False

    def check_win(self):
        expected = 1
        for row in self.tiles[:3]:
            for tile in row[:4]:
                if tile['num'] != expected:
                    return False
                expected += 1
        return self.tiles[3][3]['num'] == 0

    def draw_grid(self):
        # 绘制所有方块
        for row in self.tiles:
            for tile in row:
                if tile['num'] == 0:
                    continue
                pygame.draw.rect(self.screen, COLORS['tile'], tile['rect'])
                font = pygame.font.Font(None, 40)
                text = font.render(str(tile['num']), True, COLORS['text'])
                text_rect = text.get_rect(center=tile['rect'].center)
                self.screen.blit(text, text_rect)

    def draw_button(self):
        # 绘制Random按钮
        btn = pygame.Rect(100, HEIGHT-80, 200, 50)
        pygame.draw.rect(self.screen, (0, 200, 0), btn)
        font = pygame.font.Font(None, 30)
        text = font.render("Random", True, (255,255,255))
        self.screen.blit(text, (btn.x+50, btn.y+15))
        return btn

    def play_fireworks(self):
        # 简单礼花特效
        for _ in range(20):
            x, y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
            pygame.draw.circle(self.screen, 
                (random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                (x,y), 5)
            pygame.display.update()
            pygame.time.delay(100)

    def run(self):
        running = True
        while running:
            self.screen.fill(COLORS['bg'])
            self.draw_grid()
            btn = self.draw_button()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn.collidepoint(event.pos):
                        self.init_game()
                    else:
                        self.handle_click(event.pos)
            
            if self.check_win():
                self.play_fireworks()
                pygame.time.delay(2000)
                self.init_game()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = PuzzleGame()
    game.run()