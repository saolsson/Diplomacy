class Connection:
    
    navyConn = False
    armyConn = False
    
    def __init__(self, oneTerritory, twoTerritory, seaConnection):
        self.id = oneTerritory.name + twoTerritory.name
        self.a = oneTerritory
        self.b = twoTerritory
        self.navyConn = self.a.navy and self.b.navy and seaConnection
        self.armyConn = self.a.army and self.b.army
        oneTerritory.addConnection(self)
        twoTerritory.addConnection(self)

    def otherTerritory(self,territory):
        if (self.a == territory):
            return self.b
        if (self.b == territory):
            return self.a
        return