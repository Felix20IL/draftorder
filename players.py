#generate players for the draft ordering

#definesattributes held
class Player():
    def __init__(self, name):
        self.finished = 0
        self.finishpos = 0
        self.currentpos = 0
        self.togo = 100
        self.name = name

#take a list of players and reorders them based on their finish position and distance to go if not finished. 
def reorder_players(players):
    finished_list = []
    unfinished_list = []
    for player in players:
        if player.finished == 1:
            finished_list.append(player)
        else:
            unfinished_list.append(player)
    finished_list.sort(key=lambda x: x.finishpos)
    unfinished_list.sort(key=lambda x: x.togo)
    return finished_list + unfinished_list



