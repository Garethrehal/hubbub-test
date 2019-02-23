class Game(object):
    def __init__(self, rolls):
        self.rolls = rolls
    
    def pinsDown(self, index, length):
        return sum(map(self.roll, range(index, index + length)))
    
    def roll(self, index):
        if index < len(self.rolls):
            return self.rolls[index]
        else:
            return 0


class Frame(object):
    # Defining a frame of play.
    def __init__(self, score, length):
        self.score = score
        # normally a frame is 2 rolls. Unless it's a strike or the final frame of a game.
        # so the length of a frame needs to needs to be flexible
        self.length = length



def scoreGame(rolls):
    game = Game(rolls)
    return sum(frame.score for frame in frames(game))


def frames(game):
    index = 0
    for frame_index in range(0, 10):
        frame = createFrame(game, index)
        yield frame
        index += frame.length



def createFrame(game, index):
    # Check to see how the new frame should be flagged.
    if isStrike(game, index):
        return createStrike(game, index)
    elif isSpare(game, index):
        return createSpare(game, index)
    else:
        return createNormalFrame(game, index)
    
# Defining our various types of frame, Based on which frame it is in the game and number of pins down.
def createNormalFrame(game, index):
    score = game.pinsDown(index, 2)
    return Frame(score, 2)   

def createSpare(game, index):
    score = game.pinsDown(index, 3)
    return Frame(score, 2)

def createStrike(game, index):
    score = game.pinsDown(index, 3)
    return Frame(score, 1)



# Checks. 
def isStrike(game, index):
    return game.pinsDown(index, 1) == 10

def isSpare(game, index):
    return game.pinsDown(index, 2) == 10