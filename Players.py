
class Player:
    def __init__(self,cards,identity):
        self.point_declare={'r':1,'y':0,'g':-1}
        self.hold_cards={'r':0,'y':0,'g':0}
        self.points_scored=[0,0,0]
        self.opp_hold_cards={'r':0,'y':0,'g':0}
        self.total_players=3
        self.identity=identity
        self.hold_cards['r']=cards[0]
        self.opp_hold_cards['r']=6-cards[0]

        self.hold_cards['y']=cards[1]
        self.opp_hold_cards['y']=6-cards[1]

        self.hold_cards['g']=cards[2]
        self.opp_hold_cards['g']=6-cards[2]

        
            
    def feed_chance_played(self,cards_played):
        i=self.identity
        score=0
        for j in cards_played:
            score+=self.point_declare[j]

        self.hold_cards[cards_played[i]]-=1
        for k in range(self.total_players-1):
            i=(i+1)%self.total_players
            self.opp_hold_cards[cards_played[i]]-=1
        i=(i+1)%self.total_players
        self.points_scored[i]+=score
        
    def apply_mind_and_respond(self,chance):
        if(chance!=self.identity):
            if(self.hold_cards['g']>0):
                return 'g'
            elif(self.hold_cards['y']>0):
                return 'y'
            else:
                return 'r'
        else:
            if(self.hold_cards['r']>0):
                return 'r'
            elif(self.hold_cards['y']>0):
                return 'y'
            else:
                return 'g'

    def manual_play(self):
        print("\t\tYou have following cards left\n")
        print("\t\tRed Cards-",self.hold_cards['r'])
        print("\t\tYellow Cards-",self.hold_cards['y'])
        print("\t\tGreen Cards-",self.hold_cards['g'])
        card=input("\t\tWhich color you wanna select-")
        if(self.hold_cards[card]>0):
            return card
        else:
            print("\t\tPlease select an available card")
            self.manual_play()
            
        
        
            
        
        
        
