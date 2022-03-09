import pygame
import math
from GameParameter import clock, fps, display
from GameEffects import drawing_text, load_image, AnimatedSprite
from Settings import load_settings

from Elements import ChemicalElements, Inventory

# загрузка изображений клавиш(без 'd' на конце - клавиши на 1 и 4 линиях, с 'd' - клавиши на 2 и 3)
key0_image = load_image('skin/key0.png')  # клавиши с предпиской '0' - не нажатая клавиша
key1_image = load_image('skin/key1.png')  # клавиши с предпиской '1' - нажатая клавиша)

# загрузка изображений игрового поля
stage_image = load_image('skin/stage.png')
background = load_image('Hod.png')


class Cube:
    def __init__(self, x, y, side=100):
        self.x = x
        self.y = y
        self.side = side
        self.image = pygame.Surface((50, 50))
        self.active = False

    def render(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.side and self.y < mouse[1] < self.y + self.side:
            if click[0]:
                self.select()
                self.active = not self.active
        else:
            pass
        display.blit(self.image, (self.x, self.y))

    def select(self):
        pass

    def is_active(self):
        return self.active


class Character:
    def __init__(self, name, x, y, count_cubes=1, image=None):
        print(count_cubes)
        self.name = name
        self.image = pygame.Surface((25, 70))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.x, self.y = x, y
        self.count_cubes = count_cubes
        self.cubes = [Cube(x - 100 * (count_cubes // 2 + i), y) for i in range(count_cubes)]

        self.inventory = Inventory(name)

    def render(self):
        display.blit(self.image, (self.x, self.y))

        for cube in self.cubes:
            cube.render()
            if cube.is_active():
                self.inventory.render()


class PlayerCharacter(Character):
    def __init__(self, x, y, count_cubes=1, image=None):
        super().__init__(self, x, y, count_cubes, image)
        pass


class Game:
    def __init__(self, map):
        self.character = PlayerCharacter(800, 400)

    def handle_keys(self):
        pass

    def render(self):
        display.fill((0, 0, 0))
        display.blit(background, (0, 0))

        self.character.render()

    def end_game(self):  # функция для отслеживания окончания карты
        pass

    def pause_music(self):  # поставить музыку на паузу
        pygame.mixer.music.pause()

    def unpause_music(self):  # снять музыку с паузы
        pygame.mixer.music.unpause()
