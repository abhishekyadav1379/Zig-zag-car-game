import pygame 
import random
import os 

pygame.mixer.init()
pygame.init()                            # Created by : Abhishek Yadav

# window
win_width = 400
win_hei = 600
window = pygame.display.set_mode((win_width,win_hei))
font = pygame.font.SysFont(None, 28)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x,y])

#Background Image
bgimg = pygame.image.load("background1.jpg")
bgimg = pygame.transform.scale(bgimg, (win_width, win_hei)).convert_alpha()
bgimg2 = pygame.transform.scale(bgimg, (win_width,win_hei)).convert_alpha()

menuimg = pygame.image.load("menu.png")
menuimg = pygame.transform.scale(menuimg, (win_width, win_hei)).convert_alpha()

gameoverimg = pygame.image.load("game_over.png")
gameoverimg = pygame.transform.scale(gameoverimg, (win_width, win_hei)).convert_alpha()

highscoreimg = pygame.image.load("highscoreimg.png")
highscoreimg = pygame.transform.scale(highscoreimg, (win_width, win_hei)).convert_alpha()

# Game image
car2img = pygame.image.load("newcar.png")
car2img = pygame.transform.scale(car2img, (40, 60)).convert_alpha()


rock4 = pygame.image.load("rock4.png")
rock4 = pygame.transform.scale(rock4, (60, 60)).convert_alpha()
rock5 = pygame.image.load("rock5.jpg")
rock5 = pygame.transform.scale(rock5, (70, 60)).convert_alpha()

# colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
fade_blue = (101,140,187)

# Game Title :
pygame.display.set_caption("Zig_zag_car")
window.fill(fade_blue)
pygame.display.update()

# game clock
fps = 30
clock = pygame.time.Clock()

# Menu
def menu():
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    exit_game = True
                    gameloop()

                if event.key == pygame.K_e:
                    exit_game = True

        window.blit(menuimg, (0, 0))
        pygame.display.update()
        clock.tick(fps)


# Game Over
def gameover(score, highscore):
    print(score)
    pygame.mixer.music.load('car_crash.mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exit_game = True
                    gameloop()

                if event.key == pygame.K_RETURN:
                    exit_game = True
                    menu()

        window.blit(gameoverimg, (0, 0))
        text_screen(str(score) , black, 220, 288)
        text_screen(str(highscore), black, 220, 330)
        pygame.display.update()
        clock.tick(fps)


def gameloop():
    
    pygame.mixer.music.load('formula1.mp3')
    pygame.mixer.music.play()
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = int(f.read())

    #  game variable : 
    fps = 30

    fps_score = 0
    block = True
    position = [80,260]
    rock_se = [rock4, rock5]
    rockchoice = random.choice(rock_se)
    (rc1, rc2, rc3, rc4) = (random.choice(rock_se), random.choice(rock_se), random.choice(rock_se), random.choice(rock_se))
    
    (linex1, linex2, linex3, linex4) = (90, 120, 280, 310)
    (liney1, liney2, liney3, liney4, liney5) = (0, 150, 300, 450, 560)
    liney = 600
    score = 0
    blast = 460
    rock_speed = 5
    (a, b, c, d) = (random.choice(position), random.choice(position), random.choice(position), random.choice(position))
    exit_game = False 
    (rock_y, rock_y2, rock_y3, rock_y4) = (0, -150, -300, -450)
    (rock_y_speed, rock_y2_speed, rock_y3_speed, rock_y4_speed) = (rock_speed, rock_speed, rock_speed, rock_speed)               
    # m = 0
    # Game loop
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    block = False

                if event.key == pygame.K_LEFT:               # Created by : Abhishek Yadav
                    block = True
            
        if rock_y > 600:
            score += 10
            rock_y = 0
            rc1 = random.choice(rock_se)
            a = random.choice(position)
        
        if rock_y2 > 600:
            score += 10
            rock_y2 = 0
            rc2 = random.choice(rock_se)
            b = random.choice(position)
        
        if rock_y3 > 600:
            score += 10
            rock_y3 = 0
            rc3 = random.choice(rock_se)
            c = random.choice(position)

        if rock_y4 > 600:
            score += 10
            rock_y4 = 0
            rc4 = random.choice(rock_se)
            d = random.choice(position)

                
        
        liney1 += 10
        liney2 += 10
        liney3 += 10
        liney4 += 10
        liney5 += 10

        rock_y += rock_y_speed   
        rock_y2 += rock_y2_speed
        rock_y3 += rock_y3_speed
        rock_y4 += rock_y4_speed                            # Created by : Abhishek Yadav

        if liney1>600:
            liney1 = -70
        
        if liney2>600:
            liney2 = -70

        if liney3>600:
            liney3 = -70

        if liney4>600:
            liney4 = -70
        
        if liney5>600:
            liney5 = -70

        # window.fill(fade_blue)
        window.fill(fade_blue)
        window.blit(bgimg, (0,0))

        window.blit(bgimg, (0,20))
        
        # window.blit(bgimg, (0, 0))    
        pygame.draw.rect(window, white, [linex1, liney1, 2, 70])
        pygame.draw.rect(window, white, [linex2, liney1, 2, 70])
        pygame.draw.rect(window, white, [linex3, liney1, 2, 70])
        pygame.draw.rect(window, white, [linex4, liney1, 2, 70])

        pygame.draw.rect(window, white, [linex1, liney2, 2, 70])
        pygame.draw.rect(window, white, [linex2, liney2, 2, 70])
        pygame.draw.rect(window, white, [linex3, liney2, 2, 70])
        pygame.draw.rect(window, white, [linex4, liney2, 2, 70])

        pygame.draw.rect(window, white, [linex1, liney3, 2, 70])
        pygame.draw.rect(window, white, [linex2, liney3, 2, 70])
        pygame.draw.rect(window, white, [linex3, liney3, 2, 70])
        pygame.draw.rect(window, white, [linex4, liney3, 2, 70])

        pygame.draw.rect(window, white, [linex1, liney4, 2, 70])
        pygame.draw.rect(window, white, [linex2, liney4, 2, 70])
        pygame.draw.rect(window, white, [linex3, liney4, 2, 70])
        pygame.draw.rect(window, white, [linex4, liney4, 2, 70])

        pygame.draw.rect(window, white, [linex1, liney5, 2, 70])
        pygame.draw.rect(window, white, [linex2, liney5, 2, 70])
        pygame.draw.rect(window, white, [linex3, liney5, 2, 70])
        pygame.draw.rect(window, white, [linex4, liney5, 2, 70])


        window.blit(rc1, (a, rock_y))
        window.blit(rc2, (b, rock_y2))
        window.blit(rc3, (c, rock_y3))
        window.blit(rc4, (d, rock_y4))

        if block == True:
            window.blit(car2img, (85, 500))
        elif block ==False:
            window.blit(car2img, (275, 500))
        
        text_screen("Score", black, 5, 5)
        text_screen(str(score), black, 5,25)
        text_screen("High", black, 347,5)
        text_screen("Score", black,340,25)
        text_screen(str(highscore), black, 350,45)

        if  fps_score < score:
            fps_score += 50
            fps += 5
        
        if  (    (a==80 and block == True and rock_y == blast)
            or (b==80 and block == True and rock_y2 == blast)
            or (c==80 and block == True and rock_y3 == blast)
            or (d==80 and block == True and rock_y4 == blast)
            or (a==260 and block == False and rock_y == blast)
            or (b==260 and block == False and rock_y2 == blast)
            or (c==260 and block == False and rock_y3 == blast)
            or (d==260 and block == False and rock_y4 == blast) ):
                if score > highscore:
                    with open("highscore.txt", "w") as f:
                        f.write(str(score))
                exit_game = True
                gameover(score, highscore)

        pygame.display.update()
        clock.tick(fps)
menu()
pygame.quit()
quit()
