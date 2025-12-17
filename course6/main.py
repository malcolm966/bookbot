import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from pygame import Surface
from pygame.time import Clock
from player import Player

def init_game() -> Surface:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def init_clock() -> tuple[Clock,float]:
    clock = pygame.time.Clock()
    dt = 0.0
    return clock, dt

def init_game_loop(screen:Surface, clock: Clock, dt:float):
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(f'updated dt: {dt}') 


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT }')
    screen = init_game()
    clock,dt = init_clock()
    init_game_loop(screen, clock, dt)



if __name__ == "__main__":
    main()
