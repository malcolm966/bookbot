class Wall:
    
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width
        self.armor = 10

    def get_cost(self):
        cost = self.armor * self.height
        return cost


    def fortify(self):
        self.armor *= 2 
