from Apple import Apple
from Tree import Tree
from Gardener import Gardener

apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)
apple4 = Apple(4)
apple5 = Apple(5)

tree = Tree(apple1, apple2, apple3, apple4, apple5)
tree.grow()
gardener = Gardener('Mike', tree)
gardener.harvest()
gardener.care()
gardener.harvest()
