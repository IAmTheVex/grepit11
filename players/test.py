from labyrinth import BotAI

class Move:
    def __init__(self):
        self._movement = [0, 0]
        self._isMoving = False

    def update(self):
        if self._isMoving == True:
            self._isMoving = False
            self._movement = [0, 0]

    def move(self, x, y):
        if self._isMoving == True:
            raise Exception('You need to wait until the current movement is done!')
        else:
            self._isMoving = True
            self._movement = [x, y]

    def state(self):
        return self._movement

    def isMoving(self):
        return self._isMoving

            
class Bot(BotAI):
    def __init__(self):
        self.engine = Move()
        self.m = False

    def update(self, cast_laser):
        while self.engine.isMoving() == True:
            self.engine.update()
        
        # if self.m == False:
            # self.engine.move(0, -100)
        #     self.m = True
        # else:
        #     self.engine.move(0, 100)
        #     self.m = False
        self.engine.move(0, -10)

        return self.engine.state();
        
