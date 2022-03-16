import pygame
import math
from GameParameter import clock, fps, display
from GameEffects import drawing_text, load_image, AnimatedSprite
from Settings import load_settings

from Elements import ChemicalElements, Inventory


# загрузка изображений игрового поля
background = load_image('Hod.png')

CUBE_SIDE = 40


class Cube:
    def __init__(self, x, y, number, count_cubes):
        self.x = x
        self.y = y - CUBE_SIDE - 10
        self.number = number
        self.side = CUBE_SIDE
        self.image_off = pygame.Surface((self.side, self.side))
        self.image_on = pygame.Surface((self.side, self.side))
        self.image_on.fill((255, 255, 255))
        self.active = False

    def render(self, l_mouse_click):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.side and self.y < mouse[1] < self.y + self.side:
            if l_mouse_click:
                self.select()
                self.active = not self.active
        else:
            pass
        if self.active:
            display.blit(self.image_on, (self.x, self.y))
        else:
            display.blit(self.image_off, (self.x, self.y))

    def select(self):
        pass

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False

class Character:
    def __init__(self, name, x, y, count_cubes=1, image=None):
        self.name = name
        self.image = load_image('Binah.png')
        self.width, self.height = self.image.get_rect().size

        self.x, self.y = x, y
        self.count_cubes = count_cubes
        if count_cubes % 2 == 0:
            x = self.x + self.width // 2
        else:
            x = self.x + self.width // 2 - CUBE_SIDE // 2
        self.cubes = [Cube(x - (count_cubes // 2 - i) * (CUBE_SIDE + 5), y, i, count_cubes) for i in range(count_cubes)]
        self.has_active_cube = False

        self.inventory = Inventory(name)

    def render(self, l_mouse_click):
        display.blit(self.image, (self.x, self.y))

        for ind, cube in enumerate(self.cubes):
            cube.render(l_mouse_click)
            if cube.is_active():
                self.inventory.render()
                if self.has_active_cube:
                    self.deactivate_cubes(ind)
                self.has_active_cube = True

    def deactivate_cubes(self, index):
        for ind, cube in enumerate(self.cubes):
            if ind != index:
                cube.deactivate()

class PlayerCharacter(Character):
    def __init__(self, x, y, count_cubes=1, image=None):
        super().__init__(self, x, y, count_cubes, image)
        pass


class Game:
    def __init__(self, map):
        self.character = PlayerCharacter(800, 350, 5)

    def handle_keys(self):
        pass

    def render(self, l_mouse_click):
        display.fill((0, 0, 0))
        display.blit(background, (0, 0))

        self.character.render(l_mouse_click)

    def end_game(self):  # функция для отслеживания окончания карты
        pass

    def pause_music(self):  # поставить музыку на паузу
        pygame.mixer.music.pause()

    def unpause_music(self):  # снять музыку с паузы
        pygame.mixer.music.unpause()
