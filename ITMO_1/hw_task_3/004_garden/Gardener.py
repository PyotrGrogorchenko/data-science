class Gardener:

    def __init__(self, name, *plants):
        self.name = name
        self.plants = plants


    def care(self):
        for plant in self.plants:
            plant.grow()

    def harvest(self):
        for plant in self.plants:
            if not plant.isRipe():
                print('Not all apples are ripe')
                return
        for plant in self.plants:
            plant.harvest()
        print('The harvest is harvested')
