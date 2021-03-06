import pygame
from GameParameter import display
from GameEffects import load_image
from Button import Button

st_x = 350

background_image = load_image('backgrounds/pause_background.png')

continue_button_image = [load_image(f'ui/buttons/pause_continue_button_{i}.png') for i in range(2)]

restart_button_image = [load_image(f'ui/buttons/pause_restart_button_{i}.png') for i in range(2)]

back_button_image = [load_image(f'ui/buttons/pause_back_button_{i}.png') for i in range(2)]


class PauseMenu:
    def __init__(self, map_objects, map_background):
        self.result = -1  # переменная для отслеживания состояния экрана

        self.map_keys = map_objects[0]  # изображения клавиш
        self.map_objects = map_objects[1:]  # изображений нот
        self.map_background = map_background  # изображений заднего фона
        self.map_background.set_alpha(100)

        self.continue_btn = Button(455, 200, 238, 72, '', continue_button_image, self.continue_map)

        self.restart_btn = Button(455, 350, 238, 72, '', restart_button_image, self.restart)

        self.back_btn = Button(455, 500, 238, 72, '', back_button_image, self.back)

    def get_result(self):
        return self.result

    def continue_map(self):
        self.result = 0

    def restart(self):
        self.result = 1

    def back(self):
        self.result = 2

    def render_pause(self):  # отрисовка экрана паузы
        display.blit(background_image, (0, 0))

        self.continue_btn.draw(0, 0)
        self.restart_btn.draw(0, 0)
        self.back_btn.draw(0, 0)

    def render_map(self):  # отрисовка карты во время обратного отсчета
        display.fill((0, 0, 0))
        display.blit(self.map_background, (0, 0))

        display.blit(self.map_keys[0], (st_x, 0))

        for notes in self.map_objects[0]:  # отрисовка одиночных нот
            if len(notes) == 1:
                sprite = notes[0][0]
                display.blit(sprite.image, sprite.rect)
            elif len(notes) > 1:
                for note in notes:
                    sprite = note[0]
                    display.blit(sprite.image, sprite.rect)

        for slider in self.map_objects[1]:  # отрисовка длинных нот
            for obj in slider:
                try:
                    sprite = obj[0]
                    display.blit(sprite.image, sprite.rect)
                except (AttributeError, TypeError):
                    pass

        key0d_image, key1d_image = self.map_keys[1:]
        display.blit(key0d_image, (st_x + 30, 617))
        display.blit(key1d_image, (st_x + 30 + 45, 617))
        display.blit(key1d_image, (st_x + 30 + 45 * 2, 617))
        display.blit(key0d_image, (st_x + 30 + 45 * 3, 617))
