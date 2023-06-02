from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self,image_file, x, y, speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))   


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < width - 85:
            self.rect.x += self.speed


width = 700
height = 500


window = display.set_mode((width,height))
display.set_caption('Пинге понге')


back = (200, 255, 255)
window.fill(back)

finish = False

game = True

font.init()
font1 = font.SysFont("Arial", 36)
lose_1 = font1.render('Lose player 1', True, (180, 0, 0))
lose_2 = font1.render('Lose player 2', True, (180, 0, 0))


clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)   