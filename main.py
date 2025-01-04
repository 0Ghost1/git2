import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    #в эту переменную записываем количество хп чтобы потом отображать в красном квадрате
    count_hp = 2

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        # ...
        font = pygame.font.Font(None, 26)
        text_xp = font.render('XP', True, (255, 255, 255))
        text_counthp = font.render(f'{count_hp} / {3}', True, (255, 255, 255))
        position_rect = (1200 - 300) / 2, (800 - 300) / 2
        pygame.draw.rect(screen, (255, 255, 255), (position_rect[0], position_rect[1] + 50, 300, 300), 1)
        screen.blit(text_xp, (510, 622))
        screen.blit(text_counthp, (610, 622))
        if count_hp == 3:
            pygame.draw.rect(screen, (255, 255, 255), (540, 620, 60, 20))
        elif count_hp == 2:
            pygame.draw.rect(screen, (255, 255, 255), (540, 620, 60, 20))
            pygame.draw.rect(screen, pygame.Color('red'), (580, 620, 20, 20))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (540, 620, 60, 20))
            pygame.draw.rect(screen, pygame.Color('red'), (560, 620, 40, 20))



        # обновление экрана
        pygame.display.flip()
    pygame.quit()