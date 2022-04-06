import pygame
from GameParameter import clock, fps, display
from GameEffects import drawing_text, load_image, AnimatedSprite


BASE_EL_HEIGHT = 520
WIDTH_INVENTORY = 900
WIDTH_ELEMENTS, HEIGHT_ELEMENTS = 120, 200
X_INVENTORY = 100


class Inventory:
    def __init__(self, name_character, max_size=8):
        self.name_character = name_character
        self.inventory = []
        self.max_size = max_size
        self.index_selected_element = None
        for i in range(3):
            self.add_element(ChemicalElements('natrium', "Натрий", 3, 1, 11, 23, True))

    def add_element(self, element):
        if self.max_size == len(self.inventory):
            return False
        self.inventory.append(element)
        self.update_inventory()

    def update_inventory(self):
        size = len(self.inventory)
        if size % 2 == 0:
            x = 560
        else:
            x = 560 - WIDTH_ELEMENTS // 2
        for el in range(size):
            self.inventory[el].change_position(x - (size // 2 - el) * (WIDTH_ELEMENTS + 15))

    def render(self):
        self.index_selected_element = None
        for ind, element in enumerate(self.inventory):
            element.render()
            if element.is_selected():
                self.index_selected_element = ind

    def get_selected_element(self):
        if not self.index_selected_element is None:
            el = self.inventory.pop(self.index_selected_element)
            self.index_selected_element = None
            self.update_inventory()
            return el

    def close_inventory(self):
        for element in self.inventory:
            element.y = 800

class ChemicalElements:  # hos - high oxidation state или высшая степень окисления
    def __init__(self, name_image, name, period, group, nc_number, nc_mass, met=False, hos=False):
        self.image = load_image(f'elements/{name_image}.png')
        self.image_cube = load_image(f'elements/{name_image}_cube.png')
        self.background = pygame.Surface((WIDTH_ELEMENTS, HEIGHT_ELEMENTS))  # = load_image(image)
        self.x, self.y = 150, 300
        self.width, self.height = WIDTH_ELEMENTS, HEIGHT_ELEMENTS
        self.selected = False

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

    def is_selected(self):
        return self.selected

    def get_cube_image(self):
        return self.image_cube

    def render(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.selected = False
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if click[0]:
                self.selected = True
        elif self.y > BASE_EL_HEIGHT:
            self.y -= 30
        elif self.y < BASE_EL_HEIGHT:
            self.y = BASE_EL_HEIGHT
        display.blit(self.background, (self.x, self.y))
        display.blit(self.image, (self.x, self.y))