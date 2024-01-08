import pygame
import psutil
import random
# while True:
#     print('cpu usage:', psutil.cpu_percent())
#     print('memory usage:', psutil.virtual_memory()[2])


# import GPUtil as GPU

# GPU.showUtilization()
# GPUs = GPU.getGPUs()
# for gpu in GPUs:
#     print(gpu.memoryUsed)
#     print(gpu.memoryUtil)
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
FPS = 60
score = 0
my_clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font72 = pygame.font.Font("assets/font.otf",72)
font32 = pygame.font.Font("assets/font.otf",32)
welcome_text = font72.render("Welcome to my game", True, (156, 10, 190))
welcome_rect = welcome_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
score_text = font32.render(f"score {score}", True, (156, 10, 190))
score_rect = score_text.get_rect(topleft = (0,0))
start_time = pygame.time.get_ticks()
wolf_right_image = pygame.image.load("assets/wolf.png")
wolf_left_image = pygame.transform.flip(wolf_right_image, True, False)
wolf_image = wolf_right_image
wolf_rect = wolf_image.get_rect()
wolf_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
meat_image = pygame.image.load("assets/m.png")
meat_rect = meat_image.get_rect()
meat_rect.topleft = (random.randint(0, SCREEN_WIDTH - meat_image.get_width()), 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        wolf_rect.y -= 5
    if keys[pygame.K_DOWN]:
        wolf_rect.y += 5
    if keys[pygame.K_LEFT]:
        wolf_image = wolf_left_image
        wolf_rect.x -= 5  
    if keys[pygame.K_RIGHT]:
        wolf_image = wolf_right_image
        wolf_rect.x += 5   
    screen.fill((0,0,0))
    if pygame.time.get_ticks() - start_time < 2000:
        screen.blit(welcome_text, welcome_rect)
    else:



        meat_rect.y += 5
        print(meat_rect.y)

        if meat_rect.colliderect(wolf_rect):
            score += meat_rect.y
            meat_rect.topleft = (random.randint(0, SCREEN_WIDTH - meat_image.get_width()), 0)

        score_text = font32.render(f"score {score}", True, (156, 10, 190))
        pygame.draw.line(screen, (0,255, 0), (0, 300), (SCREEN_WIDTH, 300), 4)
        screen.blit(wolf_image, wolf_rect)   
        screen.blit(meat_image, meat_rect)   
        screen.blit(score_text, score_rect)   
    pygame.display.update()
    my_clock.tick(FPS)
