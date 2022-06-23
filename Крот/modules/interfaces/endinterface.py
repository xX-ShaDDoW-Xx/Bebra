import sys
import pygame

def endInterface(screen, end_image_path, your_score, font_path, font_colors, screensize):

    end_image = pygame.image.load(end_image_path)
    font = pygame.font.Font(font_path, 50)

    your_score_text = font.render('Your Score: %s' % your_score, True, font_colors[0]) #подставляем в строку your_score, полученный в процессе выполнения программы 

    your_score_rect = your_score_text.get_rect()
	#screensize[0] - ширина экрана
    your_score_rect.left =(screensize[0] - your_score_rect.width)/2
    your_score_rect.top = 215

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return True
        screen.blit(end_image, (0, 0))
        screen.blit(your_score_text, your_score_rect)
        pygame.display.update()
