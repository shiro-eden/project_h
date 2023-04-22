import pygame

from GameParameter import clock, fps, display
from GameEffects import drawing_text, load_image

characters = {
    "Malkuth":
        {
            "label": load_image("ui/decor/malkuth_label.png"),
            "main": load_image("character/malkuth/malkuth_novella_main.png"),
            "back": load_image("character/malkuth/malkuth_novella_back.png")
        },
    "Hod":
        {
            "label": load_image("ui/decor/hod_label.png"),
            "main": load_image("character/hod/hod_novella_main.png"),
            "back": load_image("character/hod/hod_novella_back.png")
        }
}
background = load_image("backgrounds/library.png")
text_label = load_image("backgrounds/text_label.png")

txt = open("image/levels/1_novella.txt").readline().split()
txt = [[txt[i], load_image(f"levels/{i + 1}.png")]for i in range(len(txt))]


class Novella:
    def __init__(self):
        self.text_line = 0
        self.active_text = txt[self.text_line][1]
        self.name_chr = drawing_text(txt[self.text_line][0], pygame.Color('white'), font_size=22)

    def render(self, mouse_click):
        display.blit(background, (0, 0))

        if mouse_click[0]:
            self.text_line += 1
            self.active_text = txt[self.text_line][1]
            self.name_chr = drawing_text(txt[self.text_line][0], pygame.Color('white'), font_size=22)

        if txt[self.text_line][0] == "Malkuth":
            display.blit(characters["Malkuth"]["main"], (700, 150))
            display.blit(characters["Hod"]["back"], (200, 150))
            display.blit(text_label, (0, 500))
            display.blit(characters["Malkuth"]["label"], (0, 500))
        else:
            display.blit(characters["Malkuth"]["back"], (700, 150))
            display.blit(characters["Hod"]["main"], (200, 150))
            display.blit(text_label, (0, 500))
            display.blit(characters["Hod"]["label"], (0, 500))

        display.blit(self.name_chr, (125, 554))
        display.blit(self.active_text, (110, 580))

    def get_result(self):
        return self.result

    def back(self):
        self.result = 0

    def restart(self):
        self.result = 1


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('リズム')
    pygame.display.set_icon(load_image("icon.ico"))
    size = width, height = 1280, 720
    display = pygame.display.set_mode(size)

    screen = Novella()
    game = True
    while game:
        mouse_click = [False, False]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click[0] = True
                elif event.button == 3:
                    mouse_click[1] = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # обработка выхода в меню паузы
                    screen.pause_music()
        screen.render(mouse_click)
        pygame.display.flip()
        clock.tick(fps)
    # вызов экрана с результатами игры

    pygame.quit()
