import pygame

from sys import exit
# --- functions ---

# --- player1 (W & S)---
def p1_handle_event(event):
    global p1_move_up, p1_move_down

    if event.type == pygame.KEYDOWN:
        if event.key == P1_UP:
            p1_move_up = True
            p1_move_down = False
        elif event.key == P1_DOWN:
            p1_move_down = True
            p1_move_up = False
    elif event.type == pygame.KEYUP:
        if event.key == P1_UP:
            p1_move_up = False
        elif event.key == P1_DOWN:
            p1_move_down = False

def p1_update():
    # do nothing
    pass

# --- player2 (Up & Down)---

def human_handle_event(event):
    global p2_move_up, p2_move_down

    if event.type == pygame.KEYDOWN:
        if event.key == P2_UP:
            p2_move_up = True
            p2_move_down = False
        elif event.key == P2_DOWN:
            p2_move_down = True
            p2_move_up = False
    elif event.type == pygame.KEYUP:
        if event.key == P2_UP:
            p2_move_up = False
        elif event.key == P2_DOWN:
            p2_move_down = False

def human_update():
    # do nothing
    pass


# computer follows ball

def following_handle_event(event):
    # do nothing
    pass

def following_update():
    global p2_move_up, p2_move_down

    if ball_y < p2_pad_y + 50:
        p2_move_up = True
        p2_move_down = False
    elif ball_y > p2_pad_y + 50:
        p2_move_up = False
        p2_move_down = True
    else: # stop        
        p2_move_up = False
        p2_move_down = False

# --- main ---

### initialize game
pygame.init()

### setup display
DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600
screen = pygame.display.set_mode(DISPLAY_SIZE)

### clock
clock = pygame.time.Clock()

### hide cursor
pygame.mouse.set_visible(False)

### game constants
# buttons
P1_UP = pygame.K_w
P1_DOWN = pygame.K_s
P2_UP = pygame.K_UP
P2_DOWN = pygame.K_DOWN

# other constants
PLAYER_PAD_LENGTH = 100
PLAYER_PAD_SPEED = 18
PLAYERbot_PAD_SPEED = 4.5 #Bot Speed
PLAYER_PAD_WIDTH = 10
BALL_RADIUS = 6

### game variables
## player scores
p1_score = 0
p2_score = 0

## ball speed is split into x and y axes
ball_speed_x = 50
ball_speed_y = 50

## ball coordinates
ball_x = 400
ball_y = 300

## player pad y's
p1_pad_y = 300
p2_pad_y = 300

## player move flags
p1_move_up = False
p1_move_down = False
p2_move_up = False
p2_move_down = False

### choose second players
########################################################
p2_type = 'multiplayer'
########################################################

if p2_type == 'single': 
    # computer will follow ball
    p2_handle_event = following_handle_event
    p2_update = following_update
elif p2_type == 'multiplayer':    
    # human will click keys
    p2_handle_event = human_handle_event
    p2_update = human_update

#Loops the game
carryOn = True

### main game loop
while carryOn:
    ## detect and process key events
    # keydowns and keyups raise and lower player move flags
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
              pygame.quit()
              exit()
              
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p: #Pushing P will quit the game
                     carryOn=False
                     pygame.quit()
                     exit()
                     
        elif (p1_score == 5) or (p2_score == 5):
            if p1_score == 5:
                print("Player 1 Wins!")
            elif p2_score == 5:
                print("Player 2 Wins!")
            carryOn = False # Flag that we are done so we exit this loop
            pygame.quit()
            exit()
            
        # get players keys
        p1_handle_event(event)
        p2_handle_event(event)

    # get other changes
    p1_update()
    p2_update()

    ## move player pads according to player move flags
    if p1_move_up:
        p1_pad_y -= PLAYER_PAD_SPEED
        if p1_pad_y < 0:
            p1_pad_y = 0
    elif p1_move_down:
        p1_pad_y += PLAYER_PAD_SPEED
        if p1_pad_y > DISPLAY_HEIGHT - PLAYER_PAD_LENGTH:
            p1_pad_y = DISPLAY_HEIGHT - PLAYER_PAD_LENGTH
   
    if p2_type == 'single':  
        if p2_move_up:
            p2_pad_y -= PLAYERbot_PAD_SPEED
            if p2_pad_y < 0:
                p2_pad_y = 0
        elif p2_move_down:
            p2_pad_y += PLAYERbot_PAD_SPEED
            if p2_pad_y > DISPLAY_HEIGHT - PLAYER_PAD_LENGTH:
                p2_pad_y = DISPLAY_HEIGHT - PLAYER_PAD_LENGTH

    if p2_type == 'multiplayer':  
            if p2_move_up:
                p2_pad_y -= PLAYER_PAD_SPEED
                if p2_pad_y < 0:
                    p2_pad_y = 0
            elif p2_move_down:
                p2_pad_y += PLAYER_PAD_SPEED
                if p2_pad_y > DISPLAY_HEIGHT - PLAYER_PAD_LENGTH:
                    p2_pad_y = DISPLAY_HEIGHT - PLAYER_PAD_LENGTH

    ## move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    ## check ball position
    # if out screen vertically, flip ball_speed_y
    if ball_y < 0 or ball_y > DISPLAY_HEIGHT - BALL_RADIUS:
        ball_speed_y = -ball_speed_y

    # if out screen horizontally, check whether player pad is there or not
    # if not, release the ball at the center towards scoring player
    if ball_x < 0:
        if p1_pad_y < ball_y < p1_pad_y + PLAYER_PAD_LENGTH:
            ball_speed_x = -ball_speed_x
        else:
            p2_score += 1
            ball_x = 400
            ball_y = 300
            ball_speed_x = 5
            ball_speed_y = 5
    elif ball_x > DISPLAY_WIDTH:
        if p2_pad_y < ball_y < p2_pad_y + PLAYER_PAD_LENGTH:
            ball_speed_x = -ball_speed_x
        else:
            p1_score += 1
            ball_x = 400
            ball_y = 300
            ball_speed_x = -5
            ball_speed_y = -5

    ## clear the screen
    screen.fill(pygame.Color(0, 0, 0, 255))

    ## draw ball
    pygame.draw.circle(screen, pygame.Color(255, 255, 255, 255), (ball_x, ball_y), BALL_RADIUS)

    ## draw P1 pad
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (0, p1_pad_y, PLAYER_PAD_WIDTH, PLAYER_PAD_LENGTH))

    ## draw P2 pad
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255),
                     (DISPLAY_WIDTH - PLAYER_PAD_WIDTH, p2_pad_y, PLAYER_PAD_WIDTH, PLAYER_PAD_LENGTH))

    ## draw center line
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (DISPLAY_WIDTH / 2, 0, 1, DISPLAY_HEIGHT))

    ## draw player scores
    # create font
    score_font = pygame.font.Font(None, 30)

    # draw p1 score
    p1_score_text = str(p1_score)
    p1_score_render = score_font.render(p1_score_text, 1, pygame.Color(255, 255, 255, 255))
    screen.blit(p1_score_render, (DISPLAY_WIDTH / 2 - 50, 50))

    # draw p2 score
    p2_score_text = str(p2_score)
    p2_score_render = score_font.render(p2_score_text, 1, pygame.Color(255, 255, 255, 255))
    screen.blit(p2_score_render, (DISPLAY_WIDTH / 2 + 50, 50))

    ## pygame.display.flip() is called in order to update graphics properly
    pygame.display.flip()

    ## tick the clock so we have 60 fps game
    clock.tick(60)
