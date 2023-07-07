import random
class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        
        self.name=name
        self.bowling=bowling
        self.batting=batting
        self.fielding=fielding
        self.running=running
        self.experience=experience
    
class Teams:
    def __init__(self, name, players):
        self.name=name
        self.players=players
        self.batting_order=[]
        self.current_players=[]
        self.captain=None
        self.bowler=None
        
    def select_caption(self, player_name):
        for player in self.players:
            if player.name==player_name:
              self.captain=player_name 
              break 
          
    def next_player(self):
        return self.batting_order[0]
        
        
    def select_bowler(self, bowler_name):
        for player in self.players:
            if player.name==bowler_name:
                self.bowler=bowler_name
                break
                
    
    def batting_order(self, player_names):
        for i in player_names:
            for j in players:
                if i==j.name:
                    self.batting_order.append(i)
    
class Field:
      def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage): 
        self.field_size=field_size
        self.fan_ratio=fan_ratio
        self.pitch_conditions =pitch_conditions
        self.home_advantage=home_advantage
        
    

class Umpire:
    def __init__(self, team1, team2):
        
        self.team2=team2
        self.team1=team1
        self.scores={team1.name: 0, team2.name:0}
        self.wickets={team1.name: 0, team2.name:0}
        self.overs={team1.name: 0, team2.name:0}
    
    def set_score(self, team, runs_scored):
        self.scores[team]=runs+self.scores[team]
        
    def set_wickets(self, team):
        self.wickets[team]=1+self.wickets[team]
    
    def set_overs(self, team):
        self.overs[team]=0.1+self.overs[team]
                
    
class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire
    def comment(self, batsman, bowler, runs):
        print(batsnamn.name, "scored", runs, "playing against", bowler.name )
   
   
class Match:
    def __init__(self, team1, team2, field, umpire):
        self.team1=team1
        self.team2=team2
        self.field=field
        self.umpire=Umpire(team1, team2)
        self.Commentator(self.umpire)
    
    def start_match():
        
        
    
    def change_innings():
        pass
    
    def end_match():
        pass