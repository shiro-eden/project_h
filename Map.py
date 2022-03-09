import os
import pygame

maps = []


class Map():  # класс карты
    def __init__(self, foldername, filename):
        pass


def import_maps():  # создает объекты класса Map, помещает их в maps
    songs = os.listdir(path="maps")
    maps = []
    return maps
