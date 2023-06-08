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
    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 150:
            self.rect.y += self.speed            


width = 600
height = 500


window = display.set_mode((width,height))
display.set_caption('Пинге понге')


img_back = "background.jpg"
background = transform.scale(image.load(img_back), (width,height))
finish = False

game = True

font.init()
font1 = font.SysFont("Arial", 36)
font2 = font.SysFont("Arial", 20)
lose_1 = font1.render('Win player 2', True, (180, 0, 0))
lose_2 = font1.render('Win player 1', True, (180, 0, 0))


clock = time.Clock()
FPS = 60


racket_1 = Player("racket.png",30 ,200 ,4 ,50 , 150)
racket_2 = Player("racket.png",520 ,200 ,4 ,50 , 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
score_1 = 0
score_2 = 0
ball_x = 3
ball_y = 3

while game:
       
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))        
        text_1 = font2.render('Счёт 1 игрока: ' + str(score_1), True, (0,0,0))
        window.blit(text_1, (10, 10))

        text_2 = font2.render('Счёт 2 игрока: ' + str(score_2), True, (1, 0, 0)) 
        window.blit(text_2, (440, 10))
        racket_1.update_l()
        racket_2.update_r()

        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(racket_1, ball) :
            ball_x *= -1
            ball_x += 0.3
            if ball_y > 0:
                ball_y += 0.3
            else:
                ball_y -=0.3  
        if sprite.collide_rect(racket_2, ball) :
            ball_x *= -1
            ball_x -= 0.3
            if ball_y > 0:
                ball_y += 0.3
            else:
                ball_y -=0.3  
        if ball.rect.y < 0 or ball.rect.y > height - 50:
            ball_y *= -1
            
        if ball.rect.x < 0 :
            window.blit(lose_1,(200, 250))
            finish = True
            score_2 += 1
        if ball.rect.x > width - 50 :
            window.blit(lose_2,(200, 250))
            finish = True
            score_1 += 1
        racket_1.reset()
        racket_2.reset()
        ball.reset()
    else:
        finish = False
        time.delay(3000)
        racket_1 = Player("racket.png",30 ,200 ,4 ,50 , 150)
        racket_2 = Player("racket.png",520 ,200 ,4 ,50 , 150)
        ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
        ball_x = 3
        ball_y = 3

    display.update()
    clock.tick(FPS)
