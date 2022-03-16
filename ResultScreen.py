from GameParameter import display
from GameEffects import drawing_text, load_image
from Button import Button
import sqlite3
import datetime as dt

background = load_image('backgrounds/result_background.png')

back_button_image = [load_image(f'ui/buttons/pause_back_button_{i}.png') for i in range(2)]
restart_button_image = [load_image(f'ui/buttons/pause_restart_button_{i}.png') for i in range(2)]


class ResultScreen:
    def __init__(self, count_combo, score, marks, accuracy, map):
        self.result = -1
        # self.count_combo = str(count_combo) + 'x'
        # self.score = str(score)
        # self.marks = [str(i) + 'x' for i in marks.values()]
        #
        # if accuracy == 100:
        #     self.rank = load_image('skin/rank_SS.png')
        # elif accuracy > 95:
        #     self.rank = load_image('skin/rank_S.png')
        # elif accuracy > 90:
        #     self.rank = load_image('skin/rank_A.png')
        # elif accuracy > 80:
        #     self.rank = load_image('skin/rank_B.png')
        # elif accuracy > 70:
        #     self.rank = load_image('skin/rank_C.png')
        # else:
        #     self.rank = load_image('skin/rank_D.png')
        # self.accuracy = str('%.2f' % accuracy) + '%'
        #
        # self.back_btn = Button(-30, 630, 236, 92, '', back_button_image, self.back)
        #
        # self.restart_btn = Button(908, 630, 236, 92, '', restart_button_image, self.restart)
        #
        # map_id = map[2].map_id
        # mapset_id = map[2].mapset_id
        # time = str(dt.datetime.now().time()).split('.')[0]
        # date = str(dt.datetime.now().date())
        # con = sqlite3.connect('records.db')
        # cur = con.cursor()
        # cur.execute(
        #     f"INSERT INTO Records(map_id, mapset_id, score, accuracy, combo, date, time) VALUES({map_id}, {mapset_id}, {score}, {accuracy}, {count_combo}, '{date}', '{time}')")
        # con.commit()

    def render(self):
        display.blit(background, (0, 0))

    def get_result(self):
        return self.result

    def back(self):
        self.result = 0

    def restart(self):
        self.result = 1
