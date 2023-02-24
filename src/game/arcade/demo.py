import arcade
from src.game.arcade.MainWindow import TaikoWindow, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from src.game.core import Taiko
from src.osumap import OsuMap


def demo():
    """ Main function """
    with open("./tests/test.osu") as inpt:
        mp = OsuMap.OsuMap(inpt.read())    

    taiko = Taiko()
    taiko.load(mp)
    game = TaikoWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, taiko)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    demo()