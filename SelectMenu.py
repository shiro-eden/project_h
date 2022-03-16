import pygame
import sqlite3
from GameParameter import display, fps
from Button import Button
from GameEffects import drawing_text, load_image
from Settings import load_settings

exit_button_image = [load_image(f'ui/buttons/menu_back_button_{i}.png') for i in range(2)]
chr_button_image = [load_image(f'ui/buttons/chr_button_{i}.png') for i in range(2)]
play_button_image = [load_image(f'ui/buttons/play_button_{i}.png') for i in range(2)]
settings_button_image = [load_image(f'ui/buttons/settings_button_{i}.png') for i in range(2)]
song_rect = load_image('ui/decor/select_menu_rect.png')
song_rect_active = load_image('ui/decor/select_menu_rect_active.png')
menu_back_plus = load_image('ui/decor/menu_down_rect.png')
menu_plus = load_image('ui/decor/menu_up_rect.png')
back_mask = load_image('backgrounds/mask_background.png')
settings_values = load_settings()
glow_left = load_image('ui/decor/glow_left.png')
glow_right = load_image('ui/decor/glow_right.png')
shift_v = 300

background_image = load_image('backgrounds/menu_background.png')


class SelectMenu:
    def __init__(self, maps):
        settings_values = load_settings()
        self.result = -1  # переменная для отслеживания состояния экрана

        self.maps = maps
        # создание кнопок
        self.exit_btn = Button(-30, 615, 222, 92, '', exit_button_image, self.back,
                               glow=glow_left)

        self.chr_btn = Button(-30, -30, 223, 92, '', chr_button_image, self.chr_menu,
                              glow=glow_left)

        self.play_btn = Button(908, 650, 222, 92, '', play_button_image, self.start_game,
                               glow=glow_right)

        self.settings_btn = Button(908, 0, 223, 92, '', settings_button_image, self.open_settings,
                                   glow=glow_right)
        self.active_map = 0
        self.menu_background = background_image

    def back(self):
        self.result = 1

    def chr_menu(self):
        self.result = 2

    def start_game(self):
        self.result = 3

    def open_settings(self):
        self.result = 4

    def get_result(self):
        return self.result

    def get_map(self):
        return None

    def render(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display.blit(self.menu_background, (0, 0))
        display.blit(back_mask, (0, 0))
        display.blit(song_rect, (400, 400))
        # отрисовка кнопок, полосок меню
        display.blit(menu_back_plus, (0, 620))
        display.blit(menu_plus, (0, 0))
        self.play_btn.draw(0, 0)
        self.exit_btn.draw(0, 0)
        self.play_btn.draw(0, 0)
        self.chr_btn.draw(0, 0)
        self.settings_btn.draw(0, 0)
