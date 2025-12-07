import pygame
from game.player import Player
from game.questions import get_random_question
from game.config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, BACKGROUND_IMG
from game.gamestate import GameState, GameStateManager
from game.level import create_level1
import os
from game.button import Button

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Castle Adventure")
    
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    game_state_manager = GameStateManager(GameState.MENU)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    level = create_level1(player)
    pending_question = None
    displayed_question = None
    
    background_image = pygame.image.load(BACKGROUND_IMG)
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    answer_button = Button(10, SCREEN_HEIGHT - 50, 200, 40, "Answer Question", small_font)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_state_manager.get_state() == GameState.MENU:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_state_manager.set_state(GameState.PLAYING)
            elif game_state_manager.get_state() == GameState.PLAYING:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if answer_button.is_clicked(event.pos) and pending_question:
                        displayed_question = pending_question
                        pending_question = None
                if event.type == pygame.KEYDOWN and displayed_question and not displayed_question.answered:
                    if pygame.K_1 <= event.key <= pygame.K_4:
                        if displayed_question.check_answer(event.key - pygame.K_1):
                            player.hp += 10
                        else:
                            player.take_damage(10)
                        displayed_question.answered = True
                        displayed_question = None

            elif game_state_manager.get_state() == GameState.GAME_OVER:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    level = create_level1(player)
                    pending_question = None
                    displayed_question = None
                    game_state_manager.set_state(GameState.PLAYING)


        screen.blit(background_image, (0, 0))

        if game_state_manager.get_state() == GameState.MENU:
            title_text = font.render("Castle Adventure", True, WHITE)
            start_text = small_font.render("Press Enter to Start", True, WHITE)
            screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
        
        elif game_state_manager.get_state() == GameState.PLAYING:
            if not displayed_question:
                player.update(SCREEN_WIDTH, SCREEN_HEIGHT)
                level.check_collisions()

            if not pending_question and not displayed_question:
                for trigger in level.question_triggers:
                    if player.rect.colliderect(trigger.rect) and not trigger.triggered:
                        pending_question = trigger.question
                        trigger.triggered = True
                        break
            
            if player.hp <= 0:
                game_state_manager.set_state(GameState.GAME_OVER)

            level.draw(screen)
            player.draw(screen)

            if displayed_question:
                displayed_question.draw(screen)

            if pending_question:
                answer_button.draw(screen)


        elif game_state_manager.get_state() == GameState.GAME_OVER:
            game_over_text = font.render("Game Over", True, WHITE)
            restart_text = small_font.render("Press Enter to Restart", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
