class UnknownCommand(): 
    def __init__(self,bogus):
        self.bogusCommand = bogus
    
    def execute(self):
        return "I'm not sure what you mean by \""+self.bogusCommand+"\""