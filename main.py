import pygame
from sys import exit
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)
font = pygame.font.SysFont("monospace", 20, bold=True)

obstacle_count = 0

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def draw_hud(generation, obstacles):
    gen_text = font.render(f"Generation : {generation}", True, (255, 255, 255))
    obs_text = font.render(f"Obstacles  : {obstacles}",  True, (255, 255, 255))
    config.window.blit(gen_text, (10, config.win_height - 50))
    config.window.blit(obs_text, (10, config.win_height - 26))

def main():
    global obstacle_count
    pipes_spawn_time = 10

    while True:
        quit_game()

        # Draw background instead of solid fill
        config.window.blit(config.background, (0, 0))

        # Spawn Ground
        config.ground.draw(config.window)

        # Spawn Pipes
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            was_passed = p.passed
            p.update()
            if p.passed and not was_passed:
                obstacle_count += 1
            if p.off_screen:
                config.pipes.remove(p)

        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            obstacle_count = 0
            population.natural_selection()

        draw_hud(population.generation, obstacle_count)

        clock.tick(60)
        pygame.display.flip()

main()
