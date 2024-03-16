def game_over_assets():
    go_assets = pygame.image.load(resource_path('assets/sprites/gameover.png'))
    return go_assets

def ground_assets():

    ground = pygame.image.load(resource_path('assets/sprites/base.png'))

    return ground

def wall_assets():

    wall_green = pygame.image.load(resource_path('assets/sprites/pipe-green.png'))
    wall_red = pygame.image.load(resource_path('assets/sprites/pipe-red.png'))

    return wall_red, wall_green


def bird_assets():

    bird_blue = {'down': resource_path('assets/sprites/bluebird-downflap.png'),
                 'mid': resource_path('assets/sprites/bluebird-midflap.png'),
                 'up': resource_path('assets/sprites/bluebird-upflap.png')}
    red_bird = {'down': resource_path('assets/sprites/redbird-downflap.png'),
                'mid': resource_path('assets/sprites/redbird-midflap.png'),
                'up': resource_path('assets/sprites/redbird-upflap.png')}
    yellow_bird = {'down': resource_path('assets/sprites/yellowbird-downflap.png'),
                   'mid': resource_path('assets/sprites/yellowbird-midflap.png'),
                   'up': resource_path('assets/sprites/yellowbird-upflap.png')}

    return bird_blue, red_bird, yellow_bird

def backgrounds():

    day_bg = pygame.image.load(resource_path('assets/sprites/background-day.png'))
    night_bg = pygame.image.load(resource_path('assets/sprites/background-night.png'))

    return day_bg, night_bg