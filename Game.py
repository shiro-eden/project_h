import pygame

from GameEffects import drawing_text, load_image
from Button import Button


"""4 Состояния игры:
    1 - Выбор карт: персонажи стоят на месте
    2 - Фаза проверки: персонажи не двигаются
    3 - Фаза битвы: персонажи бьются
    4 - Фаза перехода: персонажи возвращаются на начальные позиции / пропадают"""

level = {1: [
    load_image("level/turn_1.png"),
     ['+6', 190, 30, 30],
     ['+5', 190, 30, 30],
     ['-3', 190, 30, 30],
     ['+10', 190, 30, 30]],
 2: [
     load_image("level/turn_2.png"),
     ['металлов 1A группы', 60, 30, 20],
     ['галогенов', 140, 30, 20],
     ['алюминия и железа', 70, 30, 20],
     ['металлов 2A группы', 60, 30, 20]],
 3: [
     load_image("level/turn_3.png"),
     ['+1', 180, 30, 30],
     ['+2', 190, 30, 30],
     ['-1', 190, 30, 30],
     ['0', 210, 30, 30]],
 4: [
     load_image("level/turn_4.png"),
     [[load_image("level/turn_4/1_off.png"), load_image("level/turn_4/1_on.png")], 190, 30, 30],
     [[load_image("level/turn_4/2_off.png"), load_image("level/turn_4/2_on.png")], 190, 30, 30],
     [[load_image("level/turn_4/3_off.png"), load_image("level/turn_4/3_on.png")], 180, 25, 30],
     [[load_image("level/turn_4/4_off.png"), load_image("level/turn_4/4_on.png")], 190, 30, 30]],
 5: [
     load_image("level/turn_5.png"),
     [[load_image("level/turn_5/1_off.png"), load_image("level/turn_5/1_on.png")], 60, 20, 30],
     [[load_image("level/turn_5/2_off.png"), load_image("level/turn_5/2_on.png")], 60, 20, 30],
     [[load_image("level/turn_5/3_off.png"), load_image("level/turn_5/3_on.png")], 55, 15, 30],
     [[load_image("level/turn_5/4_off.png"), load_image("level/turn_5/4_on.png")], 60, 15, 30]],
 6: [
     load_image("level/turn_6.png"),
     [[load_image("level/turn_6/1_off.png"), load_image("level/turn_6/1_on.png")], 190, 30, 30],
     [[load_image("level/turn_6/2_off.png"), load_image("level/turn_6/2_on.png")], 190, 30, 30],
     [[load_image("level/turn_6/3_off.png"), load_image("level/turn_6/3_on.png")], 180, 25, 30],
     [[load_image("level/turn_6/4_off.png"), load_image("level/turn_6/4_on.png")], 190, 30, 30]],
 7: [
     load_image("level/turn_7.png"),
     ['-2', 190, 30, 30],
     ['+2', 190, 30, 30],
     ['0', 190, 30, 30],
     ['-1', 200, 30, 30]]}

class Field:
    def __init__(self, x, y, item=(False, 0, 0, 1)):
        self.is_selected = False
        self.field_x = x
        self.field_y = y

        self.text, self.text_x, self.text_y, self.size = item
        if self.text:
            if type(self.text) is list:
                self.item_off, self.item_on = self.text
            else:
                self.item_off = drawing_text(self.text, pygame.Color("white"), self.size)
                self.item_on = drawing_text(self.text, pygame.Color("black"), self.size)
        else:
            self.item_on = self.item_off = pygame.Surface((10, 10), pygame.SRCALPHA)

        self.field_on = load_image("ui/buttons/answer_field_on.png")
        self.field_off = load_image("ui/buttons/answer_field_off.png")

    def render(self, mouse_click):
        mouse = pygame.mouse.get_pos()
        if self.field_x < mouse[0] < self.field_x + 450 and self.field_y < mouse[1] < self.field_y + 90:
            if mouse_click[0]:
                self.is_selected = not self.is_selected
            display.blit(self.field_on, (self.field_x, self.field_y))
            display.blit(self.item_on, (self.field_x + self.text_x, self.field_y + self.text_y))
        elif self.is_selected:
            display.blit(self.field_on, (self.field_x, self.field_y))
            display.blit(self.item_on, (self.field_x + self.text_x, self.field_y + self.text_y))
        else:
            display.blit(self.field_off, (self.field_x, self.field_y))
            display.blit(self.item_off, (self.field_x + self.text_x, self.field_y + self.text_y))

    def text_switch(self, item):
        self.text, self.text_x, self.text_y, self.size = item
        if type(self.text) is list:
            self.item_off, self.item_on = self.text
        else:
            self.item_off = drawing_text(self.text, pygame.Color("white"), self.size)
            self.item_on = drawing_text(self.text, pygame.Color("black"), self.size)

    def get_text(self):
        return (self.text, self.text_x, self.text_y, self.size)


class FieldInventory(Field):
    def __init__(self, x, y, item=(False, 0, 0, 1)):
        super().__init__(x, y, item)

    def render(self, mouse_click):
        if not self.is_selected:
            super().render(mouse_click)
            if self.is_selected:
                return self.get_text()


class FieldCheck(Field):
    def __init__(self, x, y, item, img):
        super().__init__(x, y, item)
        self.field_res = img
        self.alpha = 0
        self.field_res.set_alpha(self.alpha)

    def render(self, mouse_click):
        display.blit(self.field_off, (self.field_x, self.field_y))
        display.blit(self.field_res, (self.field_x, self.field_y))
        display.blit(self.item_off, (self.field_x + self.text_x, self.field_y + self.text_y))
        if self.alpha != 255:
            self.alpha += 5
            self.field_res.set_alpha(self.alpha)

class Character:
    def __init__(self, hp, x, y, statement_image=None):
        self.image = statement_image
        self.hp = hp
        self.width, self.height = self.image['rest'].get_rect().size

        self.x, self.y = x, y
        self.new_x, self.new_y = None, None
        self.velocity = 35

        self.health_back = load_image('character/health_back.png')
        self.health_bar = load_image('character/health_bar.png')

    def damage(self):
        self.hp -= 0.35
        if self.hp < 0:
            self.hp = 0
        self.health_bar= self.health_bar.subsurface((0, 0, 150 * self.hp, 40))


class PlayerCharacter(Character):
    def __init__(self, hp, x, y, image=None):
        images = {'rest': load_image(f'character/{image}/{image}_rest.png'),
                  'move': load_image(f'character/{image}/{image}_move.png'),
                  'attack': load_image(f'character/{image}/{image}_fight.png'),
                  'attack_on': load_image(f'character/{image}/{image}_fight_on.png'),
                  'hurt': load_image(f'character/{image}/{image}_hurt.png'),
                  'ready': None}
        self.arrow_up = load_image("ui/buttons/arrow_up.png")
        self.arrow_down = load_image("ui/buttons/arrow_down.png")
        super().__init__(hp, x, y, images)

        self.field = Field(self.x - 160, self.y - 90)

        self.alpha = 255
        self.back_inventory = load_image('backgrounds/Hod.png').subsurface((0, 540), (1280, 180))
        self.back_inventory.set_alpha(self.alpha)

    def render_attack(self, mouse_click):
        display.blit(self.health_back, (self.x - 25, self.y + 140))
        display.blit(self.health_bar, (self.x - 25, self.y + 140))
        if self.alpha_sword != 0:
            self.alpha_sword -= 35
            self.image['attack_on'].set_alpha(self.alpha_sword)
            display.blit(self.image['attack_on'], (self.x, self.y))
        self.field.render(mouse_click)
        display.blit(self.image['attack'], (self.x, self.y))

    def render_move(self, mouse_click):
        display.blit(self.health_back, (self.x - 25, self.y + 140))
        display.blit(self.health_bar, (self.x - 25, self.y + 140))

        self.x += self.velocity
        display.blit(self.image['move'], (self.x, self.y))
        self.field.render(mouse_click)

    def render_state(self, mouse_click):
        display.blit(self.health_back, (self.x - 25, self.y + 140))
        display.blit(self.health_bar, (self.x - 25, self.y + 140))

        display.blit(self.image['rest'], (self.x, self.y))

        self.field.render(mouse_click)
        if self.field.is_selected:
            self.inventory_active = True
        else:
            self.inventory_active = False
        self.render_inventory()

        self.alpha_sword = 255

    def to_check_state(self, img):
        self.field = FieldCheck(self.x - 160, self.y - 90, self.field.get_text(), img)
        self.inventory_active = False

    def render_check(self, mouse_click):
        display.blit(self.health_back, (self.x - 25, self.y + 140))
        display.blit(self.health_bar, (self.x - 25, self.y + 140))

        display.blit(self.image['rest'], (self.x, self.y))
        self.field.render(mouse_click)

    def render_hurt(self, mouse_click):
        display.blit(self.health_back, (self.x - 25, self.y + 140))
        display.blit(self.health_bar, (self.x - 25, self.y + 140))

        display.blit(self.image['hurt'], (self.x, self.y))
        self.field.render(mouse_click)

    def render_inventory(self):
        if self.inventory_active and self.alpha != 0:
            self.alpha -= 15
            self.back_inventory.set_alpha(self.alpha)
        elif not self.inventory_active and self.alpha != 255:
            self.alpha += 15
            self.back_inventory.set_alpha(self.alpha)

        for f in range(4):
            result = self.inventory[f].render(mouse_click)
            if result:
                self.field.text_switch(result)
                for t in range(4):
                    if t == f:
                        continue
                    self.inventory[t].is_selected = False

        display.blit(self.back_inventory, (0, 540))

    def next_level(self, items):
        self.field = Field(self.x - 160, self.y - 90)
        self.alpha = 255
        self.back_inventory.set_alpha(self.alpha)
        self.inventory_active = False
        self.inventory = [
                          FieldInventory(100, 540, items[1]),
                          FieldInventory(700, 540, items[2]),
                          FieldInventory(100, 640, items[3]),
                          FieldInventory(700, 640, items[4])
                          ]

class EnemyCharacter(Character):
    def __init__(self, hp, x, y, image=None):
        images = {'rest': load_image('character/puppet/roland_rest.png'),
                  'move': load_image('character/puppet/roland_move.png'),
                  'attack': load_image('character/puppet/roland_fight.png'),
                  'attack_on': load_image('character/puppet/roland_fight_on.png'),
                  'hurt': load_image('character/puppet/roland_hurt.png'),
                  'ready': None}
        super().__init__(hp, x, y, images)
        self.velocity *= -1

    def render(self, mouse_click):
        display.blit(self.health_back, (self.x - 35, self.y + 140))
        display.blit(self.health_bar, (self.x - 35, self.y + 140))
        display.blit(self.image['rest'], (self.x, self.y))

        self.alpha_sword = 255

    def render_move(self, mouse_click):
        display.blit(self.health_back, (self.x - 35, self.y + 140))
        display.blit(self.health_bar, (self.x - 35, self.y + 140))

        self.x += self.velocity
        display.blit(self.image['move'], (self.x, self.y))

    def render_attack(self, mouse_click):
        display.blit(self.health_back, (self.x - 35, self.y + 140))
        display.blit(self.health_bar, (self.x - 35, self.y + 140))
        if self.alpha_sword != 0:
            self.alpha_sword -= 35
            self.image['attack_on'].set_alpha(self.alpha_sword)
            display.blit(self.image['attack_on'], (self.x - 50, self.y))
        display.blit(self.image['attack'], (self.x - 50, self.y))

    def render_hurt(self, mouse_click):
        display.blit(self.health_back, (self.x - 35, self.y + 140))
        display.blit(self.health_bar, (self.x - 35, self.y + 140))

        display.blit(self.image['hurt'], (self.x - 10, self.y - 10))


class Game:
    def __init__(self, map):
        self.turn = 0
        self.game_phase = 1
        self.restart = False

        self.hod = PlayerCharacter(1, 240, 350, "hod")
        # self.malkuth = PlayerCharacter(1, 240, 350, "malkuth")
        self.enemy = EnemyCharacter(1, 800, 355)

        button_start_image = [load_image(f'ui/buttons/start_button_{i}.png') for i in range(3)]
        self.button_end_turn = Button(575, -15, 130, 120, '', button_start_image, self.end_turn)

        self.background = load_image('backgrounds/Hod.png')
        self.high_ground = load_image('backgrounds/high_ground.png')
        self.mask_background = load_image('backgrounds/mask_background.png')
        self.alpha_mask = 0
        self.mask_background.set_alpha(self.alpha_mask)

        self.question = level
        self.answer = {1: 2, 2: 1, 3: 4, 4: 4, 5: 3, 6: 4, 7: 1}

        self.next_level()

        self.alpha = 255
        self.question_back = load_image('backgrounds/Hod.png').subsurface((240, 110), (800, 150))
        self.question_label = load_image('backgrounds/question_label.png')
        self.active_question = True

        self.win_background= load_image('backgrounds/victory.png')
        self.lose_background = load_image('backgrounds/defeat.png')

        self.alpha_background = 0

        button_restart_image = [load_image(f'ui/buttons/restart_button_{i}.png') for i in range(3)]
        self.win_turns = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False}
        self.restart_btn = Button(530, 350, 200, 200, '', button_restart_image, self.restart_game)

    def render(self, mouse_click):
        display.fill((0, 0, 0))
        display.blit(self.background, (0, 0))
        display.blit(self.high_ground, (0, 0))

        if self.turn == -1:
            self.alpha += 15
            self.win_background.set_alpha(self.alpha)
            display.blit(self.win_background, (0, 0))
            self.restart_btn.draw(mouse_click)
            return self.restart
        elif self.turn == -2:
            self.alpha += 15
            self.lose_background.set_alpha(self.alpha)
            display.blit(self.lose_background, (0, 0))
            self.restart_btn.draw(mouse_click)
            return self.restart

        if self.game_phase == 1:
            self.render_state(mouse_click)
        elif self.game_phase == 2:
            self.render_check(mouse_click)
        elif self.game_phase == 3:
            self.render_attack(mouse_click)
        else:
            self.game_phase = 1
            self.next_level()
            display.blit(self.mask_background, (0, 0))
            self.hod.render_state(mouse_click)
            self.enemy.render(mouse_click)
            display.blit(self.question_text, (240, 110))
            display.blit(self.question_back, (240, 110))

        if self.hod.hp == 0:
            self.turn = -2
        elif self.enemy.hp == 0:
            self.turn = -1

    def render_state(self, mouse_click):
        display.blit(self.mask_background, (0, 0))
        if self.alpha_mask != 0:
            self.alpha_mask -= 15
            self.mask_background.set_alpha(self.alpha_mask)

        if self.active_question and self.alpha != 0:
            self.alpha -= 15
            self.question_back.set_alpha(self.alpha)
        elif not self.active_question and self.alpha != 255:
            self.alpha += 15
            self.question_back.set_alpha(self.alpha)
        display.blit(self.question_text, (240, 110))
        display.blit(self.question_back, (240, 110))

        self.hod.render_state(mouse_click)
        self.enemy.render(mouse_click)
        self.button_end_turn.draw(mouse_click)

    def render_check(self, mouse_click):
        display.blit(self.mask_background, (0, 0))
        if self.alpha_mask != 255:
            self.alpha_mask += 15
            self.mask_background.set_alpha(self.alpha_mask)

        display.blit(self.question_text, (240, 110))
        display.blit(self.question_back, (240, 110))

        self.hod.render_check(mouse_click)
        self.enemy.render(mouse_click)
        if self.alpha_mask == 255:
            self.game_phase = 3

    def render_attack(self, mouse_click):
        display.blit(self.mask_background, (0, 0))
        if self.win_turns[self.turn]:
            if self.hod.x <= 630:
                self.damaged = True
                self.enemy.render(mouse_click)
                self.hod.render_move(mouse_click)
            else:
                if self.damaged:
                    self.damaged = False
                    self.enemy.damage()
                    self.time_count = 0
                self.time_count += 1
                self.hod.render_attack(mouse_click)
                self.enemy.render_hurt(mouse_click)
                if self.time_count == 30:
                    self.game_phase = 0
        else:
            if self.enemy.x >= 400:
                self.damaged = True
                self.enemy.render_move(mouse_click)
                self.hod.render_check(mouse_click)
            else:
                if self.damaged:
                    self.damaged = False
                    self.hod.damage()
                    self.time_count = 0
                self.time_count += 1
                self.enemy.render_attack(mouse_click)
                self.hod.render_hurt(mouse_click)
                if self.time_count == 30:
                    self.game_phase = 0

        display.blit(self.question_text, (240, 110))
        display.blit(self.question_back, (240, 110))

    def control_reaction(self, x, y, z, k, ans):
        x1, y1, z1, k1 = ans.split()
        return [x1 != x, y1 != y, z1 != z, k1 != k]

    def end_turn(self):
        res = self.hod.field.get_text()
        if res[0]:
            for el in range(1, 5):
                if self.question[self.turn][el][0] == res[0]:
                    if el == self.answer[self.turn]:
                        img = load_image("ui/buttons/answer_field_correct.png")
                        self.win_turns[self.turn] = True
                    else:
                        img = load_image("ui/buttons/answer_field_wrong.png")
                    break
            self.hod.to_check_state(img)
            self.game_phase = 2

    def end_game(self):  # функция для отслеживания окончания карты
        pass

    def next_level(self):
        self.turn += 1
        self.hod.x = 240
        self.hod.next_level(self.question[self.turn])
        self.enemy.x = 800
        self.question_text = self.question[self.turn][0]

    def restart_game(self):
        self.restart = True

    def pause_music(self):  # поставить музыку на паузу
        pygame.mixer.music.pause()

    def unpause_music(self):  # снять музыку с паузы
        pygame.mixer.music.unpause()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Project H')
    size = width, height = 1280, 720
    display = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    fps = 60
    screen = Game(map)
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
        if screen.render(mouse_click):
            screen = Game(map)
            pygame.display.flip()
            clock.tick(fps)
            continue
        if screen.end_game():
            game = False
        pygame.display.flip()
        clock.tick(fps)
    # вызов экрана с результатами игры

    pygame.quit()
