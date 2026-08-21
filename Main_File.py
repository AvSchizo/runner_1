import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
testFont = pygame.font.Font("fonts/LinuxLibertineCapitals-YOpa.ttf", 50)

skySurface = pygame.Surface((screen.get_width(), screen.get_height()))
skySurface.fill("White")
groundSurface = pygame.image.load('graphics/Ground.png').convert_alpha()
textSurface = testFont.render('bla', True, 'Black')

bird_surface = pygame.image.load('graphics/GMTK_tutorial_bird.png').convert_alpha()
bird_surface = bird_surface.subsurface(bird_surface.get_bounding_rect())
birdScale = 5
bird_surface = pygame.transform.scale(bird_surface, (bird_surface.get_width()/birdScale, bird_surface.get_height()/birdScale))
bird_surface = pygame.transform.flip(bird_surface, True, False)
bird_bottom = bird_surface.get_rect(bottom = 350)[1]
bird_pos_x = 800

player_surface = pygame.image.load('graphics/V-2.png').convert_alpha()
player_surface = player_surface.subsurface(player_surface.get_bounding_rect())
playerScale = 10
player_surface = pygame.transform.scale(player_surface, (16*playerScale, 9*playerScale))
player_rectangle = player_surface.get_rect(bottomleft = (80, 350))

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			exit()


	if bird_pos_x < 0-bird_surface.get_width():
		bird_pos_x = 800
	else:
		bird_pos_x -= 4
	

	screen.blit(skySurface, (0, 0))
	screen.blit(groundSurface, (0, screen.get_height()-groundSurface.get_height()))

	screen.blit(textSurface, (300, 50))

	screen.blit(bird_surface, (bird_pos_x, bird_bottom))
	screen.blit(player_surface, player_rectangle)

	pygame.display.update()

	clock.tick(60)