class Apple:
    __stages = ['blossom', 'green', 'red']

    def __init__(self, index):
        self.index = index
        self.stage = 0

    def isRipe(self):
        return self.stage == len(self.__stages) - 1

    def grow(self):
        self.stage = min(self.stage + 1, len(self.__stages) - 1)

