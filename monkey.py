import tkinter as tk

from gamelib import Sprite, GameApp, Text

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 1


class Banana(Sprite):
    def init_sprite(self):
        self.vx = 0
        self.vy = 0

        self.start_x = self.x
        self.start_y = self.y
        self.start_vx = 0
        self.start_vy = 0

        self.is_moving = False
        self.hide()

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

        self.start_vx = vx
        self.start_vy =vy

    def update(self):
        if self.is_moving:
            self.x += 5
            self.y -= self.vy
            self.vy -= GRAVITY

            if self.y > CANVAS_HEIGHT:
                self.stop()
                self.hide()


    def reset(self):
        self.x = self.start_x
        self.y = self.start_y

        self.vx = self.start_vx
        self.vy = self.start_vy
        self.stop()

    def start(self):
        self.show()
        self.is_moving = True

    def stop(self):
        self.is_moving = False


class MonkeyGame(GameApp):
    class AppObserver:
        def __init__(self, app):
            self.app = app

    class SpeedAdjustmentObserver(AppObserver):
        def notify(self, event):
            app = self.app
            if event.char == "+":
                if app.speed < 10:
                    app.speed +=1
                    app.update_speed_text()
            if event.char == "-":
                if app.speed > 1:
                    app.speed -=1
                    app.update_speed_text()

    class BananaAdjustmentObserver(AppObserver):
        def notify(self, event):
            app = self.app
            if event.char == " ":
                if not app.banana.is_moving:
                    app.banana.set_speed(3 * app.speed, 5 * app.speed)
                    app.banana.reset()
                    app.banana.start()


    def create_sprite(self):
        self.banana = Banana(self, "Banana.png", 100, 400)
        self.banana.set_speed(15, 25)

        self.monkey = Sprite(self, 'gollira.png', 100, 400)
        self.other_monkey = Sprite(self, 'gollira.png', 700, 400)

        self.speed_text = Text(self, 'Speed: XX', 40, 20)

        self.sprite.append(self.banana)
        self.sprite.append(self.monkey)
        self.sprite.append(self.other_monkey)
        self.sprite.append(self.speed_text)

    def update_speed_text(self):
        self.speed_text.set_text(f"Speed: {self.speed}")

    def init_game(self):
        self.create_sprite()

        self.speed = 3
        self.update_speed_text()

        self.register_on_key_pressed_observer(MonkeyGame.SpeedAdjustmentObserver(self))
        self.register_on_key_pressed_observer(MonkeyGame.BananaAdjustmentObserver(self))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")

    root.resizable(False, False)
    app = MonkeyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()

