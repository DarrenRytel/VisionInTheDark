from screen_settings import *
from player_class import *
from map_genreator import *



def vision_mechanic(player_x, player_y, fog_radius):

    display = (screen_width, screen_height)

    screen.blit(map_image, (0, 0))
    fog_of_war = pygame.Surface(display)

    pygame.draw.circle(fog_of_war, (60, 60, 60), (player_x, player_y), fog_radius, 0)
    fog_of_war.set_colorkey((60, 60, 60))
    screen.blit(fog_of_war, (0, 0))

''''
def fog_fill(fog_radius, player_x, player_y):

        fog_radius == 128
        display = (screen_width, screen_height)

        screen.blit(map_image, (0, 0))
        fog_fill_up = pygame.Surface(display)

        pygame.draw.circle(fog_fill_up, (0, 0, 0), (player_x, player_y), fog_radius, 0)
        screen.blit(fog_fill_up, (0, 0))

'''
