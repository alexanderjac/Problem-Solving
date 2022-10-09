# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(topAncestor, descendantOne)
    depthTwo =getDepth(topAncestor, descendantTwo)
    if depthTwo>depthOne:
        for i in range(depthTwo-depthOne):
            descendantTwo = descendantTwo.ancestor
    elif depthOne>depthTwo:
        for i in range(depthOne - depthTwo):
            descendantOne = descendantOne.ancestor
    if descendantTwo ==   descendantOne  :
        return descendantTwo
    while depthOne != topAncestor:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
        if descendantOne ==descendantTwo:
            return descendantOne
def getDepth(topAncestor, descendant):
    depth =0
    while descendant != topAncestor:
        depth +=1
        descendant = descendant.ancestor
    return depth