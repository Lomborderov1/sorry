from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

FZV = 120
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        x,y = self.land.loadLand("map_warfes.txt")
        self.hero = Hero((12, 2, 2),self.land)
        base.camLens.setFov(FZV)

game = Game()
game.run()

key_f1 = 'f1'

def key(key):
    