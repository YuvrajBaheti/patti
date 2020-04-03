import random
from Players import *
class game:
    def __init__(self):
        self.cards=['r','r','r','r','r','r','y','y','y','y','y','y','g','g','g','g','g','g']
        self.point_stat=[0,0,0]
        random.shuffle(self.cards)
        self.player_list=[]
        self.player_list.append(Player(self.count(self.cards[0:6]),0))
        self.player_list.append(Player(self.count(self.cards[6:12]),1))
        self.player_list.append(Player(self.count(self.cards[12:18]),2))

    def count(self,card_list):
        keep=[0,0,0]
        for i in card_list:
            if(i=='r'):
                keep[0]+=1
            elif(i=='y'):
                keep[1]+=1
            else:
                keep[2]+=1
        return keep

    def start(self):
        print("\t\t Let's Start The Game \n")
        #total 6 chances in game
        for i in range(0,6):
            
            #to keep track of cards played during a single chance
            chance_keep=[0,0,0]
            chance=(i%3)
            rotate=chance
            point=0
            print("player ",chance+1,"'s chance")
            
            for j in range(3):
                if(rotate==2):
                    chance_keep[rotate]=self.player_list[rotate].manual_play()
                else:
                    chance_keep[rotate]=self.player_list[rotate].apply_mind_and_respond(chance)
                rotate=(rotate+1)%3


                
            for color in chance_keep:
                if(color=='r'):
                    point+=1
                elif(color=='g'):
                    point=point-1
                else:
                    continue
            self.point_stat[chance]+=point
            print(chance_keep)    
            for objects in self.player_list:
                objects.feed_chance_played(chance_keep)

        for i in range(len(self.player_list)):
            print("Player ",i+1," has ",self.point_stat[i]," points")

            
        
obj1=game()
obj1.start()
