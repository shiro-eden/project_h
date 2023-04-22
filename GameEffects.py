import pygame
import os
import sys
from GameParameter import display


def load_fonts(font_type):  # загрузка шрифта
    font_type = "fonts/" + font_type
    if not font_type.endswith('.ttf'):
        print(f"Файл '{font_type}' не пдходит по формату")
        sys.exit()
    if not os.path.isfile(font_type):
        font_type = None
    return font_type


fonts = {'corp_round_v1.ttf': load_fonts('corp_round_v1.ttf'),
         'martfutomaru.ttf': load_fonts('martfutomaru.ttf'),
         'rizumu.ttf': load_fonts('rizumu.ttf'),
         'elements.ttf': load_fonts('elements.ttf'),
         'elements_v2.ttf': load_fonts('elements_v2.ttf'),
         None: None}


def drawing_text(text, font_color=pygame.Color('black'), font_size=30,
                 font_type='elements_v2.ttf', bold=False, italic=False):
    # функция для отрисовки текста, также возвращает surface с текстом
    font_type = pygame.font.Font(fonts[font_type], font_size)
    font_type.set_bold(bold)
    font_type.set_italic(italic)
    text = font_type.render(text, True, font_color)
    return text


def load_image(filename):  # функция загрузки изображений
    fullname = "image/" + filename
    if not fullname.endswith('.png') and not fullname.endswith('.jpg')\
            and not fullname.endswith('.ico'):
        print(f"Файл '{fullname}' не пдходит по формату")
        sys.exit()
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_music(filename):  # функция загрузки музыки
    fullname = "music/" + filename
    if not fullname.endswith('.wav') and not fullname.endswith('.mp3'):
        print(f"Файл '{fullname}' не пдходит по формату")
        sys.exit()
    if not os.path.isfile(fullname):
        print(f"Файл с музыкой '{fullname}' не найден")
        sys.exit()
    return fullname