class Castle:
    def __init__(self):
        self.owner = ""
        self.dfs = 0
        self.atk = 0
        self.hp = 0
        self.level = 0
        self.color = ""
        self.state = ""
        
    # def __init__(self, owner, dfs, atk, hp):
    #     self.owner = owner.lower()
    #     self.dfs = dfs
    #     self.atk = atk 
    #     self.hp = hp
    
    
    def __str__(self):
        if self.state == "":
            return "𝅙"

        elif self.state == "1":
            return "▘"
        elif self.state == "2":
            return "▝"
        elif self.state == "3":
            return "▖"
        elif self.state == "4":
            return "▗"
        
        elif self.state == "12":
            return "▀"
        elif self.state == "13":
            return "▌"
        elif self.state == "14":
            return "▚"
        elif self.state == "23":
            return "▞"
        elif self.state == "24":
            return "▐"
        elif self.state == "34":
            return "▄"
        
        elif self.state == "234":
            return "▟"
        elif self.state == "134":
            return "▙"
        elif self.state == "124":
            return "▜"
        elif self.state == "123":
            return "▛"
        
        elif self.state == "1234":
            return "▉"
        
        return "ERROR"
    
    def __repr__(self) -> str:
        return self.__str__()