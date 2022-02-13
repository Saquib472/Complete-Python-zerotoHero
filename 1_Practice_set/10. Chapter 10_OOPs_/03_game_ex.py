class Remote:
    pass

class Player:
    def moveLeft(self):
        pass
    def moveRight(self):
        pass
    def moveTop(self):
        pass
    def moveBackwards(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isClickleft()):
    player1.moveLeft()