
import pygame#library for creating video games
import sys
import random
import math
pygame.init()#initialzing pygame modules
#colours
BLACK=(0,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
WHITE=(255,255,255)
RED=(255,0,0)
PINK=(255,192,203)
CYAN=(0,255,255)
ORANGE=(255,165,0)
#screen dimensions IN PIXELS
SCREEN_WIDTH=600
SCREEN_HEIGHT=650
CELL_SIZE=40
#GRID DIMENSIONS
GRID_WIDTH=15
GRID_HEIGHT=15
#GAME STATES
PLAYING=0
GAME_OVER=1
#GLOBAL GAME STATE
game_state=PLAYING
#CREATING THE SCREEN OR GAME WINDOW
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("PacMan")
#font for score
font=pygame.font.Font(None,36)
#game grid which is a 2D list in python
#1 marks the position of boundary, while 0 is where pacman can move
grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,1,0,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,1,0,1,0,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,1,1,0,1,0,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
#a dictionary is created that stores position and direction of pacman
pacman={
    'x':1,'y':1,'direction':3, #0: right,1:down,2:left,3:up
    'mouth_open':False
    }
#a list that contains a dictionary of ghosts
ghosts=[
    {'x':1,'y':13,'color':RED},#2nd column and 14th row
    {'x':13,'y':1,'color':PINK},
    {'x':13,'y':13,'color':CYAN},
    {'x':11,'y':11,'color':ORANGE}
    ]
#initializing score which will be updated later
score=0
# game loop which is the core of game
clock=pygame.time.Clock()#creates a clock object that controls the frame rate of game
running=True#used as a flag while running the game
#movement delays(how frequently each can move)
pacman_move_delay=150#pacman can approximately move every 150 milliseconds
ghost_move_delay=300
mouth_anim_delay=600
#timing variables
last_pacman_move_time=0
last_ghost_move_time=0
last_mouth_anim_time=0
#function to handle movement logic for pacman
def move_pacman():
    global score
    dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][pacman['direction']]#four possible directions
    new_x,new_y=pacman['x']+dx,pacman['y']+dy
    if grid[new_y][new_x]!=1:#pacman moves if it is not a boundary
        pacman['x'],pacman['y']=new_x,new_y
        if grid[new_y][new_x]==0:
            grid[new_y][new_x]=2#mark for eaten
            score+=10
#function to handle movement logic for pacman
def move_ghost(ghost):
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    random.shuffle(directions)#randomly shuffles the list of directions
    for dx,dy in directions:
        new_x,new_y=ghost['x']+dx,ghost['y']+dy
        #ensures that pacman doesnt move into the walls
        if 0<=new_x<GRID_WIDTH and 0<=new_y<GRID_HEIGHT and grid[new_y][new_x]!=1:
            ghost['x'],ghost['y']=new_x,new_y
            break
def draw_pacman():
    #converts pacman's grid position on screen into pixel coordinates
    x=pacman['x']*CELL_SIZE+CELL_SIZE//2
    y=pacman['y']*CELL_SIZE+CELL_SIZE//2+50
    #mouth opening angles varies from 0(fully closed) and 45(fully opened)
    mouth_opening=45 if pacman['mouth_open']else 0
    #Draw Pacman as a circle
    pygame.draw.circle(screen,YELLOW,(x,y),CELL_SIZE//2)
    #calculate the angles for the mouth based on directions
    if pacman['direction']==0:#Right
        start_angle=360-mouth_opening/2
        end_angle=mouth_opening/2
    elif pacman['direction']==3:#Down
        start_angle=90-mouth_opening/2
        end_angle=90+mouth_opening/2
    elif pacman['direction']==2:#Left
        start_angle=180-mouth_opening/2
        end_angle=180+mouth_opening/2
    else:#Up
        start_angle=270-mouth_opening/2
        end_angle=270+mouth_opening/2
    #Draw the mouth using a pie shape
    pygame.draw.arc(screen,BLACK,(x-CELL_SIZE//2,y-CELL_SIZE//2,CELL_SIZE,CELL_SIZE),
                    math.radians(start_angle),math.radians(end_angle),CELL_SIZE//2)
    #Draw a line from center to create the "slice" effect
    mouth_line_end_x=x+math.cos(math.radians(start_angle))*CELL_SIZE//2
    mouth_line_end_y=y-math.sin(math.radians(start_angle))*CELL_SIZE//2
    pygame.draw.line(screen,BLACK,(x,y),(mouth_line_end_x,mouth_line_end_y),2)
    mouth_line_end_x=x+math.cos(math.radians(end_angle))*CELL_SIZE//2
    mouth_line_end_y=y-math.sin(math.radians(end_angle))*CELL_SIZE//2
    pygame.draw.line(screen,BLACK,(x,y),(mouth_line_end_x,mouth_line_end_y),2)
def draw_ghost(ghost):
    x=ghost['x']*CELL_SIZE+CELL_SIZE//2
    y=ghost['y']*CELL_SIZE+CELL_SIZE//2+50
    pygame.draw.circle(screen,ghost['color'],(x,y),CELL_SIZE//2)
#function to reset the game
def reset_game():
    global pacman,ghosts,score,grid,game_state
    pacman={'x':1,'y':1,'direction':3,
    'mouth_open':False}
    ghosts=[
    {'x':1,'y':13,'color':RED},#2nd column and 14th row
    {'x':13,'y':1,'color':PINK},
    {'x':13,'y':13,'color':CYAN},
    {'x':11,'y':11,'color':ORANGE}
    ]
    score=0
    grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,0,1,0,1,0,1,0,1,1,1,1],
    [1,1,1,1,0,1,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,1,0,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    game_state=PLAYING
def draw_game_over():
    screen.fill(BLACK)
    game_over_font=pygame.font.Font(None,64)
    score_font=pygame.font.Font(None,48)
    restart_font=pygame.font.Font(None,36)

    game_over_text=game_over_font.render("GAME OVER",True,RED)
    score_text=score_font.render(f"Score:{score}",True,WHITE)
    restart_text=restart_font.render("Press SPACE to restart",True,YELLOW)

    screen.blit(game_over_text,(SCREEN_WIDTH//2-game_over_text.get_width()//2,SCREEN_HEIGHT//3))
    screen.blit(score_text,(SCREEN_WIDTH//2-score_text.get_width()//2,SCREEN_HEIGHT//2))
    screen.blit(restart_text,(SCREEN_WIDTH//2-restart_text.get_width()//2,2*SCREEN_HEIGHT//3))
#main game loop
running=True
clock=pygame.time.Clock()
while running:
    current_time=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if game_state==PLAYING:
                if event.key==pygame.K_UP:
                    pacman['direction']=3
                elif event.key==pygame.K_DOWN:
                    pacman['direction']=1
                elif event.key==pygame.K_LEFT:
                    pacman['direction']=2
                elif event.key==pygame.K_RIGHT:
                    pacman['direction']=0
            elif game_state==GAME_OVER:
                if event.key==pygame.K_SPACE:
                    reset_game()
    if game_state==PLAYING:
        #move pacman only if enough time has passed
        if current_time-last_pacman_move_time>pacman_move_delay:
            move_pacman()
            last_pacman_move_time=current_time
        #move ghosts only if enough time has passed
        if current_time-last_ghost_move_time>ghost_move_delay:
            for ghost in ghosts:
                move_ghost(ghost)
            last_ghost_move_time=current_time
        #animate pacman's mouth
        if current_time-last_mouth_anim_time>mouth_anim_delay:
            pacman['mouth_open']=not pacman['mouth_open']
            last_mouth_anim_time=current_time
        #clear screen
        screen.fill(BLACK)
        #Draw maze and dots
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if grid[y][x]==1:
                    pygame.draw.rect(screen,BLUE,(x*CELL_SIZE,y*CELL_SIZE+50,CELL_SIZE,CELL_SIZE))
                elif grid[y][x]==0:
                    pygame.draw.circle(screen,YELLOW,(x*CELL_SIZE+CELL_SIZE//2,y*CELL_SIZE+CELL_SIZE//2+50),3)
        draw_pacman()
        for ghost in ghosts:
            draw_ghost(ghost)
        #display scores
        score_text=font.render(f"score:{score}",True,WHITE)
        screen.blit(score_text,(10,10))
        #check for collisions with ghosts
        for ghost in ghosts:
            if pacman['x']==ghost['x'] and pacman['y']==ghost['y']:
                game_state=GAME_OVER
    elif game_state==GAME_OVER:
        draw_game_over()
    #update display
    pygame.display.flip()
    #cap the frame rate
    clock.tick(60)
pygame.quit()
sys.exit()