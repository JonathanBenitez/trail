mapy = "|"
mapx= "____"

class ThreeInARow()
def __init__(self, score):
    self.score = score
            

class PrintScoreBoard():
    def __init__(self, score):
        self.score = score
        self.counter = 0
        for self.row in score:
            print()
            for self.elem in self.row:
                print(self.elem, mapy, end ='')
                self.counter=(1+self.counter)%3
                if(self.counter == 0):
                    print()
                    for self.elem in self.row:
                        print(mapx, end ='')


score = [[0 , 0 , 0],[0 , 0 ,0 ],[0, 0 , 0]]
gameover=1

playerone = 1

while gameover<2:
    PrintScoreBoard(score)
    print()
    try:
        x = int(input('Give Me them Y input'))
    except:
        print("That's not a valid option")
    try:
        y = int(input('Give Me them X input'))
    except:
        print("That's not a valid option")
    if(x > 2 or y>2 or x<0 or y<0):
        print("That's not a valid option")
    else:
        if(playerone):
            if(score[x][y] ==0):
                score[x][y] = 1
                playerone = 0
        else: 
            if(score[x][y] ==0):
                score[x][y] = 2
                playerone = 1

