from pico2d import *
import game_framework


# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.1)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:
    image = None

    def __init__(self):

        Bird.image = load_image('bird_animation.png')
        self.velocity = 10
        self.x, self.y = 1600 // 2, 200
        # Boy is only once created, so instance image loading is fine
        self.frame = 0
        self.timer = 2
        self.RUN_SPEED_PPS = RUN_SPEED_PPS

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.velocity * game_framework.frame_time
        if self.frame == 4:
            self.timer -= 1

        elif self.frame == 3:
            if self.timer == 0:
                self.timer = 2


    def draw(self):
        self.image.clip_draw(int(self.frame) * 183, 168 * self.timer, 183, 168, self.x, self.y)

    def update(self):
        self.x += self.RUN_SPEED_PPS

        if self.x < 25 or self.x > 1600 - 25:
            self.RUN_SPEED_PPS = self.RUN_SPEED_PPS * -1


