from pico2d import *
import random


# Game object class here

boy = grass = team = zombie = ball = None
world = []
running = True

# 게임 객체를 파악.
# boy, grass가 필요하다.
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100, 700)
        self.y = 85
        self.frame = 0
        self.speed = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.speed = random.randint(1, 10)
        self.x += self.speed * 5
        if self.x > 800:
            self.x = 0

class Zombie:
    def __init__(self):
        self.image = load_image('zombie_run_animation.png')
        self.x = random.randint(100, 700)
        self.y = 85
        self.frame = 0
        self.speed = 1

    def draw(self):
        zombie_frame_width = self.image.w // 10
        zombie_frame_height = self.image.h
        self.image.clip_draw(self.frame * zombie_frame_width, 0, zombie_frame_width, zombie_frame_height, self.x, self.y, 80, 80)

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.speed = random.randint(1, 10)
        self.x += self.speed * 2
        if self.x > 800:
            self.x = 0

class ball:
    pass
        

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass, team, zombie, world
    running = True

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world.extend(team)

    zombie = [Zombie() for j in range(3)]
    world.extend(zombie)
   

def update_world():
    for obj in world:
        obj.update()
    

def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()

open_canvas()

# 초기화 코드
reset_world()

# 게임 루프 코드
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# 종료 코드


close_canvas()
