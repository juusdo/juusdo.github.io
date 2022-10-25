# importing libraries
import pygame
import time
import random

# ======================================== #

versio = "1251022"

# ======================================== #


input()

 
snake_speed = 15
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snakes ' + versio)
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()




####

s1_position = [100, 50]

s1_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

s1_score = 0
s1_health = 3
s1_color = green
s1_direction = 'RIGHT'
s1_change_to = s1_direction

###

s2_position = [620, 430]

s2_body = [[620, 430],
              [630, 430],
              [640, 430],
              [650, 430]
              ]

s2_score = 0
s2_health = 3
s2_color = red
s2_direction = 'LEFT'
s2_change_to = s2_direction



####






# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True

 

 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('arial', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(str(s1_score) + " - " + str(s2_score)), True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
    

#######################################################################    




def liikkuminen():
    global s1_change_to, s2_change_to, s1_direction, s2_direction

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                s1_change_to = 'UP'
            if event.key == pygame.K_s:
                s1_change_to = 'DOWN'
            if event.key == pygame.K_a:
                s1_change_to = 'LEFT'
            if event.key == pygame.K_d:
                s1_change_to = 'RIGHT'
                
            if event.key == pygame.K_UP:
                s2_change_to = 'UP'
            if event.key == pygame.K_DOWN:
                s2_change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                s2_change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                s2_change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if s1_change_to == 'UP' and s1_direction != 'DOWN':
        s1_direction = 'UP'
    if s1_change_to == 'DOWN' and s1_direction != 'UP':
        s1_direction = 'DOWN'
    if s1_change_to == 'LEFT' and s1_direction != 'RIGHT':
        s1_direction = 'LEFT'
    if s1_change_to == 'RIGHT' and s1_direction != 'LEFT':
        s1_direction = 'RIGHT'
 
    # Moving the snake
    if s1_direction == 'UP':
        s1_position[1] -= 10
    if s1_direction == 'DOWN':
        s1_position[1] += 10
    if s1_direction == 'LEFT':
        s1_position[0] -= 10
    if s1_direction == 'RIGHT':
        s1_position[0] += 10

      ############ s2 #########



 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if s2_change_to == 'UP' and s2_direction != 'DOWN':
        s2_direction = 'UP'
    if s2_change_to == 'DOWN' and s2_direction != 'UP':
        s2_direction = 'DOWN'
    if s2_change_to == 'LEFT' and s2_direction != 'RIGHT':
        s2_direction = 'LEFT'
    if s2_change_to == 'RIGHT' and s2_direction != 'LEFT':
        s2_direction = 'RIGHT'
 
    # Moving the snake
    if s2_direction == 'UP':
        s2_position[1] -= 10
    if s2_direction == 'DOWN':
        s2_position[1] += 10
    if s2_direction == 'LEFT':
        s2_position[0] -= 10
    if s2_direction == 'RIGHT':
        s2_position[0] += 10
        
def hedelmä():
    global s1_score, s2_score, fruit_position, fruit_spawn

    s1_body.insert(0, list(s1_position))
    if s1_position[0] == fruit_position[0] and s1_position[1] == fruit_position[1]:
        s1_score += 10
        fruit_spawn = False
    else:
        s1_body.pop()
        
        
    s2_body.insert(0, list(s2_position))
    if s2_position[0] == fruit_position[0] and s2_position[1] == fruit_position[1]:
        s2_score += 10
        fruit_spawn = False
    else:
        s2_body.pop()
         
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True

def piirtely():        
    game_window.fill(black)
     
    for pos in s1_body:
        pygame.draw.rect(game_window, blue,
                         pygame.Rect(pos[0], pos[1], 10, 10))
 
    
    for pos in s2_body:
            pygame.draw.rect(game_window, red,
                         pygame.Rect(pos[0], pos[1], 10, 10))
            
            

    pygame.draw.rect(game_window, green, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10)) 
    
    
    
    # creating font object score_font
    score_font = pygame.font.SysFont("arial", 20)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(str(s1_score) + " - " + str(s2_score)), True, white)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
    
    
    
def loppuiko_peli():
    # Game Over conditions
    if s1_position[0] < 0 or s1_position[0] > window_x-10:  # og: -10
        game_over()
    if s1_position[1] < 0 or s1_position[1] > window_y-10:  # og: -10
        game_over()
    if s2_position[0] < 0 or s2_position[0] > window_x-10:  # og: -10
        game_over()
    if s2_position[1] < 0 or s2_position[1] > window_y-10:  # og: -10
        game_over()
 
    # Touching the snake body
    for block in s1_body[1:]:
        if s1_position[0] == block[0] and s1_position[1] == block[1]:
            game_over()
    for block in s2_body[1:]:
        if s1_position[0] == block[0] and s1_position[1] == block[1]:
            game_over()
            
            
    for block in s2_body[1:]:
        if s2_position[0] == block[0] and s2_position[1] == block[1]:
            game_over()
    for block in s1_body[1:]:
        if s2_position[0] == block[0] and s2_position[1] == block[1]:
            game_over()
        
    

 
def peli():
    liikkuminen()
    hedelmä()
    piirtely()
    loppuiko_peli()
    pygame.display.update()
    fps.tick(snake_speed)
    
while True:
    peli()
    
    
