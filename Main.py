import pygame

from Map import import_maps
from GameParameter import clock, fps, fps_menu
from GameEffects import AnimationTransition, load_image

from StartMenu import StartMenu  # импорты экранов
from SelectMenu import SelectMenu
# from CharacterMenu import CharacterMenu
from Game import Game
from PauseMenu import PauseMenu
from ResultScreen import ResultScreen
from Settings import Settings, load_settings

# загрузка настроек, карт
settings_values = load_settings()
closed = False


def start_menu():
    global closed
    if closed:
        return
    # функция для создания, отрисовки стартового меню
    screen = StartMenu()
    game = True
    res = -1  # переменная, возвращающая состояние экрана
    while not transition.get_transition():  # отображение перехода между меню
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                return

        transition.render()
        pygame.display.flip()
        clock.tick(fps)
    screen.render()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                closed = True
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:  # переход в меню выбора карт
                    screen.result = 1
                    pygame.mixer.music.stop()

        if transition.get_transition():  # отображение перехода между меню
            if not transition.background:
                # сохранение изображения на экране для быстрой отрисовки
                pygame.image.save(display, 'image/backgrounds/background_for_load.png')
                transition.background = load_image('backgrounds/background_for_load.png')
            transition.render()
        else:
            screen.render()
        pygame.display.flip()
        clock.tick(fps)
        res = screen.get_result()
        if res != -1:
            game = False
    if res == 1:
        frame = transition.get_frame()  # смена состояния перехода
        if frame != 35 and frame != -1:
            transition.reverse()
        transition.background = None
        select_map()


def select_map():
    # функция отрисовки, создания меню выбора карт
    global closed
    if closed:
        return

    screen = SelectMenu([])
    game = True
    res = -1
    while not transition.get_transition():  # отображение перехода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                return
        transition.render()
        pygame.display.flip()
        clock.tick(fps)
    screen.render()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                closed = True
            if event.type == pygame.MOUSEBUTTONDOWN:  # прокрутка меню
                if event.button == 1:
                    screen.render()

        if transition.get_transition():  # отображение перехода
            if not transition.background:
                pygame.image.save(display, 'image/backgrounds/background_for_load.png')
                transition.background = load_image('backgrounds/background_for_load.png')
            transition.render()
        else:
            screen.render()
        pygame.display.flip()
        clock.tick(fps)

        res = screen.get_result()
        if res != -1:
            game = False
    if res == 1:  # переход в стартовое меню
        frame = transition.get_frame()
        if frame != 35 and frame != -1:
            transition.reverse()
        transition.background = None
        start_menu()
    elif res == 2:  # переход в  меню выбора персонажа
        frame = transition.get_frame()
        if frame != 35 and frame != -1:
            transition.reverse()
        transition.background = None
        # select_character()
    elif res == 3:  # переход к игре
        map = screen.get_map()
        play_map(map)
    elif res == 4:  # переход к настройкам
        frame = transition.get_frame()
        if frame != 35 and frame != -1:
            transition.reverse()
        transition.background = None
        settings()
        select_map()


def settings():
    # функция для отрисовки, создания меню настроек
    global closed
    if closed:
        return
    screen = Settings()
    game = True
    while not transition.get_transition():  # отображение перехода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                return
        transition.render()
        pygame.display.flip()
        clock.tick(fps)
    screen.render()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                return
        if transition.get_transition():  # отображение перехода
            if not transition.background:
                pygame.image.save(display, 'image/backgrounds/background_for_load.png')
                transition.background = load_image('backgrounds/background_for_load.png')
            transition.render()
        else:
            screen.render()
        pygame.display.flip()
        clock.tick(fps)
        res = screen.get_result()
        if res != -1:
            game = False
    if res == 0:  # возврат в функцию select_map
        frame = transition.get_frame()
        if frame != 35 and frame != -1:
            transition.reverse()
        transition.background = None
        return


# def select_character():
#     # меню выбора персонажа
#     global closed
#     if closed:
#         return
#     screen = CharacterMenu()
#
#     game = True
#     res = -1
#
#     while not transition.get_transition():  # отображение перехода
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 closed = True
#                 return
#         transition.render()
#         pygame.display.flip()
#         clock.tick(fps)
#
#     screen.render()
#     while game:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 closed = True
#                 game = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     x, y = event.pos
#                     # обработка смен персонажа
#                     if 200 < x < 300 and 310 < y < 410:
#                         screen.switch_chr(-1)
#                     elif 820 < x < 920 and 310 < y < 410:
#                         screen.switch_chr(1)
#
#         if transition.get_transition():  # отображение перехода
#             if not transition.background:
#                 pygame.image.save(display, 'image/background_for_load.png')
#                 transition.background = load_image('background_for_load.png')
#             transition.render()
#         else:
#             screen.render()
#         pygame.display.flip()
#         res = screen.get_result()
#         if res != -1:
#             game = False
#     if res == 0:
#         # возвращение к экрану select_map
#         frame = transition.get_frame()
#         if frame != 35 and frame != -1:
#             transition.reverse()
#         transition.background = None
#         select_map()


def play_map(map):
    # экран игрового процесса
    global closed
    if closed:
        return
    screen = Game(map)
    game = True
    while game:
        l_mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    l_mouse_click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # обработка выхода в меню паузы
                    screen.pause_music()
                    result = pause(None, screen.map.background)
                    if result == -2:
                        return
                    elif result == 0:
                        screen.time = pygame.time.get_ticks() - screen.time_now
                        screen.unpause_music()
                    elif result == 1:
                        return play_map(map)
                    elif result == 2:
                        transition.background = None
                        return select_map()
                else:
                    screen.handle_keys()  # обработка нажатий на клавиши
        screen.render(l_mouse_click)
        if screen.end_game():
            game = False
        pygame.display.flip()
        clock.tick(fps)
    transition.background = None
    # вызов экрана с результатами игры
    result_game(screen.max_combo, screen.score, screen.count_marks, screen.accuracy, map)


def pause(objects, background):  # экран паузы
    global closed
    if closed:
        return
    screen = PauseMenu(objects, background)
    game = True
    timer = False
    timer_image = [load_image(f'timer_{i}.png') for i in range(1, 4)]
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                return -2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return pause(objects, background)
        if timer:
            screen.render_map()
            time_after_pause = (pygame.time.get_ticks() - time_in_pause) / 1000
            if time_after_pause < 3:
                display.blit(timer_image[-1 * (int(time_after_pause) + 1)], (600, 295))
            else:
                game = False
                timer = False
        else:
            screen.render_pause()
        pygame.display.flip()
        clock.tick(fps)
        res = screen.get_result()
        if res == 0:
            if not timer:
                timer = True
                time_in_pause = pygame.time.get_ticks()
        elif res != -1:
            game = False
    return res


def result_game(count_combo, score, marks, accuracy, map):  # экран с результатом игры
    global closed
    if closed:
        return
    screen = ResultScreen(count_combo, score, marks, accuracy, map)
    game = True

    transition.frame = -1
    transition.transition_back = False
    while not transition.get_transition():  # отрисовка перехода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                return
        transition.render()
        pygame.display.flip()
        clock.tick(fps)

    screen.render()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                game = False
        if transition.get_transition():  # отрисовка перехода
            if not transition.background:
                pygame.image.save(display, 'image/backgrounds/background_for_load.png')
                transition.background = load_image('backgrounds/background_for_load.png')
            transition.render()
        else:
            screen.render()
        pygame.display.flip()
        clock.tick(fps)
        res = screen.get_result()
        if res == 0:  # переход к меню выбора карт
            game = False
            frame = transition.get_frame()
            if frame != 35 and frame != -1:
                transition.reverse()
            transition.background = None
            select_map()
        if res == 1:
            game = False
            play_map(map)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('リズム')
    pygame.display.set_icon(load_image("icon.ico"))
    transition = AnimationTransition()
    size = width, height = 1120, 720
    display = pygame.display.set_mode(size)
    start_menu()
    pygame.quit()
