class Room:

    # Each room have 4 opening possible
    # By default each wall is closed and set to True
    # If the room have been visited we should not consider it anymore and set visited to True

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.N = True
        self.S = True
        self.E = True
        self.W = True
        self.visited = False

    def openDoor(self, x, y):
        return [["x", x], ["self.x", self.x], ["y", y], ["self.y", self.y]]

    def getN(self):
        return self.N

    def setN(self, boolean):
        self.N = boolean
        return self

    def getS(self):
        return self.S

    def setS(self, boolean):
        self.S = boolean
        return self

    def getE(self):
        return self.E

    def setE(self, boolean):
        self.E = boolean
        return self

    def getW(self):
        return self.W

    def setW(self, boolean):
        self.W = boolean
        return self

    def getIsVisited(self):
        return self.visited

    def setIsVisited(self, boolean):
        self.visited = boolean
        return self
