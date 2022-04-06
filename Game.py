import pygame
import math
from GameParameter import clock, fps, display
from GameEffects import drawing_text, load_image, AnimatedSprite
from Settings import load_settings

from Elements import ChemicalElements, Inventory


# загрузка изображений игрового поля
background = load_image('backgrounds/Hod.png')

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

        self.handle_element = None

    def render(self, l_mouse_click):
        mouse = pygame.mouse.get_pos()

        if self.x < mouse[0] < self.x + self.side and self.y < mouse[1] < self.y + self.side:
            if l_mouse_click:
                self.active = not self.active
        if self.active:
            display.blit(self.image_on, (self.x, self.y))
        else:
            display.blit(self.image_off, (self.x, self.y))

        if self.handle_element:
            display.blit(self.handle_element.get_cube_image(), (self.x + 5, self.y + 5))

    def take_element(self, element):
        self.handle_element = element

    def return_element(self):
        el = self.handle_element
        self.handle_element = None
        return el

    def is_handle_element(self):
        if self.handle_element:
            return True
        return False

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False


class Character:
    def __init__(self, name, x, y, count_cubes=1, image=pygame.Surface((50, 50))):
        self.name = name
        self.image = image
        self.width, self.height = self.image.get_rect().size

        self.x, self.y = x, y
        self.count_cubes = count_cubes
        if count_cubes % 2 == 0:
            x = self.x + self.width // 2
        else:
            x = self.x + self.width // 2 - CUBE_SIDE // 2
        self.cubes = [Cube(x - (count_cubes // 2 - i) * (CUBE_SIDE + 5), y, i, count_cubes) for i in range(count_cubes)]
        self.active_cubes = [False] * count_cubes
        self.ind_active_cube = -1

        self.inventory = Inventory(name)

        self.target = None

    def render(self, l_mouse_click):
        display.blit(self.image, (self.x, self.y))

    def attack(self, new_target):
        self.target = new_target

    def deactivate_cubes(self, index):
        for ind, cube in enumerate(self.cubes):
            if ind != index:
                cube.deactivate()


class PlayerCharacter(Character):
    def __init__(self, x, y, count_cubes=1, image=None):
        super().__init__(self, x, y, count_cubes, load_image('Binah.png'))
        pass

    def render(self, l_mouse_click):
        super(PlayerCharacter, self).render(l_mouse_click)

        for ind, cube in enumerate(self.cubes):
            cube.render(l_mouse_click)
            condition = cube.is_active()
            self.active_cubes[ind] = condition
            if condition and self.ind_active_cube != ind:
                self.cubes[self.ind_active_cube].deactivate()
                self.ind_active_cube = ind
        if any(self.active_cubes):
            self.inventory.render()
            if not self.cubes[self.ind_active_cube].is_handle_element():
                result_render = self.inventory.get_selected_element()
                if result_render:
                    self.cubes[self.ind_active_cube].take_element(result_render)
        else:
            self.inventory.close_inventory()


class EnemyCharacter(Character):
    def __init__(self, x, y, count_cubes=1, image=None):
        super().__init__(self, x, y, count_cubes, load_image('Xiao.png'))

    def render(self, l_mouse_click):
        super(EnemyCharacter, self).render(l_mouse_click)
        for ind, cube in enumerate(self.cubes):
            cube.render(False)


class Game:
    def __init__(self, map):
        self.character = PlayerCharacter(800, 350, 5)
        self.enemy = EnemyCharacter(300, 350, 3)

    def handle_keys(self):
        pass

    def render(self, l_mouse_click):
        display.fill((0, 0, 0))
        display.blit(background, (0, 0))

        self.character.render(l_mouse_click)
        self.enemy.render(l_mouse_click)

    def end_game(self):  # функция для отслеживания окончания карты
        pass

    def pause_music(self):  # поставить музыку на паузу
        pygame.mixer.music.pause()

    def unpause_music(self):  # снять музыку с паузы
        pygame.mixer.music.unpause()
