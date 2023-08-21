import random
from tabulate import tabulate
class ChessPlayer:
    def __init__(self,name,age,elo,tenacity,isboring,score):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.isboring = isboring
        self.score = score
    
players = [
ChessPlayer("Courage the Cowardly Dog",25,1000.39,1000,False,0),
ChessPlayer("Princess Peach",23,945.65,50,True,0),
ChessPlayer("Walter White",50,1650.73,750,False,0),
ChessPlayer("Rory Gilmore",16,1700.87,500,False,0),
ChessPlayer("Anthony Fantao",37,1400.45,400,True,0),
ChessPlayer("Beth Harmon",20,2500.34,150,False,0)
]

def simulateMatch(list):
    factor = random.randint(1,10)
    print("The random factor is",factor)
    for i in range(5):
        for j in range(i+1,6):
            if ((players[i].isboring or players[j].isboring) and (abs(players[i].elo - players[j].elo)<=100)):
                players[i].score+=1
                players[j].score+=1
            else:   
                if players[i].elo > players[j].elo:
                    x = players[i].elo - players[j].elo
                    if x > 100:
                        players[i].score+=2
                    elif x>=50 and x<=100:
                        if factor*players[j].elo > players[i].elo:
                            players[j].score+=2
                        else:
                            players[i].score+=2
                    elif x<50:
                        if players[i].tenacity > players[j].tenacity:
                            players[i].score+=2
                        else:
                            players[j].score+=2
                elif players[j].elo > players[i].elo:
                    x = players[j].elo - players[i].elo
                    if x > 100:
                        players[j].score+=2
                    elif (x>=50 and x<=100):
                        if factor*players[i].elo > players[j].elo:
                            players[i].score+=2
                        else:
                            players[j].score+=2
                    elif x<50:
                        if players[j].tenacity > players[i].tenacity:
                            players[j].score+=2
                        else:
                            players[i].score+=2 
                 

            
simulateMatch(players)


headers = ['Player','Age','Elo','Tenacity','isBoring','Score']
data = [["Courage the Cowardly Dog",23,1000.39,1000,False,players[0].score],
["Princess Peach",23,945.65,50,True,players[1].score],
["Walter White",50,1650.73,750,False,players[2].score],
["Rory Gilmore",16,1700.87,500,False,players[3].score],
["Anthony Fantano",37,1400.45,400,True,players[4].score],
["Beth Harmon",20,2500.34,150,False,players[5].score]
]

data.sort(key=lambda row:row[-1] , reverse=True)
print(tabulate(data,headers=headers))
print()
