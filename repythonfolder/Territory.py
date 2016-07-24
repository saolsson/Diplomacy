import Country
import Connection
import ConnectionInfo
import Unit
import Army
import Navy

class Territory:
    def __init__(self, name="", parentList=[], supplycenter=0,navy=0, army=0):
        self.name = name
        parentList.append(self)
        self.supplyCenter = bool(supplycenter)
        self.navy = bool(navy)
        self.army = bool(army)
        self.coast = self.navy and self.army
        self.sea = self.navy and not self.army
        self.connections=[]
        self.navyConnections=[]
        self.armyConnections=[]
        self.unit = None
        self.firstOrder = 0
        self.armyFirstOrder = 0
        self.navyFirstOrder = 0
        self.secondOrder = 0
        self.armySecondOrder = 0
        self.navySecondOrder = 0
        self.naiveValue = 0
        self.mildValue = 0
        self.FIRSTORDERCENTERBONUS = 0

    def unitInTerritory(self):
        return self.unit
    
    def setCountry(self,country:Country.Country,unit:Unit.Unit):
        self.country = country    
        self.unit = unit

    def addConnections(self,connectionInfos):
        for connInfo in connectionInfos:
            if (type(connInfo) == ConnectionInfo.ConnectionInfo):
                territory = connInfo.territory
                seaConnection = connInfo.seaConnection
            else:
                territory = connInfo
                seaConnection = True
            quit = False
            for connect in territory.connections:
                if ((connect.id == (self.name + territory.name)) or (connect.id == (territory.name + self.name))):                  
                    quit = True
            if(not quit):
                conn = Connection.Connection(self,territory,seaConnection)
    
    def addConnection(self,connection):
        self.connections.append(connection)
        if (connection.navyConn):
            self.navyConnections.append(connection)
        if (connection.armyConn):
            self.armyConnections.append(connection)

    def updateFirstOrder(self):
        for conn in self.connections:
            if (conn.a == self):
                #print(self.FIRSTORDERCENTERBONUS* conn.b.supplyCenter)
                self.firstOrder += 1 + self.FIRSTORDERCENTERBONUS*(conn.b.supplyCenter)
                #self.firstOrder = self.firstOrder + self.FIRSTORDERCENTERBONUS*(conn.b.supplyCenter) + 1
            else:
                #print(self.FIRSTORDERCENTERBONUS* conn.b.supplyCenter)
                self.firstOrder += 1 + self.FIRSTORDERCENTERBONUS*(conn.b.supplyCenter)
                #self.firstOrder = self.firstOrder + self.FIRSTORDERCENTERBONUS*(conn.a.supplyCenter) + 1
        self.armyFirstOrder = (len(self.armyConnections) / self.firstOrder) * len(self.armyConnections)
        self.navyFirstOrder = (len(self.navyConnections) / self.firstOrder) * len(self.navyConnections)

    def updateSecondOrder(self):
        for conn in self.connections:
            if (conn.a == self):
                self.secondOrder = self.secondOrder + conn.b.firstOrder
                self.armySecondOrder = self.armySecondOrder + conn.b.armyFirstOrder
                self.navySecondOrder = self.navySecondOrder + conn.b.navyFirstOrder
            else:
                self.secondOrder = self.secondOrder + conn.a.firstOrder
                self.armySecondOrder = self.armySecondOrder + conn.a.armyFirstOrder
                self.navySecondOrder = self.navySecondOrder + conn.a.navyFirstOrder
    
    def updateValue(self):
        self.naiveValue = (10 * self.supplyCenter) + (10 * self.firstOrder) + (self.secondOrder)
        self.armyValue = ((10 * self.armyFirstOrder) + self.armySecondOrder)
        self.navyValue = ((10 * self.navyFirstOrder) + self.armySecondOrder)
        self.mildValue = (100 * self.supplyCenter) + self.armyValue + self.navyValue
        
    def armyVal(self):
        return self.armyValue 
    
    def navyVal(self):
        return self.navyValue

    def value(self):
        return self.mildValue
     