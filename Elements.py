import pygame
from GameParameter import display
from GameEffects import drawing_text, load_image

BASE_EL_HEIGHT = 520
WIDTH_INVENTORY = 900
WIDTH_ELEMENTS, HEIGHT_ELEMENTS = 140, 200
X_INVENTORY = 100


class Inventory:
    def __init__(self, name_character, max_size=8):
        self.name_character = name_character
        self.inventory = []
        self.max_size = max_size
        self.index_selected_element = None
        for el in ELEMENTS.values():
            self.add_element(el(1))

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
    def __init__(self, name_image, name, period, group, nc_number, nc_mass, index, met, hos):
        self.image = None  # поменять на name_image
        self.background = load_image('elements/card.png')
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

        self.index = index
        self.draw_index()

    def change_position(self, x):
        self.x = x

    def is_selected(self):
        return self.selected

    def get_image(self):
        return self.image

    def update_value(self, value):
        if 0 < value < 10:
            self.index = value
            self.draw_index()

    def draw_index(self):
        self.image = drawing_text(self.name, pygame.Color('white'), font_size=65)
        if self.index != 1:
            ind = drawing_text(str(self.index), pygame.Color('white'), font_size=20)
            img = pygame.Surface((self.image.get_width() + ind.get_width(), self.image.get_height()), pygame.SRCALPHA)
            img.blit(self.image, (0, 0))
            img.blit(ind, (self.image.get_width(), self.image.get_height() - ind.get_height()))
            self.image = img

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
        x, y = self.image.get_size()
        x, y = (WIDTH_ELEMENTS - x) // 2, (HEIGHT_ELEMENTS - y) // 2
        display.blit(self.background, (self.x, self.y))
        display.blit(self.image, (self.x + x - 5, self.y + y))


class Natrium(ChemicalElements):
    def __init__(self, index):
        name_image = "Natrium"
        name = "Na"
        period = 3
        group = 1
        nc_number = 11
        nc_mass = 23
        met = True
        super().__init__(name_image, name, period, group, nc_number, nc_mass, index, met, False)

class Bromum(ChemicalElements):
    def __init__(self, index):
        name_image = "Bromum"
        name = "Br"
        period = 4
        group = 17
        nc_number = 35
        nc_mass = 80
        met = False
        super().__init__(name_image, name, period, group, nc_number, nc_mass, index, met, False)


class Nitrogenium(ChemicalElements):
    def __init__(self, index):
        name_image = "Nitrogenium"
        name = "N"
        period = 2
        group = 15
        nc_number = 7
        nc_mass = 14
        met = False
        super().__init__(name_image, name, period, group, nc_number, nc_mass, index, met, False)


class Lithium(ChemicalElements):
    def __init__(self, index):
        name_image = "Lithium"
        name = "Li"
        period = 2
        group = 1
        nc_number = 3
        nc_mass = 7
        met = True
        super().__init__(name_image, name, period, group, nc_number, nc_mass, index, met, False)


class Hydrogenium(ChemicalElements):
    def __init__(self, index):
        name_image = "Hydrogenium"
        name = "H"
        period = 1
        group = 1
        nc_number = 1
        nc_mass = 1
        met = False
        super().__init__(name_image, name, period, group, nc_number, nc_mass, index, met, False)


class Oxygenium(ChemicalElements):
    def __init__(self, index):
        name_image = "Oxygenium"
        name = "O"
        period = 2
        group = 16
        nc_number = 8
        nc_mass = 16
        met = False
        super().__init__(name_image, name, period, group, nc_number, nc_mass, index, met, False)

class Aluminium(ChemicalElements):
    def __init__(self, index):
        name_image = "Aluminium"
        name = "Al"
        period = 3
        group = 13
        nc_number = 8
        nc_mass = 13
        met = True
        super().__init__(name_image, name, period, group, nc_number, nc_mass, index, met, False)


ELEMENTS = {"N": Nitrogenium,
            "Li": Lithium,
            "H": Hydrogenium,
            "O": Oxygenium,
            "Al": Aluminium,
            "Br": Bromum}