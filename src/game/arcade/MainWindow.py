import time
import arcade
import arcade.key
from src.game.core import Taiko, Action
from queue import Queue

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256
SCREEN_TITLE = "osu!taiko simplistic render"


class TaikoWindow(arcade.Window):

    def __init__(self, width, height, title, taiko: Taiko = None):
        super().__init__(width, height, title)

        self.taiko = taiko
        self.time = None
        self.action = Queue()

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.time = 0

    def on_key_press(self, symbol: int, modifiers: int):
        super().on_key_press(symbol, modifiers)
        if symbol == arcade.key.Z:
            self.action.put((Action.KEY1, time.monotonic(),))
        elif symbol == arcade.key.V:
            self.action.put((Action.KEY2, time.monotonic(),))

    def on_draw(self):
        super().on_draw()
        arcade.start_render()
        to_render = self.taiko.state.slice(self.time, self.time + 1)
        for hit_object in to_render:
            color = arcade.color.AERO_BLUE
            rad = 20
            # print(f"{hit_object.type}")
            if hit_object.type & 1 != 0:
                # print(f" is circle\n")
                if hit_object.hit_sound == 0 or hit_object.hit_sound == 4:
                    color = arcade.color.RED
                if hit_object.hit_sound == 4 or hit_object.hit_sound == 12:
                    rad = 40
            elif hit_object.type & 8 != 0:
                print("SPINNER!")
                rad = 60
                color = arcade.color.YELLOW
            arcade.draw_circle_filled(radius=rad, color=color, center_y=SCREEN_HEIGHT / 2,
                                      center_x=100 + self._lerp(hit_object.time - self.time))
        arcade.finish_render()

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        self.time += delta_time

    def _lerp(self, t):
        N = SCREEN_WIDTH - 100
        return N * t

    @property
    def dt(self):
        return (time.monotonic_ns() - self.time)
