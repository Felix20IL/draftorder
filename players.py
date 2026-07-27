#generate players for the draft ordering

class Player():
    def __init__(self, name):
        self.finished = 0
        self.finishpos = 0
        self.currentpos = 0
        self.togo = 100
        self.name = name


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



