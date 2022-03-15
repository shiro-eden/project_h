import pygame
from GameParameter import clock, fps, display
from GameEffects import drawing_text, load_image, AnimatedSprite


MAX_EL_HEIGHT = 400
BASE_EL_HEIGHT = 600
WIDTH_INVENTORY = 900
WIDTH_ELEMENTS, HEIGHT_ELEMENTS = 100, 400
X_INVENTORY = 100


class Inventory:
    def __init__(self, name_character, max_size=8):
        self.name_character = name_character
        self.inventory = []
        self.max_size = max_size
        for i in range(1):
            self.add_element(ChemicalElements(None, "Натрий", 3, 1, 11, 23, True))

    def add_element(self, element):
        if self.max_size == len(self.inventory):
            return False
        self.inventory.append(element)

        size = len(self.inventory)
        if size % 2 == 0:
            x = 560
        else:
            x = 560 - WIDTH_ELEMENTS // 2
        for el in range(size):
            self.inventory[el].change_position(x - (size // 2 - el) * (WIDTH_ELEMENTS + 15))

    def render(self):
        for element in self.inventory:
            element.render()


class ChemicalElements:  # hos - high oxidation state или высшая степень окисления
    def __init__(self, image, name, period, group, nc_number, nc_mass, met=False, hos=False):
        self.image = pygame.Surface((WIDTH_ELEMENTS, HEIGHT_ELEMENTS))  # = load_image(image)
        self.x, self.y = 150, 800
        self.width, self.height = WIDTH_ELEMENTS, HEIGHT_ELEMENTS

        self.name = name
        self.period = period
        self.group = group
        self.nc_number = self.z = nc_number  # self.z - число протонов
        self.nc_mass = nc_mass  # nc_mass тоже самое что и A
        self.n = self.nc_mass - self.z  # self.n - число нейтронов
        self.metallic = met
        if hos:
            self.hos = hos
        else:
            self.hos = group

    def change_position(self, x):
        self.x = x

    def select(self):
        pass

    def render(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if self.y < MAX_EL_HEIGHT:
                self.y += 15
            if click[0]:
                self.select()
        elif self.y > BASE_EL_HEIGHT:
            self.y -= 15
        display.blit(self.image, (self.x, self.y))