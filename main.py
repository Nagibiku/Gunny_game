import pygame
import math
import random
import json
import os
import time

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

screen_width=1000
screen_height=500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gunny")


def draw_ruler():  #Thước đo lực
    color=(0,255,255)
    font = pygame.font.Font('freesansbold.ttf', 15)
    pygame.draw.rect(screen,color,pygame.Rect(100, 450, 500, 20),1)
    text1 = font.render('0',True, (255,255,0))
    screen.blit(text1, (100,435))
    pygame.draw.line(screen,color,(150,450),(150,470),1)
    text2 = font.render('10',True, (255,255,0))
    screen.blit(text2, (150,435))
    pygame.draw.line(screen,color,(200,450),(200,470),1)
    text3 = font.render('20',True, (255,255,0))
    screen.blit(text3, (200,435))
    pygame.draw.line(screen,color,(250,450),(250,470),1)
    text4 = font.render('30',True, (255,255,0))
    screen.blit(text4, (250,435))
    pygame.draw.line(screen,color,(300,450),(300,470),1)
    text5 = font.render('40',True, (255,255,0))
    screen.blit(text5, (300,435))
    pygame.draw.line(screen,color,(350,450),(350,470),1)
    text6 = font.render('50',True, (255,255,0))
    screen.blit(text6, (350,435))
    pygame.draw.line(screen,color,(400,450),(400,470),1)
    text7 = font.render('60',True, (255,255,0))
    screen.blit(text7, (400,435))
    pygame.draw.line(screen,color,(450,450),(450,470),1)
    text8 = font.render('70',True, (255,255,0))
    screen.blit(text8, (450,435))
    pygame.draw.line(screen,color,(500,450),(500,470),1)
    text9 = font.render('80',True, (255,255,0))
    screen.blit(text9, (500,435))
    pygame.draw.line(screen,color,(550,450),(550,470),1)
    text10 = font.render('90',True, (255,255,0))
    screen.blit(text10, (550,435))

    text11 = font.render('100',True, (255,255,0))
    screen.blit(text11, (600,435))




def start_screen():  #Màn hình start
    font = pygame.font.Font('04B_19__.TTF', 60)
    text_over = font.render("GUNNY GAME",True, (250,191,29))
    textRect_over = text_over.get_rect(center=(500,150))
    screen.blit(text_over, textRect_over)

    font = pygame.font.Font('04B_19__.ttf', 20)
    text_over = font.render("Press Enter to play start!",True, (250,111,18))
    textRect_over = text_over.get_rect(center=(500,330))
    screen.blit(text_over, textRect_over)

    font = pygame.font.Font('freesansbold.ttf', 15)
    guide1 = font.render('Press arrow key (^ or v) to adjust angle.',True, (255,255,255))
    screen.blit(guide1, (360,435))

    guide1 = font.render('Press Space 1st to adjust force.',True, (255,255,255))
    screen.blit(guide1, (360,450))

    guide2 = font.render('Press Space 2nd to fire.',True, (255,255,255))
    screen.blit(guide2, (360,465))

def game_over_screen():  #Màn hình game over
    font = pygame.font.Font('04B_19__.TTF', 60)
    text_over = font.render("Game over",True, (250,250,250))
    textRect_over = text_over.get_rect(center=(500,100))
    screen.blit(text_over, textRect_over)

    font = pygame.font.Font('04B_19__.TTF', 30)
    text_over = font.render("Score: "+str(score),True, (250,250,250))
    textRect_over = text_over.get_rect(center=(500,200))
    screen.blit(text_over, textRect_over)

    font = pygame.font.Font('04B_19__.TTF', 30)
    text_over = font.render("High Score: "+str(high_score),True, (250,250,250))
    textRect_over = text_over.get_rect(center=(500,260))
    screen.blit(text_over, textRect_over)

    font = pygame.font.Font('04B_19__.ttf', 20)
    text_over = font.render("Press Enter to play again!",True, (250,111,18))
    textRect_over = text_over.get_rect(center=(500,330))
    screen.blit(text_over, textRect_over)

def get_high_score(): #Lấy điểm max được lưu
    with open(os.path.dirname(__file__)+'\high_score.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        return json_object["high_score"]
    
def set_high_score(score):  #Lưu điểm max
    data={"high_score": score}
    json_object = json.dumps(data, indent=4)
    with open(os.path.dirname(__file__)+'\high_score.json', "w") as outfile:
        outfile.write(json_object)
    

def generate_wind():  #Tạo lực gió
    return round(random.uniform(-4, 4),1)



class Image():  # class đối tượng


        bg=pygame.image.load('./image/bg.png')
        bg=pygame.transform.scale(bg,(1000,500))

        chr=pygame.image.load('./image/character.png')
        chr=pygame.transform.scale_by(chr,0.1)
        chr_rect=chr.get_rect(center=(100,380))

        goal=pygame.image.load('./image/goal2.png')
        goal=pygame.transform.scale_by(goal,1)
        goal_random=pygame.transform.scale_by(goal,random.uniform(0.1, 0.25))
        goal_rect=goal_random.get_rect(center=(800,370))


        arrow=pygame.image.load('./image/arrow.png')
        arrow=pygame.transform.scale_by(arrow,0.4)
        arrow_rotate=pygame.transform.rotate(arrow,0)
        arrow_rect=arrow_rotate.get_rect()
        arrow_rect.bottomleft=chr_rect.midbottom
        

        bullet=pygame.image.load('./image/bullet.png')
        bullet=pygame.transform.scale_by(bullet,0.05)
        bullet_rect=bullet.get_rect()
        bullet_rect.center=(-100,-100)

        fire=pygame.image.load('./image/explode.png')
        fire=pygame.transform.scale_by(fire,0.15)
        fire_rect=fire.get_rect(center=(-100,-100))

        wind=pygame.image.load('./image/wind.png')
        wind=pygame.transform.scale_by(wind,0.15)
        wind_rect=wind.get_rect(center=(500,130))

        burn=pygame.image.load('./image/fire.png').convert_alpha()
        burn.set_alpha(150)

class Sound():  #class âm thanh
    bg=pygame.mixer.Sound('./sound/bg2.mp3')
    adjust=pygame.mixer.Sound('./sound/adjust.mp3')
    shoot=pygame.mixer.Sound('./sound/shoot.mp3')
    explode=pygame.mixer.Sound('./sound/explode.mp3')
    ready=pygame.mixer.Sound('./sound/ready2.mp3')
    game_over=pygame.mixer.Sound('./sound/game_over.mp3')
    win=pygame.mixer.Sound('./sound/win.mp3')

        


high_score=get_high_score()
score=0
FPS = 60
fpsClock = pygame.time.Clock()
image=Image()
sound=Sound()
angle=0
t=0
g=9.8
vmax=180
vmin=20
v0=vmin
count=0
wind=0
last_v0=vmin
x,y=0,-100
x0,y0=x,y
flag_shoot=False
flag_boom=False
flag_count=False
flag_next=False
flag_game_active=False
game_state="Start"
check_win=None
count_disapear=0
press_key_down=False
press_key_up=False

running=True

def reset_game():  #Reset game
    global x,y,v0,count, flag_boom, flag_shoot, t,x0, y0
    x,y=0,-100
    v0=vmin
    count=0
    flag_shoot=False
    flag_boom=False
    t=0
    x0,y0=x,y
    image.fire_rect.center=x,y
    image.bullet_rect.center=x,y
    image.goal_random=pygame.transform.scale_by(image.goal,random.uniform(0.1, 0.25))
    image.goal_rect=image.goal_random.get_rect(center=(200+random.random()*(900-200), 100+random.random()*(400-100)))

while running:

    if press_key_down and (not flag_shoot):  #giảm góc
        angle-=1
        angle=0 if angle<=0 else angle
        image.arrow_rotate=pygame.transform.rotate(image.arrow,angle)
        image.arrow_rect=image.arrow_rotate.get_rect()
        image.arrow_rect.bottomleft=image.chr_rect.midbottom
        sound.adjust.play()
    if press_key_up and (not flag_shoot):   #tăng góc
        angle+=1
        angle=90 if angle>=90 else angle
        image.arrow_rotate=pygame.transform.rotate(image.arrow,angle)
        image.arrow_rect=image.arrow_rotate.get_rect()
        image.arrow_rect.bottomleft=image.chr_rect.midbottom
        sound.adjust.play()

    for event in pygame.event.get():
        
        if event.type== pygame.QUIT:
            running=False
        if event.type==pygame.KEYUP and (not flag_shoot) and game_state=='Play':
            if event.key ==pygame.K_DOWN:
                press_key_down=False
                press_key_up=False
            elif event.key==pygame.K_UP:
                press_key_down=False
                press_key_up=False
        elif event.type==pygame.KEYDOWN and (not flag_shoot):
            if event.key ==pygame.K_DOWN and game_state=='Play' and (not flag_boom):
                press_key_down=True
                press_key_up=False
                time.sleep(0.1)
            elif event.key==pygame.K_UP and game_state=='Play' and (not flag_boom):
                press_key_down=False
                press_key_up=True
                time.sleep(0.1)
                
            elif event.key==pygame.K_SPACE and game_state=='Play' and (not flag_boom):
                if flag_count:
                    flag_shoot=True
                    flag_count=False
                    sound.ready.stop()
                    sound.shoot.play()
                if flag_shoot==False:
                    flag_count=True
                    count=1
                

            elif event.key==13 or event.key==pygame.K_KP_ENTER:  # phím enter
                if game_state=='Start':
                    wind=generate_wind()
                    game_state='Play'
                elif game_state=='Game over':
                    wind=generate_wind()
                    game_state='Play'
                    reset_game()
                    score=0


    screen.blit(image.bg, (0,0))
    text_design = pygame.font.Font('freesansbold.ttf', 15).render("---Design by IFS---",True, (105,43,255))
    screen.blit(text_design, (860,480))
    if game_state=='Play': #đang chế độ play
        sound.bg.stop()
        screen.blit(image.wind if wind>=0 else pygame.transform.flip(image.wind, True, True), image.wind_rect)
        font = pygame.font.Font('freesansbold.ttf', 15)
        text_wind = font.render("Windy: "+str(wind),True, (100,100,255))
        textRect_wind = text_wind.get_rect(center=(500,100))
        screen.blit(text_wind, textRect_wind)
        if flag_shoot:  #đang bắn
            flag_count=False
            xt=v0*t*math.cos(math.radians(angle))
            x=image.chr_rect.midbottom[0]+xt+(wind*math.sin(math.radians(angle)))*5*t   #ptrình x
            y=image.chr_rect.midbottom[1]-(v0*math.sin(math.radians(angle))*t-0.5*g*t*t) #ptrình y
            # y=image.chr_rect.midbottom[1]-(-g*xt*xt/(2*(v0*math.cos(math.radians(angle)))**2)+xt*math.tan(math.radians(angle)))
            t+=0.05
            last_v0=v0
            
        if y>image.chr_rect.bottom or x>1000 or x<0:  #đạn ra khỏi màn hình hoặc không trúng
            if x>1000:
                x=1200
            elif x<0:
                x=-100


            print("Loose")
            y=image.chr_rect.bottom
            flag_shoot=False
            flag_boom=True
            check_win='Loose'
            
        if pygame.Rect.colliderect(image.bullet_rect,image.goal_rect):  #trúng đạn
            
            print("Win")
            x,y=image.bullet_rect.center
            flag_shoot=False
            flag_boom=True
            check_win='Win'
            
            
        
            
        # tính góc xoay viên đạn khi bay
        if x==x0:
            if -y+y0>0:
                goc_xoay=3.14/2
            else:
                goc_xoay=-3.14/2
        else:
            if x-x0>0:
                goc_xoay=math.atan((-y+y0)/(x-x0))
            else:
                goc_xoay=math.atan((-y+y0)/(x-x0))+3.14
        bullet_rotate=pygame.transform.rotozoom(image.bullet,180*goc_xoay/3.14,1)
        x0=x
        y0=y

        #show các đối tượng
        screen.blit(image.chr, image.chr_rect)
        screen.blit(image.goal_random, image.goal_rect)
        screen.blit(image.arrow_rotate, image.arrow_rect)
        screen.blit(bullet_rotate, image.bullet_rect)
        screen.blit(image.fire, image.fire_rect)
        # pygame.draw.rect(screen,(255,200,200),image.bullet_rect)
        # pygame.draw.rect(screen,(255,200,200),image.goal_rect)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text_score = font.render("Score: "+str(score),True, (200,50,50))
        textRect_score = text_score.get_rect(center=(500,50))
        screen.blit(text_score, textRect_score)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render("Angle: "+str(angle),True, (200,50,50))
        textRect_angle = text.get_rect(center=(image.chr_rect.centerx-5,image.chr_rect.midbottom[1]+15))
        screen.blit(text, textRect_angle)
        if flag_boom:  #Đạn đến đích
            sound.explode.play()
            v0=vmin
            image.fire_rect.center=x,y
            count_disapear+=1
            if check_win=='Loose':  #thua
                if count_disapear>=100:
                    sound.explode.stop()
                    sound.game_over.play()
                    count_disapear=0
                    game_state='Game over'
                    check_win=None
            elif check_win=='Win': #thắng
                burn=pygame.transform.scale(image.burn,image.goal_random.get_size())
                # burn_rect=burn.get_rect(center=)
                screen.blit(burn, image.goal_rect)
                if count_disapear>=100:
                    sound.explode.stop()
                    sound.win.play()
                    wind=generate_wind()
                    count_disapear=0
                    score+=1
                    if score >high_score:
                        high_score=score
                        set_high_score(high_score)
                    reset_game()
                    check_win=None

        image.bullet_rect.center=x,y

        draw_ruler()
        pygame.draw.line(screen,(255,50,50),(102+(last_v0-vmin)*(598-102)/(vmax-vmin),450),(102+(last_v0-vmin)*(598-102)/(vmax-vmin),470),3)  #Lực bắn trước đó
        if flag_count:  #đang đo lực
            v0+=count
            if v0>=vmax:
                count=-1
            if v0<=vmin:
                count=1
            # pygame.draw.rect(screen,(255,200,200),pygame.Rect(102, 452,(v0-vmin)*(598-102)/(vmax-vmin), 16))
            #Vẽ lực có transparent
            shape_surf = pygame.Surface(pygame.Rect(102, 452,(v0-vmin)*(598-102)/(vmax-vmin), 16).size)
            shape_surf.set_alpha(128)
            shape_surf.fill((255,50,50))
            screen.blit(shape_surf, pygame.Rect(102, 452,(v0-vmin)*(598-102)/(vmax-vmin), 16))
            sound.ready.play()

    elif game_state=='Game over':  #chế độ thua
        #game over
        game_over_screen()
        

    else:  #chế độ start
        start_screen()
        sound.bg.play()
        


    pygame.display.update()  #update màn hình
    fpsClock.tick(FPS) #set FPS
    

pygame.quit()
