class Tree:
    __apples = []

    def __init__(self, *apples):
        self.__apples = [*apples]

    def isRipe(self):
        return all(a.isRipe() for a in self.__apples)

    def grow(self):
        for apple in self.__apples:
            apple.grow()

    def harvest(self):
        apples = self.__apples.copy()
        self.__apples.clear()
        return apples
