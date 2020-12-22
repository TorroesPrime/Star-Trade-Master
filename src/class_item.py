from game_state_instance import game_state_instance as gsi
class item():
    def __init__(self,stats,itemActions):
        self.name = stats[0]
        self.description = stats[1]
        self.weight = stats[2]
        self.actions = {}
        for action, response in itemActions.items():
 #           gsi.actions.append(action)
            self.actions.update({action:response})
        
    def get_name(self):
        return self.name
    
    def result_from_action(self,action):
        if action in self.actions.keys():
            return self.actions.get(action)
        else:
            return "You can not "+action+" a "+self.name
