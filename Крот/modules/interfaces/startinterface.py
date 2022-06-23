import sys
import pygame


def startInterface(screen, begin_image_paths):

	#создаём список для смены изображений
    begin_images = [pygame.image.load(begin_image_paths[0]),       pygame.image.load(begin_image_paths[1])]
	#устанавливем начальное изображение с помощью обращения к элементу списка
    begin_image = begin_images[0]

    while True:
        for event in pygame.event.get():
            #условия выхода из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #условия смены картинки при наведении мышки 
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                #дипазон реагирования мышки в заданных координатах 
                if mouse_pos[False] in list(range(366, 626)) and mouse_pos[True] in list(range(70, 140)):
                    begin_image = begin_images[1]
                else:
                    begin_image = begin_images[0]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == True and mouse_pos[False] in list(range(366, 626)) and mouse_pos[True] in list(range(70, 140)):
                    return True
        screen.blit(begin_image, (0, 0))
        pygame.display.update()
