class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
    
    def __str__(self):
        pisteet = self.goals + self.assists
        return f"{self.name:20} {self.team:10} {self.goals} + {self.assists} = {pisteet}"

