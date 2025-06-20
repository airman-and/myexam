import tkinter as tk
from math import sqrt
from cmath import sqrt as csqrt

# —————— STEP #2: Sprite 클래스 ——————
class Sprite:
    def __init__(self, canvas, item):
        self.canvas = canvas       # 캔버스 객체
        self.item = item           # 도형 ID
        self.speedx, self.speedy = 9, 9
        self.x, self.y = 0, 0

    def get_coords(self):
        return self.canvas.coords(self.item)

    def get_position(self):
        x, y = self.canvas.coords(self.item)[:2]
        return x, y

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

    def move(self):
        self.canvas.move(self.item, self.speedx, self.speedy)

    def delete(self):
        self.canvas.delete(self.item)


# —————— STEP #3: Ball 클래스 ——————
class Ball(Sprite):
    def __init__(self, canvas, x, y, radius):
        self.radius = radius
        item = canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill='red'
        )
        super().__init__(canvas, item)
        self.x, self.y = x, y

    def update(self):
        x, y = self.get_position()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        # 벽 충돌
        if x <= 0 or x + 2*self.radius >= w:
            self.speedx *= -1
        if y <= 0:
            self.speedy *= -1

    def collide(self, obj_list):
        if obj_list:
            self.speedy *= -1
        for obj in obj_list:
            if isinstance(obj, Brick):
                obj.handle_collision()


# —————— STEP #4: Paddle 클래스 ——————
class Paddle(Sprite):
    def __init__(self, canvas, x, y):
        self.width, self.height = 100, 20
        item = canvas.create_rectangle(
            x - self.width/2, y - self.height/2,
            x + self.width/2, y + self.height/2,
            fill='white'
        )
        super().__init__(canvas, item)
        self.x, self.y = x, y

    # 좌우 이동
    def move(self, dx, dy=None):
        # dy는 사용하지 않음
        self.x += dx
        self.canvas.move(self.item, dx, 0)


# —————— STEP #5: Brick 클래스 ——————
class Brick(Sprite):
    def __init__(self, canvas, x, y):
        self.width, self.height = 52, 24
        item = canvas.create_rectangle(
            x - self.width/2, y - self.height/2,
            x + self.width/2, y + self.height/2,
            fill='yellow', tags='brick'
        )
        super().__init__(canvas, item)

    def handle_collision(self):
        self.delete()


# —————— STEP #1,6,7,8: 메인 게임 프레임 ——————
class BrickBreaker(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.width, self.height = 640, 480
        self.canvas = tk.Canvas(
            self, bg='blue',
            width=self.width, height=self.height
        )
        self.canvas.pack()
        self.pack()

        # 모든 스프라이트 보관
        self.shapes = {}

        # 패들 생성
        self.paddle = Paddle(self.canvas, self.width/2, self.height - 30)
        self.shapes[self.paddle.item] = self.paddle

        # 공 생성
        self.ball = Ball(self.canvas, self.width/2, self.height/2, 10)

        # 벽돌 여러 개 생성
        for r in range(3):
            for c in range(10):
                brick = Brick(self.canvas,  c*60 + 35, r*30 + 40)
                self.shapes[brick.item] = brick

        # 키 바인딩
        self.canvas.focus_set()
        self.canvas.bind('<Left>',  lambda e: self.paddle.move(-15))
        self.canvas.bind('<Right>', lambda e: self.paddle.move(15))
        self.canvas.bind('<space>', lambda e: self.start())

    def start(self):
        self.game_loop()

    def game_loop(self):
        # 충돌 감지
        coords = self.ball.get_coords()
        items = self.canvas.find_overlapping(*coords)
        objects = [self.shapes[i] for i in items if i in self.shapes]

        self.ball.collide(objects)
        self.ball.update()
        self.ball.move()

        # 바닥에 떨어지면 게임 오버
        _, y = self.ball.get_position()
        if y > self.height:
            self.canvas.create_text(
                self.width/2, self.height/2,
                text="Game Over", fill="white", font=("Arial", 24)
            )
            return

        self.after(50, self.game_loop)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Brick Breaker")
    game = BrickBreaker(window)
    window.mainloop()
