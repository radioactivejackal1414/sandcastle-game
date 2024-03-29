class Player:
    def __init__(self):
        self.name = ""
        self.color = ""
        self.cpu = None
        
        self.money = 100
        self.castles = []

    # def __init__(self, name, color):
    #     self.name = name
    #     self.color = color
        
    #     self.money = 100
    #     self.castles = []

    def __str__(self):
        return self.name + ", " + self.color
    
    def set_name_and_color(self):
        print("TODO")