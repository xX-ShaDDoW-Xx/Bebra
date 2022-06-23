import cfg
import sys
import pygame 
import random 
from modules import * 

srceen = (0, 0)

def initGame():
    
    pygame.init()
    pygame.mixer.init() #инициализировать подключение музыки(модуль mixer)
    pygame.font.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('Поймай бобра') #добавление заголовка окна
    return screen

def main():
    global screen

    # инициализация
    screen = initGame()
    #Загрузить фоновую музыку и другие звуковые эффекты
    # pygame.mixer.music.load(cfg.BGM_PATH)
    # pygame.mixer.music.play(-1)


    # Загрузить шрифт
    
    # Загрузить фоновое изображение
    


    font = pygame.font.Font(cfg.FONT_PATH, 40)
    bg_img = pygame.image.load(cfg.GAME_BG_IMAGEPATH)
    count_down = pygame.mixer.Sound(cfg.COUNT_DOWN_SOUND_PATH)
    hammering = pygame.mixer.Sound(cfg.HAMMERING_SOUND_PATH)




    # Начальный интерфейс
    startInterface(screen, cfg.GAME_BEGIN_IMAGEPATHS)
    #Время смены положения бобра
    hole_pos = random.choice(cfg.HOLE_POSITIONS)
    change_hole_event = pygame.USEREVENT
    pygame.time.set_timer(change_hole_event, 800)
    # бобёр
    mole = Mole(cfg.MOLE_IMAGEPATHS, hole_pos)
    # молоток
    hammer = Hammer(cfg.HAMMER_IMAGEPATHS, (500, 250))
    # таймер
    clock = pygame.time.Clock()
    # счёт
    your_score = 0
    check = False # дополнительная проверка
    # Начальное время
    init_time = pygame.time.get_ticks()



    while True:
        # Игровое время 60сек
        time_remain = round((61000 - (pygame.time.get_ticks() - init_time)) / 1000.)

        if time_remain == 40 and not check:
            hole_pos = random.choice(cfg.HOLE_POSITIONS)
            mole.reset()
            mole.setPosition(hole_pos)
            pygame.time.set_timer(change_hole_event, 650)
            check = True
        elif time_remain == 20 and check:
            hole_pos = random.choice(cfg.HOLE_POSITIONS)
            mole.reset()
            mole.setPosition(hole_pos)
            pygame.time.set_timer(change_hole_event, 500)
            check = False


            
        if time_remain == 10:
            count_down.play()
            # --игра окончена
        if time_remain < 0: 
            break
        count_down_text = font.render('Time: '+str(time_remain), True, cfg.WHITE)


        for event in pygame.event.get():
        # кнопка выход из игры и закрытие интерпретатора
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # движение молотка за мышью
            elif event.type == pygame.MOUSEMOTION:
                hammer.setPosition(pygame.mouse.get_pos())
        # смена костюма молотка при нажатии мышки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == True:
                    hammer.setHammering()
        # перемещение бобра в разные норы
            elif event.type == change_hole_event:
                hole_pos = random.choice(cfg.HOLE_POSITIONS)
                mole.reset()
                mole.setPosition(hole_pos)


        # --Проверка на удар
        if hammer.is_hammering and not mole.is_hammer:#молот ударил и is_hammer != True
            is_hammer = pygame.sprite.collide_mask(hammer, mole)#проверка на столкновение
            if is_hammer:
                hammering.play() #музыка
                mole.setBeHammered()
                your_score += 10
    # --счёт
        your_score_text = font.render('Score: '+str(your_score), True, cfg.BROWN)

        
        screen.blit(bg_img, (0, 0))
        screen.blit(count_down_text, (875, 8))
        screen.blit(your_score_text, (800, 430))
        mole.draw(screen)
        hammer.draw(screen)
    # --Обновление
        pygame.display.flip()



    is_restart = endInterface(screen, cfg.GAME_END_IMAGEPATH, your_score, cfg.FONT_PATH, [cfg.WHITE, cfg.RED], cfg.SCREENSIZE)
    return is_restart




if __name__ == '__main__':
    while True:
        is_restart = main()
        if not is_restart:
            break